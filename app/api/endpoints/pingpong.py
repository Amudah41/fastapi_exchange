from fastapi import APIRouter
from fastapi.responses import FileResponse

pingpong_router = APIRouter(prefix="/waiting", tags=["Waiting"])



@pingpong_router.get("/pingpong")
def list_currencies():
    return FileResponse("./app/data/ping.html")
