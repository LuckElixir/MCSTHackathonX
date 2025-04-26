import ui.main
from enum import Enum
import math

Type = Enum('Type', [('Music', 1), ('Math', 2), ('English', 3)

class Tasks:
    TYPES = []
    def __init__(self, name: str, type: Type, effort, baseHours, points, base) -> None:
        self.name = name
        self.type = type
        self.baseHours = baseHours
        self.effort = effort
        self.points = points
        self.base = 1.6

    def computeLevel(self) -> int:
        self.base = 1.6
        if self.points < 1:
            return 0
        return int(math.log(self.points, self.base))

    def computeRank(self) -> str:
        if self.computeLevel() < 10:
            return "Bronze League"







class Profile:
    def __init__(self, name) -> None:
        self.name : str = name
        self.tasks : list[Tasks] = []
        self
