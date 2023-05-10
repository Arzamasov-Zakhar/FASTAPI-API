from databases import Database
from sqlalchemy import (TEXT, Boolean, Column, Date, ForeignKey, Integer,
                        MetaData, Table, create_engine)
from sqlalchemy_utils import create_database, database_exists

engine = create_engine(
    "mysql+pymysql://user_manager:user_manager@127.0.0.1/user_manager"
)
if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData(engine)

city_table = Table(
    "city",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", TEXT),
)

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", TEXT),
    Column("last_name", TEXT),
    Column("other_name", TEXT),
    Column("email", TEXT),
    Column("phone", TEXT),
    Column("birthday", Date),
    Column("city", ForeignKey("city.id")),
    Column("additional_info", TEXT),
    Column("is_admin", Boolean),
    Column("password", TEXT),
)


metadata.create_all()

db = Database("mysql+aiomysql://user_manager:user_manager@127.0.0.1/user_manager")
