import numpy as np
list1 = [12.23, 13.32, 100, 36.32]
array1 = np.array(list1)
print("Original List:", list1)
print("One-dimensional NumPy array:", array1)

import numpy as np
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

import numpy as np
vector = np.zeros(10)
vector[6] = 11
print("Original vector:", vector)
print("Updated vector:", vector)

import numpy as np
array = np.arange(12,38)
print(array)

import numpy as np
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)
print("Data type before:", arr.dtype)
float_arr = arr.astype(float)
print("Converted to float:", float_arr)
print("Data type after:", float_arr.dtype)

import numpy as np
centigrade = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = centigrade * 9 / 5 + 32
print("Centigrade:", centigrade)
print("Fahrenheit:", fahrenheit)

import numpy as np
arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("Original array:", arr)
print("New arr:", new_arr)

import numpy as np
arr = np.random.rand(10)
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)
print("Array:", arr)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)

import numpy as np
array = np.random.rand(10,10)
min_val = array.min()
max_val = array.max()
print("Array:\n", array)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

import numpy as np
array = np.random.rand(3,3,3)
print(array)
