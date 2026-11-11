word = "Python"
print(word[0]) 
print(word[-1])

phrase = "Hello, World!"
print(phrase[0:5])
print(phrase[7:])
print(phrase[:5])

message = "Welcome to Python"
print(len(message))

# Case conversion methods
s = "  Kodnest technologies 123  "
print("upper():", s.upper())           # '  KODNEST TECHNOLOGIES 123  '
print("lower():", s.lower())           # '  kodnest technologies 123  '
print("title():", s.title())           # '  Kodnest Technologies 123  '
print("capitalize():", s.capitalize()) # '  kodnest technologies 123  '
print("swapcase():", s.swapcase())     # '  kODNEST TECHNOLOGIES 123  '

# Whitespace removal (strip) methods
print("strip():", s.strip())           # Removes spaces from both ends: 'Kodnest technologies 123'
print("lstrip():", s.lstrip())         # Removes leading spaces: 'Kodnest technologies 123  '
print("rstrip():", s.rstrip())         # Removes trailing spaces: '  Kodnest technologies 123'

# Search and count methods
print("count('e'):", s.count("e"))     # 3 (counts occurrences of 'e')
print("find('tech'):", s.find("tech")) # Starting index of 'tech' (or -1 if not found)
print("startswith('  Kod'):", s.startswith("  Kod")) # True
print("endswith('123  '):", s.endswith("123  "))     # True

# Replace and split methods
print("replace():", s.replace("123", "Pvt Ltd")) # Replaces '123' with 'Pvt Ltd'
print("split():", s.split())                     # Splits into list of words: ['Kodnest', 'technologies', '123']

# String checking (Boolean) methods
clean_str = "Kodnest"
num_str = "12345"
print("isalpha():", clean_str.isalpha()) # True (only alphabetic letters)
print("isdigit():", num_str.isdigit())   # True (only numbers)
print("isalnum():", "Kodnest123".isalnum()) # True (alphanumeric, no spaces)
print("isspace():", "   ".isspace())     # True (only whitespace)
