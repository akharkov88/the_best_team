import uvicorn
from settings import Settings
from api import router
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException


async def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('404.html', {'request': request}, status_code=404)


async def internal_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('500.html', {'request': request}, status_code=500)


templates = Jinja2Templates(directory="src/error")

exception_handlers = {
    404: not_found_error,
    500: internal_error
}

app = FastAPI(exception_handlers=exception_handlers)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(Path(__file__).parent.parent.absolute() , "the_best_team","src","static")),
    name="static",
)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
        host=Settings.server_host,
        port=Settings.server_port
                )
