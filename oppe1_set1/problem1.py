def abs_diff_between_sum_and_sum_of_squares(a:int, b:int) -> int:
    '''
    Given two integers, find the absolute difference between 
    their sum and the sum of their squares.
    Eg. 
    a, b = 2,3 
    sum is 5
    sum of squares is 13 
    absolute difference is 8

    Args:
        a - int : The first integer.
        b - int : The second integer.

    Returns:
        int: absolute difference between the sum and the sum of squares
    '''
    sum_num: int = a + b
    sum_square: int = a*a + b*b
    result: int = sum_num - sum_square
    return result if result > 0 else -result

def swap_except_middle_three(s: str) -> str:
    '''
    Given an odd-length string, 
    swap the parts before and after the middle three characters,
    while keeping the middle three characters in place.

    Assume the string has at least 5 characters.

    Examples:
        "firstabclast1" -> "last1abcfirst"
        "abcdefghi" -> "ghidefabc"

    Args:
        s (str): The input string of odd length.

    Returns:
        str: The modified string with the parts swapped.
    '''
    start: int = int(len(s) / 2) - 1
    end: int = int(len(s) / 2) + 1

    return f"{s[end+1:]}{s[start:end+1]}{s[0:start]}"

# print(swap_except_middle_three("abcdefghi"))

def interleave_lists(list1, list2, list3):
    '''
    Given three lists of same length, 
    interleave them together and return the interleaved list.

    Example:
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [(1,1),(2,2),(3,3)]
        output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A list containing interleaved elements from all three lists.
    '''
    result: list = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result

# print(interleave_lists([1, 2, 3], ['a', 'b', 'c'], [(1,1),(2,2),(3,3)]))

def has_more_than_5_unique_digits(num: int) -> bool:
    '''
    Determine if a given integer has more than 5 unique digits.

    Args:
        num (int): The input integer.

    Returns:
        bool: True if the integer has more than 5 unique digits, otherwise False.
    '''
    check_set = set(str(num))
    return len(check_set) > 5

print(has_more_than_5_unique_digits(11223344445))
# 1 2 2 3 4

def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the the final position of the point after a given time. 

    Hint: final position = intial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: time of movement.

    Returns:
        tuple[int]: A tuple representing the displacement (dx, dy).
    '''
    def add_payload(s0, v0) -> int:
        return s0 + v0 * time
    
    return tuple(map(add_payload, pos, vel))

# print(final_position((1,1), (2,2), 3))

def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    The function modifies the dictionary in place and does not return anything.

    Note: 
        Modifying a dict while iterating over it will give an error in python. 
        So, make a copy of the dict keys and then iterate over it.

    Args:
        d (dict): The dictionary to modify.
        l (list): The list of keys to keep in the dictionary.

    Returns:
        None
    '''
    keys: list = []
    for key, _ in d.items():
        keys.append(key)

    for k in keys:
        if k not in l:
            del d[k]

# d = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# l = [7,6,5,4,3]
# remove_keys_not_in_list(d, l)
# print(d)