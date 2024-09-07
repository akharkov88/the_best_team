from datetime import (
    datetime,
    timedelta,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordBearer
from jose import (
    JWTError,
    jwt,
)
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

import models
import tables
import json

from database import get_session
from settings import Settings as settings
import traceback

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')
from fastapi.encoders import jsonable_encoder


def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
    return AuthService.verify_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_token(cls, token: str) -> models.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            print(traceback.format_exc())
            raise exception from None

        user_data = payload.get('user')

        try:
            user = models.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: tables.User) -> models.Token:
        user_data = models.User.from_orm(user)
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return models.Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(
            self,
            user_data: models.UserCreate,
    ) -> models.Token:
        user = tables.User(
            # email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
            name=user_data.name,
            surname=user_data.surname,
        )
        self.session.add(user)
        self.session.commit()


        return self.create_token(user)

    def authenticate_user(
            self,
            username: str,
            password: str,
    ) -> models.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        user = (
            self.session
            .query(tables.User)
            .filter(tables.User.username == username)
            .first()
        )

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)

    def get_all_user(self, user_data: models.UserCreate) -> list[models.UserCreate2]:
        try:
            if json.loads(user_data.roles).count('ADMIN') > 0:
                operation = (
                    self.session
                    .query(tables.User)
                    .order_by(tables.User.id)
                    .all()
                )
                # if not operation:
                #     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
                # return jsonable_encoder(operation)
                return jsonable_encoder(operation)
            else:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не хватает прав")
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def get_all_username(self,) :
        try:
            operation = (
                self.session
                .query(tables.UserPfofile.username,tables.UserPfofile.first_name,tables.UserPfofile.last_name )
                .all()
            )
            # if not operation:
            #     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
            # return jsonable_encoder(operation)
            rez={}
            for user in operation:
                rez[user.username]=user.first_name+" "+user.last_name
            return rez
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def update_user_roles(self, id, roles, user_data: models.UserCreate) -> bool:
        try:
            if json.loads(user_data.roles).count('Admin') > 0:

                # operation = tables.TaskForm(
                #     NameTechTask=TechTaskDATA.NameTechTask,
                #     TechTaskClient=TechTaskDATA.TechTaskClient,
                #     TechTaskProject=TechTaskDATA.TechTaskProject,
                #     TechTaskPPR=TechTaskDATA.TechTaskPPR,
                #     TechTaskOverhead=TechTaskDATA.TechTaskOverhead,
                #     TechTaskDateKP=TechTaskDATA.TechTaskDateKP,
                #     TechTaskDateEndWork=TechTaskDATA.TechTaskDateEndWork,
                #     TechTaskPrice=TechTaskDATA.TechTaskPrice,
                #     TechTaskLeaderKP=TechTaskDATA.TechTaskLeaderKP,
                # )

                # existing_row = self.session.query(tables.TaskForm).filter(tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask).first()
                # existing_row.column1 = 'new_value1'
                # existing_row.column2 = 'new_value2'
                # existing_row.TechTaskClient = TechTaskDATA.TechTaskClient,
                # self.session.commit()

                self.session.query(tables.User).filter(tables.User.id == id).update(dict(roles=roles))
                self.session.commit()
                return HTTPException(status.HTTP_200_OK)
            else:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не хватает прав")
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Запись с таким именем уже существует запись")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    def get_all_roles(self) -> bool:
        try:
            operation = (
                self.session
                .query(tables.ListUserRoles.role, tables.ListUserRoles.name_roles)
                .all()
            )

            if not operation:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="")
            rez={}
            for user in operation:
                rez[user.role]=user.name_roles
            return rez

        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Запись с таким именем уже существует запись")
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

    def update_user_password(self, id, password, user_data: models.UserCreate) -> bool:
        try:
            if json.loads(user_data.roles).count('Admin') > 0:

                self.session.query(tables.User).filter(tables.User.id == id).update(
                    dict(password_hash=self.hash_password(password)))
                self.session.commit()
                return HTTPException(status.HTTP_200_OK)
            else:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Не хватает прав")
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_400_BAD_REQUEST)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


    # def get_my_UserPfofile(self, user_data: models.BaseUser) -> models.ModelUserPfofile_my_username:
    #             operation = (
    #                 self.session
    #                 .query(tables.UserPfofile)
    #                 .filter(tables.UserPfofile.username == user_data.username)
    #                 .first()
    #             )
    #             if not operation:
    #                 raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
    #             my_profile=jsonable_encoder(operation)
    #             my_profile["my_username"]=user_data.username
    #
    #             return my_profile


    # def get_UserPfofile(self, user_data: models.BaseUser) -> list[models.UserProfile]:
    #             operation = (
    #                 self.session
    #                 .query(tables.UserPfofile)
    #                 .filter(tables.User.username == user_data.username)
    #                 .first()
    #             )
    #             if not operation:
    #                 raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
    #             return jsonable_encoder(operation)
    #
