from fastapi import APIRouter, Response

logout_router = APIRouter(tags=["auth"])


@logout_router.get("/logout", status_code=200)
async def logout(response: Response):
    response.delete_cookie(key="id")
