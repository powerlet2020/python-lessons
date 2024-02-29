mylist = ['hamza', 'power','nasara','goal']
print(mylist)

a = mylist[0]
print(a)
print(mylist[0])

#  The list is changeable, meaning that we can change,
#  add, and remove items in a list after it has been created.

#  ALLOW DUPLICATES
# Since lists are indexed, lists can have items with the same value:
fruits = ['mango','mango','orange','banana']
print(fruits)
print(fruits[0],fruits[1])

#  list length
print(len(mylist))
print(len(fruits))

#  list can be any data type

mix_list = [1, 4 , True, False, 'hamza']
print(mix_list)
print(type(mylist))
print(type(mix_list[1]))

#   THE LIST CONSTRUCTOR LIST()
thislist = list((2,'hamza',True,5,6))
print(thislist)

#  slicing list
#  slicing means accessing items of a list using range of index

names = ['koko', 'hamza','shani','sara','hakim','nsara','hiday']
print(names[1:4])
print(names[:5])
print(names[1:])
print(names[::])
print(names[::2])
print(names[::-1])
print(names[-4:-1])

#  check if an item exist in a list
if 'sara' in names:
    print('sara is in the list : "names" ')