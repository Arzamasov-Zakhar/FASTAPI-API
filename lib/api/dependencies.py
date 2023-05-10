import typing as ty

from fastapi import Cookie, Depends
from fastapi.exceptions import HTTPException

from lib.db import mysql_db

from .schemas.common import CurrentUserResponseModel


async def get_user_id(id: ty.Union[int, None] = Cookie(None)):
    if id is None:
        raise HTTPException(401)
    return id


async def get_current_user(id: int = Depends(get_user_id)):
    return await mysql_db.get_user_by_id(id)


async def check_user_is_admin(
    user: CurrentUserResponseModel = Depends(get_current_user),
):
    if not user.is_admin:
        raise HTTPException(405)
