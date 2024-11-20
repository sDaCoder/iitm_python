def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where 
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''
    for string in strings:
        if '-' not in string:
            return False
        if string == "-":
            return False
        
        parts = string.split("-")
        if len(parts) != 2:
            return False
        if parts[0] != parts[1]:
            return False
    return True

strings = ["fast-slow", "slow-slow","high-high", "low-low"]
print(is_all_same_word_twice(strings))