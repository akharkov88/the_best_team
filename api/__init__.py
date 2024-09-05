from fastapi import APIRouter

from . import (
    auth,
    main,
)
router = APIRouter()
router.include_router(auth.router)
router.include_router(main.router)