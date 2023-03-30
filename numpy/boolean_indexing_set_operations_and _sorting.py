'''
Up to now we have seen how to make slices and select elements of an ndarray using indices. This is useful when we know the exact indices of the elements we want to select. However, there are many situations in which we don't know the indices of the elements we want to select. For example, suppose we have a 10,000 x 10,000 ndarray of random integers ranging from 1 to 15,000 and we only want to select those integers that are less than 20. Boolean indexing can help us in these cases, by allowing us select elements using logical arguments instead of explicit indices. Let's see some examples:


'''
import numpy as np

# We create a 5 x 5 ndarray that contains integers from 0 to 24
X = np.arange(25).reshape(5, 5)

# We print X
print()
print('Original X = \n', X)
print()

# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# We use Boolean indexing to assign the elements that are between 10 and 17 the value of -1
X[(X > 10) & (X < 17)] = -1

# We print X
print()
print('X = \n', X)
print()

'''
In addition to Boolean Indexing NumPy also allows for set operations. This useful when comparing ndarrays, for example, to find common elements between two ndarrays. Let's see some examples:
'''
# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))

'''
We can also sort ndarrays in NumPy. We will learn how to use the np.sort() function to sort rank 1 and rank 2 ndarrays in different ways. Like with other functions we saw before, the sort function can also be used as a method. However, there is a big difference on how the data is stored in memory in this case. When np.sort() is used as a function, it sorts the ndrrays out of place, meaning, that it doesn't change the original ndarray being sorted. However, when you use sort as a method, ndarray.sort() sorts the ndarray in place, meaning, that the original array will be changed to the sorted one. Let's see some examples:
'''
# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a function.
print()
print('Sorted x (out of place):', np.sort(x))

# When we sort out of place the original array remains intact. To see this we print x again
print()
print('x after sorting:', x)

'''
Notice that np.sort() sorts the array but, if the ndarray being sorted has repeated values, np.sort() leaves those values in the sorted array. However, if desired, we can sort only the unique elements in x by combining the sort function with the unique function. Let's see how we can sort the unique elements of x above:
'''

# We sort x but only keep the unique elements in x
print(np.sort(np.unique(x)))

'''
Finally, let's see how we can sort ndarrays in place, by using sort as a method:
'''
# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a method.
x.sort()

# When we sort in place the original array is changed to the sorted array. To see this we print x again
print()
print('x after sorting:', x)

'''
When sorting rank 2 ndarrays, we need to specify to the np.sort() function whether we are sorting by rows or columns. This is done by using the axis keyword. Let's see some examples:
'''

# We create an unsorted rank 2 ndarray
X = np.random.randint(1,11,size=(5,5))

# We print X
print()
print('Original X = \n', X)
print()

# We sort the columns of X and print the sorted array
print()
print('X with sorted columns :\n', np.sort(X, axis = 0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))



