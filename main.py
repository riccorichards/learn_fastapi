from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import delete_tables, create_table
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("database was cleaned")
    await create_table()
    print("database is ready to work")
    yield
    print("Stop server!")
    

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)
