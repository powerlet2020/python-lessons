import numpy as np
arr = np.array([2,3,5,6,8,9])
x = arr.copy()
arr[0] = 24
print(arr)
print(x)

# The copy SHOULD NOT be affected by the changes made to the original array.

#   VIEW VIEW VIEW
arr1 = np.array([1,5,5,6,7,8])
y = arr1.view()
arr1[0] = 45
print(arr1)
print(y)
# The view SHOULD be affected by the changes made to the original array.

#  make changes in VIEW
l = np.array([3,8,9,6,2])
z = l.view()
z[0] = 50
print(l)
print(z)

# The original array SHOULD be affected by the changes made to the view.