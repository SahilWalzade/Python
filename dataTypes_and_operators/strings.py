'''
Strings
Strings in Python are shown as the variable type str. You can define a string with either double quotes " or single quotes '. If the string you are creating actually has one of these two values in it, then you need to be careful to assure your code doesn't give an error.

'''
my_string = 'this is a string!'
my_string2 = "this is also a string!!!"
#You can also include a \ in your string to be able to include one of these quotes:
this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)


first_word = 'Hello'
second_word = 'There'
print(first_word + second_word)
print(first_word + ' ' + second_word)
print(first_word + ' ' + second_word)
print(len(first_word))
first_word[0]

'''
The len() function
len() is a built-in Python function that returns the length of an object, like a string. The length of a string is the number of characters in the string. This will always be an integer.

There is an example above, but here's another one:

print(len("ababa") / len("ab"))
2.5
You know what the data types are for len("ababa") and len("ab"). Notice the data type of their resulting quotient here.
'''