import typing as ty
from datetime import date

from pydantic import BaseModel


class UpdateUserModel(BaseModel):
    first_name: ty.Union[str, None]
    last_name: ty.Union[str, None]
    other_name: ty.Union[str, None]
    email: ty.Union[str, None]
    phone: ty.Union[str, None]
    birthday: ty.Union[date, None]


class UpdateUserResponseModel(BaseModel):
    first_name: str
    last_name: str
    other_name: str
    email: str
    phone: str
    birthday: date


class UsersListElementModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class UsersListResponseMetaPaginationModel(BaseModel):
    total: int
    page: int
    size: int


class UsersListResponseMetaModel(BaseModel):
    pagination: UsersListResponseMetaPaginationModel


class UsersListResponseModel(BaseModel):
    data: ty.List[UsersListElementModel]
    meta: UsersListResponseMetaModel
