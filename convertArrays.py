import numpy as np
arr = np.array([3,6,9,7,2,0,8,6,8,6,7,4])
print(arr)

newarr = arr.reshape(3,4)
print(newarr)

arr1 = np.array([1,2,3,4,6,7,8,9,1,2,3,4,5,6,7,8,6,7])
newarr1 = arr1.reshape(6, 3)
newarr11 =arr1.reshape(9,2)
print(newarr1)
print(newarr11)

#converttings arrays to 3D

my_arr = np.array([1,2,3,4,5,6,7,8,9,1,2,3])
my_newarr = my_arr.reshape([2,3,2])
my_newarr1 = my_arr.reshape([3,2,2])
print(my_newarr)
print(my_newarr1)