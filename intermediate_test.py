def add_to_list(numbers):
    """
    Task:
    - Add the number 6 to the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.append(6)
    return numbers

numbers = [1, 2, 3]
add_to_list(numbers)


def remove_from_list(numbers):
    """
    Task:
    - Remove the number 3 from the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.remove(3)
    return numbers

numbers = [1, 2, 3, 4]
    
remove_from_list(numbers)


def insert_at_beginning(numbers):
    """
    Task:
    - Insert the number 0 at the beginning of the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.append(0)
    numbers.sort()
    return numbers

numbers = [1, 2, 3]

insert_at_beginning(numbers)


def reverse_list(numbers):
    """
    Task:
    - Reverse the order of elements in the list `numbers`.
    
    Return:
    - The reversed list.
    """
    return numbers[::-1]
numbers = [1, 2, 3]
reverse_list(numbers)


def create_new_tuple(t):
    """
    Task:
    - Create a new tuple that contains the first two elements of the tuple `t`.
    
    Return:
    - The new tuple with the first two elements.
    """
    new_tup = t[:2]
    return new_tup

t = (5, 10, 15, 20)
create_new_tuple(t)


def check_if_value_exists(t, value):
    """
    Task:
    - Check if the value 15 exists in the tuple `t`.
    
    Return:
    - True if the value exists, otherwise False.
    """
    for i in t:
        if i == value:
            return True
t =(5, 10, 15, 20)
value = 15
check_if_value_exists(t, value)

def find_intersection(set1, set2):
    """
    Task:
    - Find the intersection of sets `set1` and `set2`.
    
    Return:
    - The intersection of the two sets.
    """
    d = set1 & set2
    return d



def find_union(set1, set2):
    """
    Task:
    - Find the union of sets `set1` and `set2`.
    
    Return:
    - The union of the two sets.
    """
    c = set1 | set2
    return c



def find_difference(set1, set2):
    """
    Task:
    - Find the difference between set1 and set2 (i.e., set1 - set2).
    
    Return:
    - The difference between the two sets.
    """
    
    b = set1 - set2
    return b



def add_student(student_grades):
    """
    Task:
    - Add a new student 'David' with a grade of 92 to the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with the new student.
    """
#     student_grades = 
#     return student_grades
# student_grades = {}
# print(add_student(student_grades))


def change_bob_grade(student_grades):
    """
    Task:
    - Change Bob’s grade to 95 in the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Bob’s grade changed.
    """
    for k,v in student_grades.items():
        if k == 'Bob':
            v = 95
            #print(k,v)
            return student_grades

student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
#print(change_bob_grade(student_grades))

def delete_charlie(student_grades):
    """
    Task:
    - Delete 'Charlie' from the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Charlie removed.
    """
    # student_grades.delete('Charlie')
    # return student_grades

student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
delete_charlie(student_grades)

def retrieve_alice_grade(student_grades):
    """
    Task:
    - Retrieve the grade of Alice from the dictionary `student_grades`.
    
    Return:
    - Alice's grade.
    """
    grade = student_grades['Alice']
    return grade
student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
print(retrieve_alice_grade(student_grades))
