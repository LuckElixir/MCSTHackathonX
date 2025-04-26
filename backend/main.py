import ui.main
from enum import Enum

Type = Enum('Type', [('Music', 1), ('Math', 2), ('English', 3)])

class Tasks:
    TYPES = []
    def __init__(self, name: str, type: Type, effort, baseHours) -> None:
        self.name = name
        self.type = type
        self.baseHours = baseHours
        self.effort = effort
    
    def computeXP(self, hours) -> int:
        XP = None
        return XP

class Profile:
    def __init__(self, name) -> None:
        self.name : str = name
        self.tasks : list[Tasks] = []
