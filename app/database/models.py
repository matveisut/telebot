
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, BigInteger

# импорт из родительской папки
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config

print(f"Database URL: {config.DATABASE_URL}")

engine = create_async_engine(url = config.DATABASE_URL)
  
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    __table_args__ = {'extend_existing': True}

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    tg_id = mapped_column(BigInteger)
    

class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    name: Mapped[str]  = mapped_column(String(25))


class Item(Base):
    __tablename__ = 'items'

    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    name: Mapped[str]  = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(120))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)