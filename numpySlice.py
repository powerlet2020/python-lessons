import numpy as np
a = np.array([1,3,4,6,4,6,7,6,7,4,9])
print(a[1:10])
print(a[1:10:2])

# slicing from a number to end of a list
b = np.array([2,3,5,7,9,9,9,5,7])
print(b[2:])

#  slicing from the begining some element
print(b[:5])
print(a[::])
print(a[::2])