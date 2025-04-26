import ui.main
from enum import Enum
import math
import os
import logging
from filesave.main import *

class Type:
    MUSIC = 1
    MATH = 2
    ENGLISH = 3
    COMMUNITY_SERVICE = 4
class Effort:
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Tasks:
    TYPES = []

    def __init__(self, name: str, type: Type, effort: Effort, baseHours, points, base) -> None:
        self.name = name
        self.type: Type = type
        self.baseHours = baseHours
        self.effort = effort
        self.points = self.computePoints()

    def computePoints(self):
        points = 10
        if self.effort == Effort.HIGH:
            points *= 2
        elif self.effort == Effort.MEDIUM:
            points *= 1.5
        else:
            points = points
        if self.type == Type.COMMUNITY_SERVICE:
            points *= 3

    @staticmethod
    def notify(title, text):
        os.system("""
                    osascript -e 'display notification "{}" with title "{}"'
                    """.format(text, title))


class Profile:
    def __init__(self, name, points=0) -> None:
        self.base = 1.6
        self.name: str = name
        self.rank: str = self.computeRank()
        self.tasks: list[Tasks] = []
        self.league = self.computeRank()
        self.points = points

    def computeLevel(self) -> int:
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

    def addTask(self, name, ):
        self.tasks.append(Tasks())
