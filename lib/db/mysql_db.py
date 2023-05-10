import typing as ty

from sqlalchemy import delete, func, insert, select, update

from .db_instance import city_table, db, user_table


async def connect():
    await db.connect()


async def disconnect():
    await db.disconnect()


async def get_user_id_by_login_info(login: str, password: str) -> int:
    return await db.fetch_val(
        select(user_table).where(
            (user_table.c.email == login) & (user_table.c.password == password)
        ),
        column="id",
    )


async def get_user_by_id(id: int):
    return await db.fetch_one(select(user_table).where(user_table.c.id == id))


async def update_current_user(id: int, user_info: ty.Dict[str, ty.Any]):
    await db.execute(
        update(user_table).where(user_table.c.id == id).values(**user_info)
    )


async def get_users(page: int, size: int):
    return await db.fetch_all(select(user_table).limit(size).offset((page - 1) * size))


async def get_total_users():
    return await db.fetch_val(select(func.count(user_table.c.id)))


async def create_user(user_info: ty.Dict[str, ty.Any]):
    id = await db.execute(insert(user_table).values(**user_info))
    return id


async def get_cities():
    return await db.fetch_all(select(city_table))


async def delete_user(id: int):
    await db.execute(delete(user_table).where(user_table.c.id == id))


async def update_user(id: int, user_info: ty.Dict[str, ty.Any]):
    await db.execute(
        update(user_table).where(user_table.c.id == id).values(**user_info)
    )
