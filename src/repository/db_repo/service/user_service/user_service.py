from src.repository.db_repo.postgre_repo import PostgreSQLRepository
from src.repository.table_orm.user import User
from  ..dto.user_dto import UserPostDTO


class UserService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_user(self, filter_data: dict) -> list[UserPostDTO] | UserPostDTO | None:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(UserPostDTO, res)
        return result_dto
    
    async def insert_user(self, insert_data: dict | list) -> User:
        value = await self.insert_data(insert_data)
        return value.id
    
    async def update_params(self, upd_id: int, upd_data: dict) -> User:
        await self.update_data(upd_id, upd_data)
   

user_service = UserService(User)