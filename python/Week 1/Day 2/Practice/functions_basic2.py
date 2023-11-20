#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    return list(range(num, -1, -1))
print(countdown(5))  

def print_and_return(lst):
    print(lst[0])
    return lst[1]

# Example
result = print_and_return([1, 2])
print("Returned:", result)  # Output: 1, Returned: 2

def first_plus_length(lst):
    return lst[0] + len(lst)

# Example
result = first_plus_length([1, 2, 3, 4, 5])
print(result)  # Output: 6
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False

    second_value = lst[1]
    new_list = [value for value in lst if value > second_value]

    print(len(new_list))
    return new_list

# Examples
result1 = values_greater_than_second([5, 2, 3, 2, 1, 4])  # Output: 3, Returned: [5, 3, 4]
result2 = values_greater_than_second([3])  # Output: False
def length_and_value(size, value):
    return [value] * size

# Examples
result1 = length_and_value(4, 7)  # Output: [7, 7, 7, 7]
result2 = length_and_value(6, 2)  # Output: [2, 2, 2, 2, 2, 2]

