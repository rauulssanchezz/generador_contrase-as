from enum import Enum

class Complexity(str, Enum):
    hard = "hard"
    medium = "medium"
    easy = "easy"

    @property
    def value_num(self):
        mapping = {
            "hard": 30,
            "medium": 20,
            "easy": 10
        }
        return mapping[self.value]
