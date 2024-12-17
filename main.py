import uvicorn
from fastapi import FastAPI

from app.api.endpoints.users import user_router
from app.api.endpoints.currency import currency_router
from app.api.endpoints.pingpong import  pingpong_router


app = FastAPI(title="Currency exchange")

app.include_router(user_router)
app.include_router(currency_router)
app.include_router(pingpong_router)


if __name__ == "__main__":
    uvicorn.run(app)
