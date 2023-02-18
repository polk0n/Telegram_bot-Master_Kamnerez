import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

engine = create_async_engine(f"postgresql+asyncpg://postgres:{os.getenv('PSQL_PASS')}@localhost/kamnerez_db")
Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer)
    site_link = Column(String, primary_key=True)
    photo = Column(String)
    kind = Column(String, nullable=False)
    material = Column(String, nullable=False)
    size = Column(String)
    price = Column(String)

    def __repr__(self):
        return f"{self.product_id}, {self.kind}, {self.material}, {self.size}, {self.photo}"


async def models_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(models_init())
