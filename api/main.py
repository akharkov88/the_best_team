from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    Response,
    Path,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from fastapi.responses import FileResponse

from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates

import models,json
import os,pathlib
from services.main import (
    TaskServices,
)
from services.auth import (
    AuthService,
    get_current_user,
)
from services.main import TaskServices
# from services.UserProfile import UserProfileServices

router = APIRouter(
    prefix='/main',
    tags=['main'],
)


templates = Jinja2Templates(directory="src/main")


@router.get('/', )
def get_operation(request: Request,
                  Auth_Service: AuthService = Depends(), ):
    try:
        Auth_Service.verify_token(str(request.cookies.get('Authorization')).replace("bearer ", ""))
    except:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )