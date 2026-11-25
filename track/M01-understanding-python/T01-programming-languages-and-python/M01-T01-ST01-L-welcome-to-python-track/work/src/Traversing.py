# Traversing NESTED LIST, LIST INSIDE DICTIONARIES, NESTED DICTIONARIES

# 1. NESTED LIST
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# 2. LIST INSIDE DICTIONARY
students = {
    "Ram": ["Python", "SQL"],
    "Sita": ["Java", "AWS"]
}
for name, skills in students.items():
    print(name, ":", skills)

# 3. NESTED DICTIONARY
employees = {
    101: {"name": "Ram", "salary": 65000},
    102: {"name": "Sita", "salary": 70000}
}
for emp_id, info in employees.items():
    print(emp_id, info["name"], info["salary"])


# -----------------------------------------------
# NESTED COLLECTIONS AND COUNTER
# -----------------------------------------------

trainer = {"divya","gamana","salman","gamana","salman","gamana"}
trainer_count = { }
for t in trainer:
    if t in trainer_count:
        trainer_count[t] += 1
    else:
        trainer_count[t] = 1

print(trainer_count)

trainer = ["divya","gamana","salman","gamana","salman","gamana"]   
trainer_count = { }

for i in trainer:
    if i in trainer_count:
        trainer_count[i] += 1
    else:
        trainer_count[i] = 1

print(trainer_count)

from collections import Counter
trainer_count = Counter(trainer)
print(trainer_count)