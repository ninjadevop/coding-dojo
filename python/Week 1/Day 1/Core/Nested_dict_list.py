x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]['y'] = 30

# Print the modified data
print("Modified x:", x)
print("Modified students:", students)
print("Modified sports_directory:", sports_directory)
print("Modified z:", z)

#2-Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} : {value}")

#3-Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
        else:
            print(f"The key '{key_name}' is not present in one of the dictionaries.")
#4-Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{key} - {len(values)} items")
        for value in values:
            print(value)
        print()  