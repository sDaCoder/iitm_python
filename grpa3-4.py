# factors - Find the factors of a number n (including 1 and itself) in ascending order.
# find_min - Take n numbers from the input and print the minimum number.
# prime_check - Check whether a given number is prime or not.
# is_sorted - Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
# any_true - Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.
# manhattan - Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.

any = None 
all = None  
min = None 

task = input()

def factors(n: int) -> None:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

def find_min(n: int) -> int:
    mini = int(input())
    for i in range(1, n):
        num = int(input())
        if num < mini:
            mini = num
    return mini

def prime_check(n: int) -> bool:
    isPrime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime

def is_sorted(s: str) -> bool:
    isSorted = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            isSorted = False
    return isSorted

def any_true(n: int) -> bool:
    isDiv = False
    for i in range(n):
        num = int(input())
        if num % 3 == 0:
            isDiv = True
    return isDiv

def calc_manhattan() -> int:
    x, y = 0, 0
    while True:
        dir = input()
        if dir == 'STOP':
            break
        if dir == 'UP':
            y += 1
        elif dir == 'DOWN':
            y -= 1
        elif dir == 'LEFT':
            x -= 1
        elif dir == 'RIGHT':
            x += 1
    return abs(x) + abs(y)

if task == 'factors':
    n = int(input())
    factors(n)

elif task == 'find_min':
    n = int(input())
    print(find_min(n))

elif task == 'prime_check':
    n = int(input())
    print(prime_check(n))

elif task == 'is_sorted':
    s = input()
    print(is_sorted(s))

elif task == 'any_true':
    n = int(input())
    print(any_true(n))

elif task == 'manhattan':
    print(calc_manhattan())

else:
    pass