from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

import models

from services.auth import (
    AuthService,
    get_current_user,
)
from typing import List

from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

templates = Jinja2Templates(directory="src/auth")


@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@router.post(
    '/sign-up/',
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
        user_data: models.UserCreate,
        auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=models.Token,
)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
):


    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )

#
# @router.get("/create")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "create.html", {"request": request}
#     )
#
#
# @router.get("/Admin_user")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "Admin_user.html", {"request": request}
#     )
#
#

# @router.get('/set')
# async def setting(response: Response):
#     response.set_cookie(key='refresh_token', value='helloworld', httponly=True)
#     return True
# @router.get(
#     '/user/',
#     response_model=models.User,
# )
# def get_user(user: models.User = Depends(get_current_user)):
#     return user
#
#
# @router.get(
#     '/get_all_user/',
#     response_model=list[models.User],
# )
# def get_user(user: models.User = Depends(get_current_user),
#              auth_service: AuthService = Depends(), ):
#     return auth_service.get_all_user(user)
#
# @router.get(
#     '/get_all_username/',
#     # response_model=list[models.Username],
# )
# def get_user(user: models.User = Depends(get_current_user),
#              auth_service: AuthService = Depends(), ):
#     return auth_service.get_all_username()
#
#
#
#
# @router.post(
#     '/update_roles_user',
# )
# def get_user(id: int,roles: str,user: models.User = Depends(get_current_user),
#              auth_service: AuthService = Depends(),):
#     return auth_service.update_user_roles(id,roles,user)
#
#
#
#
#
# @router.post(
#     '/update_all_roles',
# )
# def get_user(user: models.User = Depends(get_current_user),
#              auth_service: AuthService = Depends(),):
#     return auth_service.update_user_roles(user)
#


#
# @router.post(
#     '/update_password_user',
# )
# def get_user(id: int,password: str,user: models.User = Depends(get_current_user),
#              auth_service: AuthService = Depends(),):
#     return auth_service.update_user_password(id,password,user)

#
# @router.get(
#     '/get_my_UserPfofile/',
#     response_model=models.ModelUserPfofile_my_username,
# )
# def get_user(user: models.User = Depends(get_current_user),
#              auth_service: AuthService = Depends(), ):
#     return auth_service.get_my_UserPfofile(user)
#

#
#
# @router.post(
#     '/get_UserPfofile',
#     # response_model=models.UserTask,
#     # status_code=status.HTTP_200_OK,
# )
# def create_operation(
#         request: Request,
#         user_data: models.BaseUser,
#         auth_service: AuthService = Depends(),
# ):
#     try:
#         auth_service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
#     except:
#         return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
#     return auth_service.get_UserPfofile(user_data)
#
