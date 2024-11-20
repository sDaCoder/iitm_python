def get_student_details():
    '''
    Get the student details over multiple lines

    Input format:

    name
    age
    rollno

    Return: name:str, age:int, rollno:int
    '''
    name: str = input()
    age: int = int(input())
    rollno = int(input())

    return name, age, rollno

# heterogeneous - single line 
def get_student_details_same_line():
    '''
    Get the student details from the same line

    Input format:(separated by space)

    name age rollno

    Return: name:str, age:int, rollno:int
    '''
    ...
    details = input()
    name, age, rollno = details.split(" ")[0], int(details.split(" ")[1]), int(details.split(" ")[2])
    return name, age, rollno

# homogeneous - single line
def get_comma_separated_integers():
    '''
    Get a list of comma separated integers from input

    Return: numbers:list[int]
    '''
    input_str = input()
    
    numbers = []
    for num in input_str.split(","):
        numbers.append(int(num))
    return numbers

# homogeneous - multi-line - definite
def get_n_float_numbers():
    '''
    Get n float numbers with one number in each line 
    and the first line has n.

    Input Format:
    n
    num1
    num2
    ...
    numn

    Return: nums:list[float]
    '''
    ...
    n = int(input())
    i: int = 0
    nums: list[float] = []

    while(i < n):
        num = float(input())
        nums.append(num)
        i += 1

    return nums

# homogeneous - multi-line - indefinite
def get_nums_until_end():
    '''
    Get float numbers with one number in each line 
    until the input is "end"(case insensitive)

    Input Format:
    num1
    num2
    ...
    numx
    End

    Return: nums:list[float]
    '''
    
    nums = []
    num = input()
    if(num == 'End'):
        return nums
    else:
        nums.append(float(num))

    while(num != 'End'):
        num = input()
        nums.append(float(num))

    return nums

# hybrid - single line
def get_batsman_runs():
    '''
    Get batsman name, number and runs as a list

    Input format: (separated by space)
    name no run1 run2 run3 ...

    Return: name:str, no:int, runs:list[int]
    '''
    input_str = input()
    parts = input_str.split()

    name = parts[0]
    no = int(parts[1])
    runs = [int(run) for run in parts[2:]]

    return name, no, runs

# key value 
def get_course_scores():
    '''
    Get course name and scores of the over multiple lines where 
    course name and scores are separated by a hypen in each line.
    First line corresponds to the number or entries.

    Input format:
    2
    course1-score1
    course2-score2

    Return: dict[str,int] - with course name as key and score as value
    '''
    course_scores = {}
    num_entries = int(input())
    
    for i in range(num_entries):
        entry = input()
        course, score = entry.split('-')
        course_scores[course.strip()] = int(score.strip())
    
    return course_scores

# # dict with list as values
def get_all_batsman_runs():
    '''
    Given the batsman name and the comma separated runs 
    where both are seperted by a hypen in multiple lines, 
    create a dictionary with batsman name and list of runs as value.
    The number of lines is given in the first line

    Input format:
    3
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2

    Return: dict[str,list[int]] - with batsman name as key and list of runs as values
    '''
    batsman_runs = {}
    n = int(input())
    
    for _ in range(n):
        input_str = input()
        name, runs = input_str.split("-")
        batsman_runs[name.strip()] = [int(run) for run in runs.split(",")]
    
    return batsman_runs

# # csv - list of dicts
def get_student_marks():
    '''
    Given the student rollno, city, age,
    course1_marks, course2_marks and course3_marks 
    as comma separated values over multiple lines,
    create a list of dict with the above attributes as keys 
    and the corresponding value as values.
    The number of lines is given in the first line

    Input Format:
    n
    1,citya,23,86,69,86
    2,cityb,19,78,65,89
    ...
    n,cityx,35,89,57,76

    Return: 
    student_data - list[dict]: where each dict would be 

    {'rollno':int, 'city':str,'age':int, 
    'course1':int, 'course2':int, 'course3':int}
    '''
    ...

    student_data = []
    n = int(input())

    for _ in range(n):
        input_str = input()
        rollno, city, age, course1, course2, course3 = input_str.split(',')
        
        student_info = {
            'rollno': int(rollno.strip()),
            'city': city.strip(),
            'age': int(age.strip()),
            'course1': int(course1.strip()),
            'course2': int(course2.strip()),
            'course3': int(course3.strip())
        }
        
        student_data.append(student_info)
    
    return student_data

# # list of dicts
def get_student_data_over_multiple_lines():
    '''
    Given each attribute as described above in given over multiple lines 
    and multiple entries are given create a dictionary as described above.

    Input format:
    n
    1
    citya
    23
    86
    69
    86
    2
    cityb
    19
    78
    65
    89
    ...
    n
    cityx
    35
    89
    57
    76
    '''
    student_data = []
    n = int(input())

    for _ in range(n):
        rollno = int(input().strip())
        city = input().strip()
        age = int(input().strip())
        course1 = int(input().strip())
        course2 = int(input().strip())
        course3 = int(input().strip())

        student_info = {
            'rollno': rollno,
            'city': city,
            'age': age,
            'course1': course1,
            'course2': course2,
            'course3': course3
        }
        
        student_data.append(student_info)
    
    return student_data

# # this will read the function name from the input.
# func = eval(input()) 

# # this will read the actual output that is required which is the second line
# expected_output = eval(input())

# # The remaining of the input should be read by your function
# actual_output = func()

# if expected_output != actual_output:
#     print("Your output doesn't match the expected output.")
# print(actual_output)

print(get_batsman_runs())