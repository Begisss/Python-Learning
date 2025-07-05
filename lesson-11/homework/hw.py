def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
print(add(12, 3))        
print(divide(10, 2))     

def reverse_string(s):
    """Return the reversed string."""
    return s[::-1]

def count_vowels(s):
    """Return the number of vowels in the string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(reverse_string("hello"))      
print(count_vowels("OpenAI ChaaaaaaaaatGPT")) 

import math
def area_of_circle(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2
def circumference_of_circle(radius):
    """Return the circumference of a circle given its radius."""
    return 2 * math.pi * radius
print(area_of_circle(5))          
print(circumference_of_circle(5))  

# file_operations/file_reader.py

def read_file(file_path):
    """Read and return the contents of the given file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File not found at '{file_path}'"
    except Exception as e:
        return f"Error reading file: {e}"

# file_operations/file_writer.py

def write_file(file_path, content):
    """Write the given content to the specified file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")
write_file("sample.txt", "Hello, world!")
text = read_file("sample.txt")
print(text)
