from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import ProgrammingError


async def is_table_exist(engine, table) -> bool:
    """
    The function checks if a table exists in the database
    """
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        async with session.begin():
            try:
                await session.execute(select(table))
                return True
            except ProgrammingError:
                return False


async def all_obj(engine, table) -> None:
    """
    The function displays ALL objects from the table.
    """
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(table))
            for items in result.scalars().all():
                print(items)


async def group_obj(engine, table, group: str) -> None:
    """
    The function displays a group of objects from the database. Grouping by product type.
    Available groups: "шар", "яйцо", "шкатулка"
    """
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        async with session.begin():
            statement = select(table).where(table.kind == group)
            result = await session.execute(statement)
            for items in result.scalars().all():
                print(items)


def write_parse_data_to_database(goods: list[tuple[str, str, str, str, str | None, str]],
                                 table,
                                 pr_id,
                                 session) -> None:
    prod_id = pr_id
    for good in goods:
        link = good[0]
        photo = good[1]
        kind = good[2]
        material = good[3]
        size = good[4]
        price = good[5]
        session.add(
            table(
                product_id=prod_id,
                site_link=link,
                photo=photo,
                kind=kind,
                material=material,
                size=size,
                price=price
            )
        )
        prod_id += 1


async def filling_base(engine, table, goods) -> None:
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        async with session.begin():
            product_id = 1
            write_parse_data_to_database(goods, table, product_id, session)
        await session.commit()
        print("The database has been filled with data")
