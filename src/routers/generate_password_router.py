from fastapi.routing import APIRouter
from fastapi import Body
from src.services.generate_password_service import GeneratePasswordService
from src.utils.enums.complexity_enum import Complexity

router = APIRouter(
    prefix='/password',
    tags=['Generate Password']
)

@router.post('/generate')
def generate_password(complexity: Complexity = Body()):
    return GeneratePasswordService.generate_password(complexity=complexity)
