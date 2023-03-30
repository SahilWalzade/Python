'''
Dictionaries and Identity Operators
Dictionaries
A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.
'''
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
#Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the same type! We can look up values or insert new values in the dictionary using square brackets that enclose the key.
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
#We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. Dicts have a related method that's also useful, get. get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.
print("carbon" in elements)
print(elements.get("dilithium"))
#Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program.

'''
Identity Operators
Keyword	Operator
is	evaluates if both sides have the same identity
is not	evaluates if both sides have different identities
You can check if a key returned None with the is operator. You can check for the opposite using is not.
'''
n = elements.get("dilithium")
print(n is None)
print(n is not None)