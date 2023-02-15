import asyncpg


async def connect_database(user, database, password=None):
    try:
        await asyncpg.connect(
            user=user,
            database=database,
            password=password,
        )
        print("Database is ready to work")
    except asyncpg.exceptions.ConnectionDoesNotExistError:
        await create_database(
            user=user,
            database=database,
            password=password
        )
        print("Database has been created")


async def create_database(user, database, password):
    conn = await asyncpg.connect(
        user=user,
        password=password
    )
    await conn.execute(
        f'CREATE DATABASE "{database}"'
    )
    await conn.close()
