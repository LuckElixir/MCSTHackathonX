import ui.main
from enum import Enum
import math
import os

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
        return int(math.log(self.points, self.base) + 0.001 * self.points)

    def computeRank(self) -> str:
        if self.computeLevel() < 10:
            return "Bronze League"
        elif self.computeLevel() < 25:
            return "Silver League"
        elif self.computeLevel() < 20:
            return "Gold League"
        elif self.computeLevel() < 25:
            return "Platinum League"
        elif self.computeLevel() < 30:
            return "Crystal League"
        elif self.computeLevel() < 35:
            return "Masters League"
        elif self.computeLevel() < 40:
            return "Titans League"
        elif self.computeLevel() >= 40:
            return "Ultimates League"
        return "No League"

    def notify(tit  le, text):
        os.system("""
                    osascript -e 'display notification "{}" with title "{}"'
                    """.format(text, title))














class Profile:
    def __init__(self, name) -> None:
        self.name : str = name
        self.tasks : list[Tasks] = []
        self
