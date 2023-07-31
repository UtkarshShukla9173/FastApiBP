from tortoise import Tortoise
async def connectToDatabase():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.schemas.profile']}
    )