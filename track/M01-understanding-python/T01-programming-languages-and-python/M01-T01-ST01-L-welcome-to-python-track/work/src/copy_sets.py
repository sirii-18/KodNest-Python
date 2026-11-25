import copy

# --- 1. Shallow Copy ---
original = [[1, 2], [3, 4]]
S_copy = copy.copy(original)

# Modifying a nested element
original[1][0] = 300
print("Original:    ", original)
print("Shallow copy:", S_copy)

# --- 2. Deep Copy ---
original = [[1, 2], [3, 4]]

# Creating a deep copy
D_copy = copy.deepcopy(original)

# Modifying a nested element in the original
original[1][0] = 300
print("Original:    ", original)
print("Deep copy:   ", D_copy)

# SETS IN PYTHON
# set{} unordered,unindexed,mutable(items are changeable but only add and remove can be performed)

fruits = {"apple", "mango", "banana", "kiwi"}
print("\n--- SETS IN PYTHON ---")
print("Initial set: ", fruits)

# 1. add() - adds a single element to the set
fruits.add("orange")
print(fruits)

# 2. update() - adds multiple elements from another iterable (list, tuple, or set)
fruits.update(["grapes", "watermelon"])
print( fruits)

# 3. Removing elements
# remove() - removes an element (raises KeyError if element is not found)
fruits.remove("apple")
print("After remove('apple'):", fruits)

# discard() - removes an element without error if it does not exist
fruits.discard("pineapple")  # Will not raise an error

# pop() - removes and returns an arbitrary element (sets are unordered)
popped_item = fruits.pop()
# clear() - removes all elements from the set
# fruits.clear()
# print(fruits)

# del - deletes the set object entirely
# del fruits

# 4. Immutable set: frozenset()
# frozenset cannot be modified (no add, remove, or update)
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print("\nFrozenset:   ", frozen_fruits, type(frozen_fruits))

"""
SET OPERATIONS:
# union() or | - returns a set containing all unique elements from both sets
# intersection() or & - returns a set containing elements common to both sets
# difference() or - - returns a set containing elements in the first set but not in the second set
# symmetric_difference() or ^ - returns a set containing elements in either set, but not both
# issubset() or <= - checks if one set is a subset of another (all elements of the first set are in the second set)
# issuperset() or >= - checks if one set is a superset of another (all elements of the second set are in the first set)
# isdisjoint() - returns True if the two sets have no elements in common
"""

# set - {}, unordered, unindexed,
# mutable (items are unchangeable but add or remove), no duplicates

fruits = {"apple", "banana", "kiwi", "apple"}
print(fruits, type(fruits))
# Output: {'apple', 'banana', 'kiwi'} - duplicate "apple" removed

# set constructor
stu_info = set(("Ram", 23, 89.65, "a"))
print(stu_info, type(stu_info), len(stu_info))

fruits2 = set(("apple", "banana", "kiwi"))
print(fruits2, type(fruits2))

# set methods
# add()
fruits = {"apple", "banana", "kiwi", "apple"}
nfruits = {"orange", "lemon", "grapes"}
fruits.update(nfruits)
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# discard()
fruits.discard("apple")
print(fruits)

# pop() - last element removed (actually random, since set is unordered)
fruits.pop()
print(fruits)

# clear()
fruits.clear()
print(fruits)  # set()

# del
del fruits
# print(fruits) -> Error, fruits deleted

fruits = {"apple", "banana", "kiwi"}
for i in fruits:
    print(i)

# Immutable frozenset
fruits = frozenset({"apple", "banana", "kiwi"})
print(fruits, type(fruits))
for i in fruits:
    print(i)

# fruits.add("orange")  # ERROR: frozenset is immutable, has no add() -> AttributeError
# print(fruits)

# union() - | operator also can be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.union(fruits2))
print(fruits | fruits2)

# intersection() - & operator also can be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.intersection(fruits2))
print(fruits & fruits2)

# difference() - - operator
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.difference(fruits2))
print(fruits2 - fruits)

# symmetric_difference() - ^ operator
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.symmetric_difference(fruits2))
print(fruits ^ fruits2)

# update() - adds all items from fruits2 to fruits
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
fruits.update(fruits2)
print(fruits)

# discard() - removes if present, no error if not present
fruits.discard("apple")
print(fruits)

# remove() - removes, but gives error if not present
fruits.remove("banana")
print(fruits)

# isdisjoint() - True if no common items
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.isdisjoint(fruits2))

# difference_update() - updates fruits with difference
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
fruits.difference_update(fruits2)
print(fruits)

# intersection_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
fruits.intersection_update(fruits2)
print(fruits)

# symmetric_difference_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
fruits.symmetric_difference_update(fruits2)
print(fruits)

# issubset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.issubset(fruits2))

#issuperset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}
print(fruits.issuperset(fruits2))

# frozenset() methods
#union
fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})
print(fruits.union(fruits2))

#intersection
fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})
print(fruits.intersection(fruits2))


#Dictionaries - {key:value} - key value pairs
#key is immutable but values are mutable
#values can be aything - duplicates are allowed only for values

dict1 = {"name":"Maha","age": 23,"city":"costa rica"}
print(dict1)

#overwriting or update
dict1["name"] = "Doe"
print(dict1)

#to list only keys
print(dict1.keys())

#to list only values
print(dict1.values())

#to list both key and value
print(dict1.items())

#assigning multiple valuesnto keys
dict1 = {"name":"Maha","age": 23,"city":["costa rica","usa","georgia"]}
print(dict1)
print(type(dict1),dict1["name"],dict["city"])
#to print a specific city
print(dict1["city"][1])

#constructor
#stu_info = dict()  representation of constructor in dictionary

stu_info = dict(name = "Ram", age = 30, city = "U")
#to add a key value 
stu_info["salary"] = 50000

#updating the salary - 2 ways
stu_info["salary"] = 30000
stu_info.update({"salary": 20000})

#deleting an item
stu_info.pop("age")
stu_info.popitem() # removes last added key value/item
del stu_info["city"]

#to delete the entire dictionary
stu_info.clear()

del stu_info
# print(stu_info)

# loop dicts
dict1 = {
    "name": "John",
    "age": 30,
    "city": ["New York", "USA", "Germany"]
}


#to get the keys only
for i in dict1.keys():
    print(i)

#to get the values only
for i in dict1.values():
    print(i)

# Dict Methods
print(dict1.get("name"))
print(dict1.get("salary",0))

#fromkeys
print(dict1.fromkeys(["name","age","city"]))

#setdefault
print(dict1.setdefault("name","john"))

#copy
dict2 = dict1.copy()
print(dict2)