'''
Lists!
Data structures are containers that organize and group data types together in different ways. A list is one of the most common and basic data structures in Python.

You saw here that you can create a list with square brackets. Lists can contain any mix and match of the data types you have seen so far.
'''
list_of_random_things = [1, 3.4, 'a string', True]
#This is a list of 4 elements. All ordered containers (like lists) are indexed in python using a starting index of 0. Therefore, to pull the first value from the above list, we can write:
print(list_of_random_things[0])
#Alternatively, you can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.
print(list_of_random_things[-1] )


'''
Slice and Dice with Lists
You saw that we can pull more than one value from a list at a time by using slicing. When using slicing, it is important to remember that the lower index is inclusive and the upper index is exclusive.

Therefore, this:
'''
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[1:2])
#will only return 3.4 in a list. Notice this is still different than just indexing a single element, because you get a list back with this indexing. The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.
#If you know that you want to start at the beginning, of the list you can also leave out this value.
print(list_of_random_things[:2])
#or to return all of the elements to the end of the list, we can leave off a final element.
print(list_of_random_things[1:])

'''
Are you in OR not in?
You saw that we can also use in and not in to return a bool of whether an element exists within our list, or if one string is a substring of another.
'''
print('this' in 'this is a string')
print(5 not in [1, 2, 3, 4, 6])


'''
Mutability and Order
Mutability is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called mutable. However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.
'''
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
#strings are immutable. This means to change this string, you will need to create a completely new string.
'''
** Order** is about whether the position of an element in the object can be used to access the element. ** Both strings and lists are ordered.** We can use the order to access parts of a list and string.

However, you will see some data types in the next sections that will be unordered. For each of the upcoming data structures you see, it is useful to understand how you index, are they mutable, and are they ordered. Knowing this about the data structure is really useful!

Additionally, you will see how these each have different methods, so why you would use one data structure vs. another is largely dependent on these properties, and what you can easily do with it!
'''

