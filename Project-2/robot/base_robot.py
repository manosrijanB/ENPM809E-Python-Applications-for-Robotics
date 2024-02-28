import sys
sys.path.append('./')

from abc import ABC
from gripper.gripper import Gripper
from utils.utils import current_state

class BaseRobot(ABC):
    def __init__(self, name, payload, weight, bins = [], category = "industrial"):
        self._name = name
        self._category = category
        self._payload = payload
        self._weight = weight
        self._gripper: Gripper = None
        self._accessible_bins = bins
        
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @property
    def payload(self):
        return self._payload
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def accessible_bins(self):
        return self._accessible_bins
    
    @accessible_bins.setter
    def accessible_bins (self, bins):
        self._accessible_bins = bins      
        
          
    @property
    def gripper(self):
        return self._gripper
    
    @gripper.setter
    def gripper(self, obj):
       self._gripper = obj

    def _remove_part_from_bin(self, bin):
        '''Input: bin, bin from current_state
           Result: Number of parts in bin decreased by 1
        '''
        bin_obj = current_state['bins'][bin]
        bin_obj['part_quantity'] -= 1

    def _find_part(self):
        '''Result: Execute _pickup_part() if a part is found
        '''
        found_part = None
        found_bin = None
        tray = current_state['kit']['tray']
        tray_obj = current_state['trays'][tray]
        expected_parts = tray_obj['expected_parts']
        current_parts = tray_obj['current_parts']
        # Remove parts from remaining_parts which are in current_parts
        remaining_parts = expected_parts[:]
        for part in current_parts:
            remaining_parts.remove(part)

        for part_to_look_for in remaining_parts:
            if found_part is None:
                for bin in self._accessible_bins:
                    bin_obj = current_state['bins'][bin]
                    part_type = bin_obj['part_type']
                    part_quantity = bin_obj['part_quantity']
                    if part_type == part_to_look_for:
                        if part_quantity > 0:
                            found_part = part_type
                            found_bin = bin
            else: break

        if found_bin is not None:
            if found_part is not None:
                self._pickup_part(found_bin, found_part)

    def _pickup_part(self, bin, part):
        '''Input: bin  Bin where part is located
        Input: part  Part to pick up
        Result: Execute _place_part(tray, part, agv) if pickup is successful
        '''
        kit_obj = current_state['kit']
        bin_obj = current_state['bins'][bin]
        if kit_obj['complete'] is True:
            print("Kit is complete")
            return
        if self._gripper._object_held is None:
            self._gripper.activate_gripper()
            self._gripper._object_held = part
            bin_obj['part_quantity'] -= 1
            print(f"pickup_part({self._name}, {bin}, {part})")
        else:
            print("Robot's gripper is already holding an object")
            return
        tray = current_state['kit']['tray']
        agv = current_state['kit']['agv']
        self._place_part(tray, part, agv)

    def _place_part(self, tray, part, agv):
        ''''Input: tray  Tray where the part should be placed
        Input: part Part being held by the robots gripper
        Input: agv AGV where the tray is located
        Result: Execute _find_part() if part is successfully placed
        '''
        if self._gripper._object_held != part:
            return
        self._gripper.deactivate_gripper()
        self._gripper._object_held = None
        print(f"place_part({self._name}, {tray}, {part}, {agv})")

        tray_obj = current_state['trays'][tray]
        tray_obj['current_parts'].append(part)
        current_parts = tray_obj['current_parts']
        expected_parts = tray_obj['expected_parts']

        if expected_parts == current_parts:
            current_state['kit']['complete'] == True
            station = current_state['agvs'][agv]['destination'] 
            print('kit is complete')
            print(f'shipping {agv} to {station}')
        else:
            self._find_part()