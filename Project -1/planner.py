def pickup_tray(robot: str, tray: str, table: str):
     # robot`picks up `tray`from `table`
# Note: This function can only be executed if `robot`is 'ceiling_robot'
# Preconditions:
# - `robot`is 'robot_ceiling'
# - `tray`is located on `table`
# - `robot`'s gripper is empty
# Effects:
# - `robot`'s gripper is not empty
# - `robot`'s gripper is holding the tray
# - location of `tray`is not on `table`
# - location of `tray`is in `robot`'s gripper
# Args:
# robot (str): The robot used to perform this action
# tray (str): The tray to pick up ('yellow_tray or 'gray_tray')
# table (str): Table where the tray is located
# ('yellow_tray_table'or 'gray_tray_table')
     print(f'pickup_tray({robot}, {tray}, {table})')
     
def pickup_part(robot: str, bin: str, part: str):
#     `robot`picks up `part`from `bin`.
# Preconditions:
# - `robot`'s gripper is empty
# - `bin`has parts of type `part`
# - The number of parts in `bin`is > 0
# Effects:
# - Decrease the number of parts in `bin`by 1
# Args:
# robot (str): Robot used to perform this action
# ('robot_ceiling'or 'robot_floor')
# bin (str): Bin from which a part is removed ('bin1', ..., or 'bin4')
# part (str): The part to pick up
# ('red_part', 'green_part', or 'blue_part')
    
   
      print(f'pickup_part({robot}, bin{bin}, {part})')

def ship_agv(agv: str, tray: str, station: str):
    
#     Ship `agv`to assembly station `station`if `tray`is complete
# Preconditions:
# - `tray`is complete (it has all the parts needed)
# - `tray`is on `agv`
# Effects:
# - `agv`location is `station`
# Args:
# agv (str): AGV to ship
# ('agv1', 'agv2', 'agv3', or 'agv4')
# tray (str): Tray located on `agv`
# ('yellow_tray'or 'gray_tray')
# station (str): Assembly station where to ship `agv`
# ('as1', 'as2', 'as3', or 'as4')
    
    
    print(f'ship_agv(agv{agv}, {tray}, as{station})')
    
def place_part(robot: str, tray: str, part: str, agv: str):
#     `robot`places `part`in `tray`, which is located on `agv`
# Preconditions:
# - `robot`'s gripper is holding `part`
# - location of `tray`is `agv`
# - `tray`is not complete
# Effects:
# - `tray`has `part`
# - `robot`'s gripper is not holding `part`
# Args:
# robot (str): Robot used to perform this action
# ('robot_ceiling'or 'robot_floor')
# tray (str): Tray in which `part`is placed
# ('yellow_tray'or 'gray_tray')
# part (str): The part to place
# ('red_part', 'green_part', or 'blue_part')
# agv (str): AGV where `tray`is located.
    
    print(f'place_part({robot}, {tray}, agv{agv})')

def place_tray(robot: str, tray: str, agv: str): 
#     # """
# `robot`places `tray`on `agv`.
# Note: This function can only be executed if `robot`is 'robot_ceiling'.
# Preconditions:
# - `robot`is 'robot_ceiling'
# - `robot`'s gripper is holding `tray`
# - `tray`is located in `robot`'s gripper
# - location of `tray`is in `robot`'s gripper
# Effects:
# - `robot`'s gripper is empty
# - `robot`'s gripper is not holding `tray`
# - location of `tray`is not in `robot`'s gripper
# - location of `tray`is `agv`
# Args:
# robot (str): The robot used to perform this action
# tray (str): The tray to place on `agv`('yellow_tray'or 'gray_tray')
# agv (str): AGV where `tray`is placed
# ('agv1', 'agv2', 'agv3', or 'agv4')
    
    
    print(f'place_tray({robot}, {tray}, agv{agv})'  ) 

