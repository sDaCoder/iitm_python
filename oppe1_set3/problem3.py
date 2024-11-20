from collections import Counter

# def sorted_courses_dic(courses: dict):
#     sorted_courses = {}
#     max_enroll = dict
#     for key, value in courses.items():
#         if()

def courses_sorted_by_enrollment(student_courses: dict):
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Arguments:
    student_courses: dict - a dictionary where keys are 
        student roll numbers and values are lists of courses they chose

    Return:
    list - a list of courses sorted by the 
        number of students enrolled in descending order
    '''
    courses = []
    for key, value in student_courses.items():
        for course in value:
            courses.append(course)
    
    course_dic = dict(Counter(courses))
    return course_dic
    # return [key for key, _ in course_dic.items()]

student_courses1 = {
    '201': ['Biology', 'Chemistry'],
    '202': ['Chemistry', 'Biology'],
    '203': ['Physics', 'Chemistry'],
    '204': ['Biology', 'Physics'],
    '205': ['Chemistry']
}
print(courses_sorted_by_enrollment(student_courses1))