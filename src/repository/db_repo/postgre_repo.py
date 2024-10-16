from src.repository.config.engine import async_session_factory
from sqlalchemy import select, update, delete
from .abc_repo import AbstractRepository
from ..table_orm.declarative_base.declarative_base import Base
from pydantic import BaseModel

class PostgreSQLRepository(AbstractRepository):
    asf = async_session_factory
    table = Base

    async def insert_data(self, insert_data: dict | list):
        async with self.asf() as session:
            if type(insert_data) == dict:
                value = self.table(**insert_data)
                session.add(value)
            else:
                value = self.table(insert_data)
                session.add_all(insert_data)
            await session.flush()
            await session.refresh(value)
            await session.commit()
            return value

    async def select_data(self, filter_data: dict | None):
        async with self.asf() as session:
            if type(filter_data) is dict:
                query = (
                    select(self.table)
                    .filter_by(**filter_data)
                )
            else:
                query = (
                    select(self.table)
                )
            result = await session.execute(query)
            return result

    async def update_data(self, upd_id: int, upd_data: dict) -> None:
        async with self.asf() as session:
            upd = (
                update(self.table)
                .filter(self.table.id == upd_id)
                .values(upd_data)
            )
            await session.execute(upd)
            await session.commit()

    async def delete_data(self, id: int):
        async with self.asf() as session:
            query = (
                delete(self.table)
                .filter(self.table.id == id)
            )
            await session.execute(query)
            await session.commit()

    async def select_data_filter(self, filter_data: list):
        async with self.asf() as session:
            query = (
                select(self.table)
                .filter(*filter_data)
            )
            print(*filter_data)
            result = await session.execute(query)
            return result

    def get_dto_form(self, dto_form: BaseModel, res: list):
        result_dto = [dto_form.model_validate(row, from_attributes=True) for row in res]
        if len(result_dto) == 1:
            result_dto = result_dto[0]
        return result_dto
