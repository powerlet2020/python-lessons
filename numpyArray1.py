import numpy as np
a = np.array([1,2,3,4,5])
print(a, type(a))
b = np.array([[1,2,3,4,5,],[6,7,8,9,4]])
print(b, type(b))

# checking the shape of arrays
print(a.shape)
print(b.shape)

#  checking the dimension of arrays
print(a.ndim)
print(b.ndim)

#  one can determine dimisnsion of array
c = np.array([1,3,2], ndmin=4)
print(c, c.ndim)

#  getting elements from an array using index
#  i want to access the number 7 which has an index of 2
arr =np.array([1,4,7,6,8])
print(arr[2])

# accsessing two dimensinal arrays
arr1 = np.array([[1,2,4,5,8],[5,6,7,3,8]])
print(arr1)
print(arr1[0, 1])
print(arr1[1, 2])
print(arr1[0, 4])
print(arr1[1, 4])

#  accessing three dimensinal arrays
arr2 = np.array([[[1,3,4,5],[5,5,7,8],[1,8,9,6]]])
print(arr2)
print(arr2.ndim)