from fastapi import FastAPI, APIRouter
import uvicorn
from contextlib import asynccontextmanager

from db_connection import database
from routes import crud_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
api_router = APIRouter(prefix="/api")

api_router.include_router(crud_router)

app.include_router(api_router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
    
