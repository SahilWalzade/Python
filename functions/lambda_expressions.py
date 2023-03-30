'''
Lambda Expressions
You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

With a lambda expression, this function:
'''
def multiply(x, y):
    return x * y
#can be reduced to
multiply = lambda x, y: x * y
multiply(4, 7)
'''
Components of a Lambda Function
The lambda keyword is used to indicate that this is a lambda expression.
Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.
With this structure, lambda expressions aren’t ideal for complex functions, but can be very useful for short, simple functions.
'''
#-------------------------------------------------------------------------------------------
#Lambda with map

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)
#-------------------------------------------------------------------------------------------
#Lambda with Filter

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)