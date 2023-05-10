import typing as ty
from datetime import date

from pydantic import BaseModel, Field

from .users import UsersListElementModel, UsersListResponseMetaModel


class PrivateCreateUserModel(BaseModel):
    first_name: str
    last_name: str
    other_name: ty.Union[str, None]
    email: str
    phone: ty.Union[str, None]
    birthday: ty.Union[date, None]
    city: ty.Union[int, None]
    additional_info: ty.Union[str, None]
    is_admin: bool
    password: str


class PrivateDetailUserResponseModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    other_name: str = Field("")
    email: str
    phone: str = Field("")
    birthday: date = Field("")
    city: int = Field(0)
    additional_info: str = Field("")
    is_admin: bool


class CitiesHintModel(BaseModel):
    id: int
    name: str


class PrivateUsersListResponseMetaHintModel(BaseModel):
    city: ty.List[CitiesHintModel]


class PrivateUsersListResponseMetaModel(UsersListResponseMetaModel):
    hint: PrivateUsersListResponseMetaHintModel


class PrivateUsersListResponseModel(BaseModel):
    data: ty.List[UsersListElementModel]
    meta: PrivateUsersListResponseMetaModel


class PrivateUpdateUserModel(BaseModel):
    first_name: ty.Union[str, None]
    last_name: ty.Union[str, None]
    other_name: ty.Union[str, None]
    email: ty.Union[str, None]
    phone: ty.Union[str, None]
    birthday: ty.Union[date, None]
    city: ty.Union[int, None]
    additional_info: ty.Union[str, None]
    is_admin: ty.Union[bool, None]
