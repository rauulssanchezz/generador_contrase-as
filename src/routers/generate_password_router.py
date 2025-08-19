from fastapi.routing import APIRouter
from fastapi import Query
from src.services.password_service import PasswordService
from src.utils.enums.complexity_enum import Complexity

router = APIRouter(
    prefix='/password',
    tags=['Generate Password']
)

@router.get('/generate')
def generate_password(complexity: Complexity = Query(...)):
    return PasswordService.generate_password(complexity=complexity)

@router.post('/hash')
def hash_password(password: str):
    return PasswordService.hash_password(password=password)

@router.post('/check')
def check_password(password:str, hashed_password):
    return PasswordService.check_password(password=password, hashed_password=hashed_password)
