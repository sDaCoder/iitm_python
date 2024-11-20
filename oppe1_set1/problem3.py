passage = '''
This is a test sentence where I wanted
to let you know that the sentences are 
multi-line and words are separated by spaces.
The first letters may be of different case but you
should consider it as lowercase and return the lowercase
letter as the result. Also check the other test cases
where you can easily count the most occuring first letter.
'''

def most_occuring_first_letter(passage: str):
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    letters = []
    for line in passage.strip().split("\n"):
        for word in line.strip().split(" "):
            letters.append(word[0].lower())
    
    freq = {}
    unique_char = set(letters)

    for char in unique_char:
        count: int = 0
        for letter in letters:
            if letter == char:
                count += 1
        freq[char] = count
    max_val = max(freq, key = freq.get)
    return max_val

print(most_occuring_first_letter(passage))
