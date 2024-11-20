# You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.

# The operations your application should support are as follows:


# Odd number checker: Check whether the input number is odd.
# Name: odd_num_check
# Inputs: number:int
# Output: "yes" if the number is odd, "no" otherwise.
def odd_num_check(number):
    if number % 2 == 0:
        return "no"
    else:
        return "yes"
    
# Perfect square checker: Check whether the input number is a perfect square.
# Name: perfect_square_check
# Inputs: number:int
# Output: "yes" if the number is a perfect square, "no" otherwise.
def perfect_square_check(number):
    if number ** 0.5 == int(number ** 0.5):
        return "yes"
    else:
        return "no"
    
# Vowel checker: Check if a string has a vowel in it.
# Name: vowel_check
# Inputs: text:str
# Output: "yes" if the string contains a vowel, "no" otherwise.
def vowel_check(text):
    if "A" in text or "E" in text or "I" in text or "O" in text or "U" in text:
        return "yes"
    elif "a" in text or "e" in text or "i" in text or "o" in text or "u" in text:
        return "yes"
    else:
        return "no"
print(vowel_check("xyz"))    
# Divisibility checker: Check if a number is divisible by 2 or 3.
# Name: divisibility_check
# Inputs: number:int
# Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
def divisibility_check(number):
    if number % 2 == 0 and number % 3 == 0:
        return "divisible by 2 and 3"
    elif number % 2 == 0:
        return "divisible by 2"
    elif number % 3 == 0:
        return "divisible by 3"
    else:
        return "not divisible by 2 and 3"
    
# Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
# Name: palindrominator
# Inputs: text:str
# Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
def palindrominator(text):
    return text + text[len(text) - 2::-1]
# Simple interest calculator with inputs with a higher interest rate if long term.
# Name: simple_interest
# Inputs: principal_amount:int, n_years:int (number of years)
# Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
def simple_interest(principal_amount, n_years):
    if n_years < 10:
        return round(principal_amount * 0.05 * n_years)
    else:
        return round(principal_amount * 0.08 * n_years)
# If the operation name is not any of the above print "Invalid Operation".


# op = input()
# if op == "odd_num_check":
#     print(odd_num_check(int(input())))
# elif op == "perfect_square_check":
#     print(perfect_square_check(int(input())))
# elif op == "vowel_check":
#     print(vowel_check(input()))
# elif op == "divisibility_check":
#     print(divisibility_check(int(input())))
# elif op == "palindrominator":
#     print(palindrominator(input()))
# elif op == "simple_interest":
#     print(simple_interest(int(input()), int(input())))
# else:
#     print("Invalid Operation")