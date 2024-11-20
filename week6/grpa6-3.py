def is_num_sorted(num)->bool:
    '''
    Check if a number is sorted.
    sorted means the digits of a number are sorted in ascending order.
    Eg. 1468 - sorted , 4948 - not sorted.

    Argument: num: int
    Return: bool
    '''
    ...

def sorted_num_count(nums:list) -> int:
    '''
    Given a list of nums(int) find the count of sorted numbers in the list.

    Arguments: nums - list[int]
    Return: count - int
    '''
    ...

def common_substring(words:list)->str:
    '''
    Given a list of words check whether there is a word in words 
    that is a substring of all other words.
    If there is a word return that word else return None

    Hint: only the smallest word can be a substring of all other words.

    Arguments: words - list[str]
    Return: common_substr_word - str
    '''

    ...

def is_valid_phone_number(phone_no:int)->bool:
    '''
    Check if a number is valid for a specific operator.

    A phone number is valid if 
        - it has 10 digits
        - should begin with 98123
        - same digit should not occur more that 5 times.
    '''
    ...

def validate_phone_numbers(phone_nos:list)->dict:
    '''
    Given a list of phone numbers, create a dict with 
    phone numbers as keys and the string "VALID" or "INVALID"
    depending on the validity of the phone number as described by the above funtion.

    Arguments: phone_nos - list
    Return: validity_dict - dict[int,str]
    '''
    ...

def get_election_winner(votes:dict)->str:
    '''
    Given a dictionary with candidate name as key and number of votes as values,
    Find the winner of the election who has the maximum votes

    Arguments: votes - dict[str, int]
    Return: winner - str
    '''
    ...

def misspelt_words(vocab:str, sentence:str)->list:
    '''
    Given a comma separated string of vocabulary, 
    and a space separated string sentence,
    return a list of misspelt words in the order they occur in the sentence.

    The words which are not in the vocabulary are considered misspelt.

    Arguments: 
        vocab - str: comma separated string with vocabulary
        sentence - str: space separated string of sentence
    Return:
        misspelt_words - list
    '''
    ...

def count_sock_pairs(sock_colors:list)->int:
    '''
    Given a list of sock colors representing the color of each sock, 
    find the number of sock pair (both having same color) is there.
    Eg. ["red","blue","green","green","red","green","red","red","blue","black"] 
    2 red+ 1 green+ 1 blue = 5 pairs

    Arguments: sock_colors - list: of sock colors
    Return: number of pairs of sock - int
    '''
    ...

def is_vowely(word:str)->bool:
    '''
    Check if a given word is vowely. A word is vowely if 
    - it has all the vowels in it.
    - the vowels occur in ascending order.

    Assume no letter repeats in the given word.

    Eg. abecidofu - vowely, tripe - not vowely, eviaoqu - not vowely

    Argument: word - a string with no letter repeated
    Return: bool 

    Hint: if the non-vowels are removed from the word, it would be just aeiou
    '''
    ...

def vowely_count(words:list)->int:
    '''
    Given a list of words find the number of vowely words from the list.    

    Arguments: words :list[str]

    Return: int - number of vowely words
    '''
    ...

def format_name(first:str, middle:str, last:str)->str:
    '''
    Given three lower case parts of name, 
    return the full name with first letter capitalized in each part.

    Note that middle name can be empty.
    '''
    ...

def double_palindromes(n:int)->list:
    '''
    Given a number n, find all the positive integers till n (including)
    that are double_palindrome. A number is double palindrome if 
    it is a palindrome and its square is a palindrome.

    Eg. 
    8 - palindrome, not double palindrome
    11 - palindrome and double palindrome
    12 - not palindrome and not double palindrome

    Arguments: n - int: range of numbers to search
    Return: list of integers which are double palindrome in the ascending order
    '''

    ...

def scores_spx(kakashi_moves:list, guy_moves:list):
    '''
    Given the series of moves played by Kakashi and Guy in a Stone-Paper-Scissor game,
    find the scores of Kakashi and guy respectively.
    Rules - Stone beats Scissor, Scissor beats Paper and Paper beats Stone
    Score - Number of times won
    Symbols - Stone - S, Paper - P, Scissor - X

    Arguments: 
    kakashi_moves and guy_moves - list of moves where each move 
        is a string corresponding to the symbol

    Return: kakashi_score:int , guy_score:int
    '''
    ...

    return k_score, g_score
