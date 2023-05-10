from fastapi import APIRouter, Response

from lib.db import mysql_db

from ..schemas.common import CurrentUserResponseModel
from ..schemas.login import LoginModel

login_router = APIRouter(tags=["auth"])


@login_router.post("/login", response_model=CurrentUserResponseModel)
async def login(login_info: LoginModel, response: Response):
    id = await mysql_db.get_user_id_by_login_info(**login_info.dict())
    user = await mysql_db.get_user_by_id(id)
    response.set_cookie(key="id", value=id)
    return user
