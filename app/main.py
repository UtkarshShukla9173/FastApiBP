from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from app.database.connectToDatabase import connectToDatabase

app = FastAPI()
async def connect():
    print("trying Conneted")
    await connectToDatabase()
    print("Database Conneted")
connect()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Tortoise.init_models('app/schemas', "models")

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.schemas.profile"]},
    generate_schemas=True,
    add_exception_handlers=True,
)