
class Gripper:
    def __init__(self, name, weight = 2, closing_speed = 150):
        self._name = name
        self._weight = weight
        self._closing_speed = closing_speed
        self._enable = False
        self._object_held = None
        
    @property
    def name(self):
        return self._name
    
    @property
    def weight(self):
        return self._weight
    @property
    def closing_speed(self):
        return self._closing_speed
    
    @property
    def object_held(self):
        return self._object_held
    
    @object_held.setter
    def object_held(self, obj):
        self._object_held = obj
        
    
    def __str__(self):
        return self._name
        

    def activate_gripper(self):
        '''Set the status of the gripper to "enabled"
        '''
        self._enable = True
        print("activate gripper")

    def deactivate_gripper(self):
        '''Set the status of the gripper to "disabled"
        '''
        self._enable = False
        print("deactivate gripper")