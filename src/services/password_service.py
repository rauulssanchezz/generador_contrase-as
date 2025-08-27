from random import randint
from src.utils.enums.complexity_enum import Complexity
import bcrypt

class PasswordService:
    @staticmethod
    def generate_password(complexity: Complexity):
        try:
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
        except:
            return 'Ha ocurrido un error intentalo mas tarde.'

    @staticmethod
    def hash_password(password: str):
        try:
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        except:
            return 'Ha ocurrido un error intentalo mas tarde.'
    
    @staticmethod
    def check_password(hashed_password: str, password: str):
        try:
            return bcrypt.checkpw(password.encode(), hashed_password.encode())
        except ValueError:
            return False
        except:
            return 'Ha ocurrido un error intentalo mas tarde.'
