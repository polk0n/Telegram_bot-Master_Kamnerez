import asyncio
from create_bot import dp, bot
import commands
import handlers

commands.register_handlers(dp)
handlers.register_handlers(dp)


async def main():
    print("The bot has been launched")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except(KeyboardInterrupt, SystemExit):
        print("The Bot has been stopped")
