import ui.main
from enum import Enum
import math
import os
import logging
from filesave.main import *



class Tasks:
    TYPES = []

    def __init__(self, name: str, type, effort: int, baseHours) -> None:
        self.name = name
        self.type: str = type
        self.baseHours = baseHours
        self.effort = effort
        self.computePoints()

    def computePoints(self):
        points = 2
        if self.effort == 3:
            points *= 2
        elif self.effort == 2:
            points *= 1.5
        else:
            points = points
        if self.type.lower() == "community service":
            points *= 5
        self.points = int(points)
    @staticmethod
    def notify(title, text):
        os.system("""
                    osascript -e 'display notification "{}" with title "{}"'
                    """.format(text, title))


class Profile:
    def __init__(self, name, points=0) -> None:
        self.base = 1.6
        self.points = points
        self.name: str = name
        self.rank: str = self.computeRank()
        self.tasks: list[Tasks] = []
        self.league = self.computeRank()


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

    def addTask(self, name, type, effort, baseHours):
        self.tasks.append(Tasks(name, type, effort, baseHours))

    def removeTask(self, task_name):
        for task in self.tasks:
            if task.name == task_name:

                self.points += task.points
                self.tasks.remove(task)
                return
        print(f"Task '{task_name}' not found.")
