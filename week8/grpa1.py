from collections import Counter

def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    f = open(filename, 'r')
    words: list[str] = f.read().split("\n")
    freq: dict = dict(Counter(words))
    return freq

print(get_freq("public_1.txt"))