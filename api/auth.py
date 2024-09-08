from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,

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
@router.get("/signup")
async def root(request: Request):
    return templates.TemplateResponse(
        "signup.html", {"request": request}
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
def sign_in(response: Response,
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
):
    token=auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )
    response.set_cookie(key="Authorization", value=token.access_token, httponly=True)
    return token
