import ui.main
from enum import Enum
import math
import logging

Type = Enum('Type', [('Music', 1), ('Math', 2), ('English', 3)])

class Tasks:
    TYPES = []
    def __init__(self, name: str, type: Type, effort, baseHours, points, base) -> None:
        self.name = name
        self.type = type
        self.baseHours = baseHours
        self.effort = effort
        self.points = points
        self.base = 1.6
        self.hours: list[float] = []
        self.completion: list[bool] = []
        self.activityList = []
        self.pointsList: list[list] = []

    def computeLevel(self) -> int:
        self.base = 1.6
        if self.points < 1:
            return 0
        return int(math.log(self.points, self.base))

    def computeRank(self) -> str:
        if self.computeLevel() < 10:
            return "Bronze League"

    def log(self, time: int, activity: str, completion_input: bool):
        while 1:
            self.hours.append(time)
            self.activityList.append(activity)
            self.completion.append(completion_input)
            self.points *= 100




class Profile:
    def __init__(self, name) -> None:
        self.name : str = name
        self.tasks : list[Tasks] = []




