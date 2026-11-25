# Python Negative Slicing - 25 Difficult

# Q1
a = "ABCDEFGHIJKLMN"
print(a[-2:-12:-2])  # MKIGE

# Q2
a = "PROGRAMMING"
print(a[1:-3])  # ROGRAMM

# Q3
a = "INTERVIEWPREPARATION"
print(a[-3:-18:-3])  # IREWV

# Q4
a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[-2:-9:-2])  # [80, 60, 40, 20]

# Q5
a = "abcdefghijklmnop"
print(a[-1:-15:-3])  # pmjgd

# Q6
a = "PythonProgramming"
print(a[-2:2:-3])  # nmgPh

# Q7
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-3:1:-3])  # [8, 5]

# Q8
a = "ABCDEFGHIJ"
print(a[-2:-10:-3])  # IFC

# Q9
a = "DataSciencePython"
print(a[1:-2][::-2])  # hyeniSt

# Q10
a = "abcdefghijk"
print(a[-2:1:-2])  # jhfd

# Q11
a = [5, 10, 15, 20, 25, 30, 35, 40]
print(a[-1:-8:-3])  # [40, 25, 10]

# Q12
a = "PYTHONDEVELOPER"
print(a[-4:-14:-2])  # OEENH

# Q13
a = "ABCDEFGHIJKLMNO"
print(a[-3:1:-4])  # MIE

# Q14
a = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(a[1:-2][1:5])  # [33, 44, 55, 66]

# Q15
a = "ProgrammingLanguage"
print(a[-1:-20:-2])  # eagagimroP

# Q16
a = "abcdefghij"
print(a[-2:-8:2])  # '' -> empty

# Q17
a = "COMPUTERSCIENCE"
print(a[-2:1:-3])  # CIRU

# Q18
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(a[-2:-12:-2][::-1])  # [3, 5, 7, 9, 11]

# Q19
a = "PYTHONPROGRAMMING"
print(a[-1:-10:-4])  # GMO

# Q20
a = "abcdefghijklmn"
print(a[-3:2:-2])  # ljhfd

# Q21
a = "ABCDEFGHIJKLMN"
print(a[1:-2][::-1])  # LKJIHGFEDCB

# Q22
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a[-2:0:-2])  # [70, 50, 30]

# Q23
a = "FullStackDevelopment"
print(a[-5:-20:-3])  # peDal

# Q24
a = "abcdefgh"
print(a[-100:-1:-1])  # '' -> empty

# Q25
a = "PYTHON"
print(a[-3:1:-2][-2:1:-1])  # '' -> empty
