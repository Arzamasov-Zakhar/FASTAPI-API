from fastapi import APIRouter, Depends, Query

from lib.db import mysql_db

from ..dependencies import check_user_is_admin
from ..schemas.private import (PrivateCreateUserModel,
                               PrivateDetailUserResponseModel,
                               PrivateUpdateUserModel,
                               PrivateUsersListResponseModel)

private_router = APIRouter(tags=["admin"], dependencies=[Depends(check_user_is_admin)])


@private_router.post(
    "/private/users", response_model=PrivateDetailUserResponseModel, status_code=201
)
async def create_user(user_info: PrivateCreateUserModel):
    id = await mysql_db.create_user(user_info.dict())
    return await mysql_db.get_user_by_id(id)


@private_router.get("/private/users", response_model=PrivateUsersListResponseModel)
async def get_users(page: int = Query(..., gt=0), size: int = Query(..., gt=0)):
    data = await mysql_db.get_users(page, size)
    total = await mysql_db.get_total_users()
    cities = await mysql_db.get_cities()
    return {
        "data": data,
        "meta": {
            "pagination": {"total": total, "page": page, "size": size},
            "hint": {"city": cities},
        },
    }


@private_router.get(
    "/private/users/{pk}",
    response_model=PrivateDetailUserResponseModel,
)
async def get_user(pk: int):
    return await mysql_db.get_user_by_id(pk)


@private_router.delete("/private/users/{pk}", status_code=204)
async def delete_user(pk: int):
    await mysql_db.delete_user(pk)


@private_router.patch(
    "/private/users/{pk}",
    response_model=PrivateDetailUserResponseModel,
)
async def update_user(pk: int, user_info: PrivateUpdateUserModel):
    await mysql_db.update_user(pk, user_info.dict(exclude_unset=True))
    return await mysql_db.get_user_by_id(pk)
