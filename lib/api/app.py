from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from lib.api.routes import (login_router, logout_router, private_router,
                            users_router)
from lib.db import mysql_db

app = FastAPI()


@app.on_event("startup")
async def startup():
    await mysql_db.connect()


@app.on_event("shutdown")
async def shutdown():
    await mysql_db.disconnect()


app.include_router(login_router)
app.include_router(logout_router)
app.include_router(users_router)
app.include_router(private_router)


@app.exception_handler(Exception)
async def handler_exceptions(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Что-то пошло не так, мы уже исправляем эту ошибку",
            "code": 400,
        },
    )
