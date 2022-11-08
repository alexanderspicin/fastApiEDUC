import datetime
from typing import List
from db.users import users
from base import BaseRepository
from models.user import User, UserIn


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> User:
        query = users.select().where(users.c.id == id).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, user: UserIn) -> User:
        user = User(
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password),
            is_company=user.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()

        )

        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

        self.database.execute()
        return

    async def update(self, user: UserIn) -> User:
        return

    async def get_by_email(self, email: str):
        query = users.select().where(users.c.email == email).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
