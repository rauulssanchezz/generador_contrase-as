from random import randint
from src.utils.enums.complexity_enum import Complexity
import bcrypt

class PasswordService:
    @staticmethod
    def generate_password(complexity: Complexity):
        plain_password = ''
        characters = ''

        if Complexity.easy == complexity:
            characters = 'ABCDEFGHIJKLMNÑOPQRSTVWXYZ'
        
        elif Complexity.medium == complexity:
            characters = 'ABCDEFGHIJKLMNÑOPQRSTVWXYZ1234567890'

        elif Complexity.hard == complexity:
            characters = 'ABCDEFGHIJKLMNÑOPQRSTVWXYZ1234567890!|·#ª$%&/()¬?¿-_Ç*^.'

        characters += characters.lower()

        for _ in range(complexity.value_num):
                random_int = randint(0, len(characters) - 1)
                plain_password += characters[random_int]

        return plain_password

    @staticmethod
    def hash_password(password: str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    @staticmethod
    def check_password(hashed_password: str, password: str):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
