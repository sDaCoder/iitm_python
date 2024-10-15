# Part 1 - while loop to for loop
# factorial - print factorial of a given non-negative integer n (Type: Accumulation)
# Input - n:int
# even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
# Input - n:int
# power_sequence - Print the sequence 1, 2, 4, 8, 16, ... n terms in same line in multiple lines, where n is taken from the input(Type: Mapping)
# Input - n:int
# Part 2 - for loop With range
# sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
# Input - n:int
# from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
# Input - n:int, k:int
# part 3 - for loop with iterables.
# string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
# Input - s:str
# list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
# Input - l:list


# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

    
if task == 'factorial':

    def fact(n: int) -> int:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    n = int(input())
    print(fact(n))

        
elif task == 'even_numbers':

    def printEven(n: int) -> None:
        for i in range(0, n+1, 2):
            print(i)

    n = int(input())
    printEven(n)

elif task == 'power_sequence':

    def powerSeq(n: int) -> None:
        num = 1
        for i in range(0, n):
            print(num * (2 ** i))

    n = int(input())
    powerSeq(n)

elif task == 'sum_not_divisible':

    def printNotDiv(n: int) -> int:
        sum = 0
        for i in range(1, n):
            if (i % 4 != 0) and (i % 5 != 0):
                sum += i
        return sum
        
    n = int(input())
    print(printNotDiv(n))

elif task == 'from_k':

    def printFromk(n: int, k: int) -> None:
        count = 0
        for i in range(k, -100, -1):
            if count == n:
                break
            if (i % 2 != 0) and ('5' not in str(i)) and ('9' not in str(i)): 
                count += 1
                print(int(str(i)[::-1]))

    n = int(input())
    k = int(input())
    printFromk(n, k)

elif task == 'string_iter':
    def stringIter(s: str) -> None:
        s = "1" + s
        for i in range(1, len(s)):
            print(int(s[i]) * int(s[i - 1]))

    s = input()
    stringIter(s)

elif task == 'list_iter':

    def listIter(l: list) -> None:
        for i in l:
            print(f"{i} - type: {type(i)}")

    lst = eval(input()) # this will load the list from input
    listIter(lst)

else:
    print("Invalid")
