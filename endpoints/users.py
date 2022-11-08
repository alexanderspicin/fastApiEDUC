from typing import List

from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository
from models.user import User, UserIn
from repositories.users import UserRepository

router = APIRouter()


@router.get('/', response_model=List[User])
async def read_user(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post('/', response_model=User)
async def create(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(user)
