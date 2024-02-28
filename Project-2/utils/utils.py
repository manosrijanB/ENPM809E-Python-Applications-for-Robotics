from pprint import pprint
from typing import List, Any

current_state = {
    'parts': ['red_part', 'green_part', 'blue_part'],
    'agvs': {
        "agv1": {
            "possible_destination": ["as1", "as2"],
            "destination": None
        },
        "agv2": {
            "possible_destination": ["as1", "as2"],
            "destination": None
        },
        "agv3": {
            "possible_destination": ["as3", "as4"],
            "destination": None
        },
        "agv4": {
            "possible_destination": ["as3", "as4"],
            "destination": None
        },
    },
    'trays': {
        'yellow_tray': {
            'location': 'table',
            'expected_parts': [],
            'current_parts': []
        },
        'gray_tray': {
            'location': 'table',
            'expected_parts': [],
            'current_parts': []
        }
    },
    'bins': {
        'bin1': {
            'part_type': None,
            'part_quantity': 0
        },
        'bin2': {
            'part_type': None,
            'part_quantity': 0
        },
        'bin3': {
            'part_type': None,
            'part_quantity': 0
        },
        'bin4': {
            'part_type': None,
            'part_quantity': 0
        },
    },
    'kit': {
        'tray': None,
        'complete': False,
        'agv': None
    }
}


def get_input(prompt: str, valid_lst: List[Any]):
    """
    get valid input from the user

    Args:
        prompt (str): prompt to display
        prefix (Any): prefix to be added to the user input
        valid_ls (List[Any]): a list of valid options to be entered by the user

    Returns:
        Any: validated user input added with the prefix 
    """
    # get the type of input
    data_type = type(valid_lst[0])
    # prompt until user input is valid
    inp = data_type(input(prompt))
    while inp not in valid_lst:
        inp = data_type(input('Please enter valid value: '))
    # add prefix to the user input and return
    return inp


def main():
    pprint(current_state)


if __name__ == '__main__':
    main()
