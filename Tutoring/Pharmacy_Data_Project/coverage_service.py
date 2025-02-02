from dataclasses import dataclass
from random import choice, randrange
@dataclass
class Coverage:
    coverageClass: str
    copay: float
    outOfPocket: float

class CoverageService:
    def __init__(self):
        self.coverage_classes = ['a7', 'c1', 'd6', 'x9']

    def get_coverage(self, id, fname, lname, med, dos):
        return Coverage(
            choice(self.coverage_classes),
            randrange(10, 80),
            randrange(50, 1500)
        )