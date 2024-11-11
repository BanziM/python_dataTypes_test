def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    list = []
    for i in range(1,21):
        
        if i % 2 == 0:
            print(i)
            list.append(i*i)

    return list[:5]
create_squares_of_evens()


def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
#     dict = {}
#     for i in students:
#         for x in i:
#             print(x)


# students = [('x',10), ('y',9), ('z',8), ('m',10)]
# convert_to_dict(students)


def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    val =nested['c']['x']
    return val

nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
access_value_x(nested)

def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    nested['a'].append(6)
    return nested
nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
append_to_list_in_dict(nested)

def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    return nested['b']
nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
print(convert_tuple_to_list_and_append(nested))
