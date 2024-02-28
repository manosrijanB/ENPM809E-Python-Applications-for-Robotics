import sys
sys.path.append('./')

from robot.base_robot import BaseRobot

class LinearRobot(BaseRobot):
    def __init__(self):
        super().__init__(name = "UR10", payload = 10, weight = 200, bins = ['bin1', 'bin2'])
        self._linear_rail_length = 10
    
    def __str__(self):
        pass

    def plan(self):
        self._find_part()