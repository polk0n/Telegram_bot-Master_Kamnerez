import os
import asyncio
from create_bot import dp, bot
import commands
import handlers
from db.create_base import connect_database

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
    bot_task = asyncio.create_task(bot_launch())
    base_task = asyncio.create_task(
        connect_database(
            user="postgres",
            database="kamnerez_db",
            password=os.getenv("PSQL_PASS"))
    )
    await bot_task
    await base_task


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print("The Bot has been stopped")