# creating a tray dictionary
def generate_path():
    tray ={'yellow': 'yellow_tray', "gray" : "gray_tray"}
    # new variable for input of tray
    tray_inp = str(input('which tray to use yellow or gray?'))
    if tray_inp == 'yellow':
        table= ()
        table = tray["yellow"]
    else: table = tray["gray"]
    print(table)

        
    # created a dictionary for the variables

    bindict = {'bin1': 1, 'bin2': 2, 'bin3': 3, 'bin4': 4}
    parts= {'red' : 1, 'green': 2,  'blue': 3}
    agv = {'agv1':1, 'agv2': 2,  'agv3': 3, 'agv4': 4}
    as_st ={'as1': 1, 'as2' : 2, 'as3': 3, 'as4': 4}
    robot = {1:'robot_floor', 2:'robot_ceiling'}
            
            

    # coloured parts
    red = int(input ('How many red_parts in the workcell?'))
    if red == 0 or (red >= 4 and red <= 9):
        True
    else :  print('invalid parts entered')


    blue = int(input ('How many blue_parts in the workcell?'))
    if blue == 0 or (blue >= 4 and blue <= 9):
        True
    else :  print('invalid parts entered')

    green = int(input ('How many green_parts in the workcell?'))
    if green == 0 or (green >= 4 and green <= 9):
        True
    else :  print('invalid parts entered')   


    # bins 
    abin = [1, 2 , 3, 4]

    # creating a logic for storing of bins
    red_bin = int(input('In which bin red part should be placed?'))

    bin = red_bin
    while bin not in abin :
            print("Choose any bin between 1 to 4 ")
            bin = int(input())   
    print('you chose bin '+ str(bin) +' for red part' )
    abin.remove(bin)
    bindict['red_bin'] = bin
        

    blue_bin = int(input('In which bin blue part should be placed?'))

    bin = blue_bin
    while bin not in abin :
            print("Choose any bin between 1 to 4 ")
            bin = int(input())   
    print('you chose bin '+ str(bin) +' for blue part' )
    abin.remove(bin)
    bindict['blue_bin'] = bin



    green_bin = int(input('In which bin green part should be placed?'))

    bin = green_bin
    while bin not in abin :
            print("Choose any bin between 1 to 4 ")
            bin = int(input())   
    print('you chose bin '+ str(bin) +' for green part' )
    abin.remove(bin)
    bindict['green_bin'] = bin


    #  logic for agv and assembly station

    agv_use = int(input('which agv to use?'))
    if agv_use > 4:
        print('invaild, enter from 1 to 4')
    if agv_use in [1, 2]:
        agv_use = agv['agv1'] or agv['agv2']
        as_use = as_st['as1'] or as_st['as2']
    if agv_use in [3,4]:
        agv_use = agv['agv3'] or agv['agv4']
        as_use= as_st['as3'] or as_st['as4'] 



    #  calling the functions from actions folder to be used over here
    print()
    pickup_tray('robot_ceiling', tray_inp, table )
    place_tray('robot_ceiling', tray_inp, agv_use  )
    if red_bin in range(1,3):
        # print(red_bin)
        pickup_part(robot[1], red_bin, 'red part')
        place_part(robot[1],tray_inp, 'red part', agv_use)
        ship_agv(agv_use, tray_inp, as_use)   
        

    if red_bin in range(3, 5):
        pickup_part(robot[2], red_bin, 'red part')
        place_part(robot[2],tray_inp,'red part', agv_use)
            

    if blue_bin in range(1,3):
        pickup_part(robot[1], blue_bin, 'blue part')
        place_part(robot[1],tray_inp,'blue part', agv_use)
        

    if blue_bin in range(3, 5):
        pickup_part(robot[2], blue_bin,'blue part')
        place_part(robot[2],tray_inp, 'blue part', agv_use)
        
    
    if green_bin in range(1,3):
        pickup_part(robot[1], green_bin,'green part')
        place_part(robot[1],tray_inp, 'green part', agv_use)
    

    if green_bin in range(3, 5):
        pickup_part(robot[2], green_bin, 'green part')
        place_part(robot[2],tray_inp, 'green part', agv_use)
    ship_agv(agv_use, tray_inp, as_use)    
    

        








    # robot = input()
    # robot_ceiling = str('robot_ceiling')
    # robot_floor = str('robot_floor')

    
    # # tray = input('which tray to use yellow or gray?')
    # # tray = "yellow"
    # #     tray = 'yellow'
    # #     else
        




    # bin1 = str(input('which color part to be placed in bin1 from colors green, red and blue ?'))

    # if bin1 == 0 or (str(red) or str(green) or str(blue)): 
        
