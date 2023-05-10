from fastapi import APIRouter, Depends, Query

from lib.db import mysql_db

from ..dependencies import get_current_user, get_user_id
from ..schemas.common import CurrentUserResponseModel
from ..schemas.users import (UpdateUserModel, UpdateUserResponseModel,
                             UsersListResponseModel)

users_router = APIRouter(tags=["user"])


@users_router.get("/users/current", response_model=CurrentUserResponseModel)
async def get_current_user(user: CurrentUserResponseModel = Depends(get_current_user)):
    return user


@users_router.patch("/users/current", response_model=UpdateUserResponseModel)
async def update_current_user(
    update_user_info: UpdateUserModel,
    id: CurrentUserResponseModel = Depends(get_user_id),
):
    await mysql_db.update_current_user(id, update_user_info.dict(exclude_unset=True))
    return await mysql_db.get_user_by_id(id)


@users_router.get("/users", response_model=UsersListResponseModel)
async def get_users(page: int = Query(..., gt=0), size: int = Query(..., gt=0)):
    data = await mysql_db.get_users(page, size)
    total = await mysql_db.get_total_users()
    return {
        "data": data,
        "meta": {"pagination": {"total": total, "page": page, "size": size}},
    }
