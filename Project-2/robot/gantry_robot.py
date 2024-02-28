import sys
sys.path.append('./')

from utils.utils import current_state
from robot.base_robot import BaseRobot

class GantryRobot(BaseRobot):
    def __init__(self):
        super().__init__(name = "Gantry", payload = 15, weight = 500, bins = ['bin3', 'bin4'])
        self._small_rail_length = 12
        self._long_rail_length = 20
        self._small_rail_height = 5
        self._long_rail_height = 4.75
    
    def _pickup_tray(self, tray, table):
        '''Input: tray  Tray to pick up
        Input: table  Table where the tray is located
        Result: Execute _place_tray() if tray is successfully picked up
        '''
        tray_obj = current_state['trays'][tray]
        if tray_obj['location'] == 'table':
            self._gripper.activate_gripper()
            self._gripper._object_held = tray
            tray_obj['location'] = 'gripper'
            agv = current_state['kit']['agv']
            print(f"pickup_tray({self._name}, {tray}, {table})")
            self._place_tray(tray, agv)
        else:
            return

    def _place_tray(self, tray, agv):
        '''Input: tray Tray the robots gripper is holding
        Input: agv AGV on which the tray needs to placed
        Result: Execute _find_part() if tray is successfully placed on agv
        '''
        tray_obj = current_state['trays'][tray]
        if self._gripper._object_held == tray:
            self._gripper.deactivate_gripper()
            self._gripper._object_held = None
            tray_obj['location'] = agv
            print(f"place_tray({self._name}, {tray}, {agv})")
            self._find_part()
        else:
            return

    def __str__(self):
        pass

    def plan(self):
        '''Result: Execute _pickup_tray() if the required tray is found
        tray ← Tray required for kitting
        '''
        tray = current_state['kit']['tray']
        tray_obj = current_state['trays'][tray]
        if tray_obj['location'] is not None:
            table = tray_obj['location']
            self._pickup_tray(tray, table)