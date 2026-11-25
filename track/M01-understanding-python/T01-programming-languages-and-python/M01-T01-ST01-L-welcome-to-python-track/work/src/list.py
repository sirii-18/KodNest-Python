# SQUARE numbers

nums = [1,2,3,4]
#WAP to find square
sq_nums = []
for i in nums:
    sq_nums.append(i*i)
print(sq_nums)
#output [1,4,9,16]

# newlist = [expression for item in iterable condition]
sq_nums = [i*i for i in nums]
print(sq_nums)

# EVEN ODD UPPER LENGTH

even = [i for i in nums if i % 2 == 0]
print(even)  # [2, 4]
odd = [i for i in range(1, 10) if i % 2 != 0]
print(odd)   # [1, 3, 5, 7, 9]
names = ["Ram", "Sita", "Lakshmana", "Ravana"]
upper_lst = [n.upper() for n in names]
print(upper_lst)  # ['RAM', 'SITA', 'LAKSHMANA', 'RAVANA']
len_lst = [len(n) for n in names]
print(len_lst)    # [3, 4, 9, 6]

# EVEN ODD

numbers = [1,2,3,4,5,6]
# SYNTAX: new_list = [value_if_true if condition else value_if_false for item in iterable]
result = ["even" if n%2==0 else "odd" for n in numbers]
print(result)

num = [1, 7, 3, 8, 2]
gt_num = [n for n in num if n > 5]
print(gt_num)  # [7, 8]

word = "python"
lst = [ch for ch in word]
print(lst)     # ['p', 'y', 't', 'h', 'o', 'n']

# O/P [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]
res = [(i, j) for i in range(1, 3) for j in range(1, 4)]
print(res)

# MATRIX Flattening
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(flat)    # [1, 2, 3, 4, 5, 6]
