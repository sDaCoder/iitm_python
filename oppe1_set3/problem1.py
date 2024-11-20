def square_and_clip(x: int, threshold:int) -> int:
    '''
    Square the given integer and clip the result to threshold
    (clipping means if the value x goes greater than the threshold, keep it at threshold).

    Arguments:
    x: int - the input number
    threshold: int - the threshold value

    Return:
    int - squared and clipped result
    '''
    return x*x if x*x <= threshold else threshold

# print(square_and_clip(5, 25))

def lowercase_first_half_and_uppercase_second_half(s: str) -> str:
    '''
    Given an even-length string of any case, create a string with the first half 
    in lowercase and the second half in uppercase.

    Arguments:
    s: str - the input string

    Return:
    str - the modified string
    '''
    return_str = ""
    for i in range(len(s)):
        if len(s) % 2 == 0:
            if i < int(len(s) / 2):
                return_str += s[i].lower()
            else:
                return_str += s[i].upper()
        else:
            if i <= int(len(s) / 2):
                return_str += s[i].lower()
            else:
                return_str += s[i].upper()

    return return_str

# print(lowercase_first_half_and_uppercase_second_half("HELLOworld"))

def add_the_middle_element_to_both_ends(l: list) -> None:
    '''
    Given an odd-length list, insert the middle element to both ends of the list.
    Modify the input list and do not return a new list.

    Arguments:
    l: list - the input list

    Return:
    None - the input list is modified inside the function.
    '''
    mid: int = int(len(l) / 2)
    element = l[mid]
    l.insert(0, element)
    l.append(element)

# l = [7, 8, 9, 10, 11]
# add_the_middle_element_to_both_ends(l)
# print(l)

def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    '''
    S1 = set(list(str(n1)))
    S2 = set(list(str(n2)))
    S = S1.intersection(S2)
    return len(S)

# print(number_of_unique_common_digits(12345, 54321))

def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Given three points a, b, and c on the Cartesian plane, 
    calculate the Manhattan distance to go from point a to point c via point b.

    Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.

    Args:
        a (tuple): Coordinates of point a as (x1, y1).
        b (tuple): Coordinates of point b as (x2, y2).
        c (tuple): Coordinates of point c as (x3, y3).

    Returns:
        int: The Manhattan distance from point a to point c via point b.
    '''
    d1: int = abs(b[0] - a[0]) + abs(b[1] - a[1])
    d2: int = abs(c[0] - b[0]) + abs(c[1] - b[1])
    return d1 + d2

# a = (-1, -1)
# b = (1, 1)
# c = (2, 2)
# print(manhattan_distance_via_b(a, b, c))

def create_indexed_dict(names: list) -> dict:
    '''
    Given a list of names, create a dictionary with the indices as keys and the names as values.

    Args:
        names (list): A list of names.

    Returns:
        dict: A dictionary with indices as keys and names as values.
    '''
    return {i: names[i] for i in range(len(names))}

# names1 = ["Alice", "Bob", "Charlie", "David"]
# print(create_indexed_dict(names1))
