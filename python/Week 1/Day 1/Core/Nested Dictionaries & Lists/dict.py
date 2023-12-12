# ---4--- # Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list. For example:
def printInfo(some_dict):
    for key in some_dict:
        result = " "
        for i in range(0, len(some_dict[key])):
            print(f"{key}, {some_dict[key][i]}")
    return


# f"we can inject {my_num} varibale here."

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
