import sys
sys.path.append('./')
# sys.path.insert(1,'/home/chaosmachete/Documents/python projects/rwa2/')

from utils.utils import current_state
from gripper.gripper import Gripper
from robot.linear_robot import LinearRobot
from robot.gantry_robot import GantryRobot

# separator to print between prompts
separator = '\n' + '='*100
    
# ---------------------- generate plan --------------------------------
def generate_plan():
    
    # generates and executes the plan given environment state and goal state
   
    print(separator)
    set_initial()
    print('\n\n', separator)
    print('\nTHE SOLUTION IS:')
    print(separator, '\n')
    
    # instantiate gantry gripper and robot
    gantry_gripper = Gripper('gantry_gripper')
    gantry_robot = GantryRobot()

    # attach the gripper to gantry robot
    gantry_robot._gripper = gantry_gripper
    gantry_robot.plan()

    # instantiate gantry gripper and robot
    linear_gripper = Gripper('linear_gripper')
    linear_robot = LinearRobot()

    # attach the gripper to gantry robot
    linear_robot._gripper = linear_gripper
    linear_robot.plan()

    

def set_initial():
    
    # sets the initial environment state from user input
    
    avail_bins = [1, 2, 3, 4]
    parts = []

    # for each part type
    for part in current_state['parts']:
        # get no. of parts of this type  
        count = int(input(f'\nHow many {part}s in the workcell [0, 4, 9]? '))
        if count == 0 or (count >= 4 and count <= 9):
           pass
        else :  
            print('invalid parts entered')
            return
        # if the part count is zero, continue to next part type 
        if count == 0: continue
        parts.append(part)
        # get available bins from current state
        
        # get the bin in which the parts are
        bin_no = int(input(f'\nIn which bin are {part}s located {avail_bins}? '))
        if bin_no not in avail_bins:
            print('invalid bin entered')
            return
        # update the world state according to the input
        bin = 'bin' + str(bin_no)
        bin_ob = current_state['bins'][bin]
        bin_ob['part_type'] = part
        bin_ob['part_quantity'] = count
        # remove the bin from available bins
        avail_bins.remove(bin_no)
        
    
    kit_obj = current_state['kit']

    # get the tray to be used for knitting
    inp = input('\nWhich tray to use [(y)ellow, (g)ray]? ')
    tray = 'yellow_tray' if inp == 'y' else 'gray_tray'
    if inp == 'y' or  inp == 'g':
        pass
    else: 
        print("select trays yellow or gray") 
    
    kit_obj['tray'] = tray
    
    print(separator)


    # get the agv to be used for knitting
    agv_no = int(input('\nWhich AGV to use [1, 2, 3, 4]? '))
    if agv_no in [1,2,3,4]:
         True
    else:
        print("invalid parts entered")
        return
    
    agv = 'agv' + str(agv_no)
    agv_obj = current_state['agvs'][agv]
    kit_obj['agv'] = agv
    
    # get the assembly station to be used for knitting
    reachable = [int(st[-1]) for st in agv_obj['possible_destination']]
    as_no = int(input(f'\nWhich assembly station to ship {reachable}? '))
    if as_no not in reachable:
            print('invalid as_no entered')
            return
    agv_obj['destination'] = 'as' + str(as_no)
    
    print(separator)
    expected_parts = current_state['trays'][tray]['expected_parts']
    # get the part mix to be placed on the tray
    for part in parts:
        part_count = int(input(f'\nHow many {part}s in tray [0, 1, 2]? '))
        if part_count in [0,1,2]:
         True
        else: print("invalid parts entered")
        expected_parts += [part]*part_count
            

generate_plan()