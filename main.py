import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from create_bot import dp, bot
import commands
import handlers
from db.create_base import connect_database
from db.models import models_init
from db.base_utils import is_table_exist, filling_base
from parse.goods import goods as goods
from db.models import Product

commands.register_handlers(dp)
handlers.register_handlers(dp)


async def bot_launch():
    print("The bot has been launched")
    await dp.start_polling(bot)


async def main():
    """
    password=os.getenv("PSQL_PASS")) is the password from the user in the postgresql system,
    if you do not have a password, leave the field blank.
    """
    await connect_database(
        user="postgres",
        database="kamnerez_db",
        password=os.getenv("PSQL_PASS"))
    engine = create_async_engine(f"postgresql+asyncpg://postgres:{os.getenv('PSQL_PASS')}@localhost/kamnerez_db")
    is_table = await is_table_exist(engine, Product)
    if not is_table:
        await models_init(engine)
        await filling_base(engine, Product, goods)
    await bot_launch()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print("The Bot has been stopped")
