#Defining Functions
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
print(cylinder_volume(10, 3)) #cylinder_volume(10, 3)

'''
Function Header
Let's start with the function header, which is the first line of a function definition.

The function header always starts with the def keyword, which indicates that this is a function definition.
Then comes the function name (here, cylinder_volume), which follows the same naming conventions as variables. You can revisit the naming conventions below.
Immediately after the name are parentheses that may include arguments separated by commas (here, height and radius). Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. If a function doesn't take arguments, these parentheses are left empty.
The header always end with a colon :.
'''

'''
Function Body
The rest of the function is contained in the body, which is where the function does its work.

The body of a function is the code indented after the header line. Here, it's the two lines that define pi and return the volume.
Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function. A return statement consists of the return keyword followed by an expression that is evaluated to get the output value for the function. If there is no return statement, the function simply returns None.
'''

'''
Naming Conventions for Functions
Function names follow the same naming conventions as variables.

Only use ordinary letters, numbers and underscores in your function names. They can’t have spaces, and need to start with a letter or underscore.
You can’t use reserved words or built-in identifiers that have important purposes in Python, which you’ll learn about throughout this course. A list of Python reserved words is described here.
Try to use descriptive names that can help readers understand what the function does.

'''

'''
Print vs. Return in Functions
Here are two valid functions. One returns a value and one simply prints a value, without returning anything. Test run this code and experiment to understand the difference.
'''

#--------------------------------------------------------------------------

'''
Default Arguments
We can add default arguments in a function to have default values for parameters that are unspecified in a function call.
'''
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

'''
In the example above, radius is set to 5 if that parameter is omitted in a function call. If we call cylinder_volume(10), the function will use 10 as the height and 5 as the radius. However, if we call cylinder_volume(10, 7) the 7 will simply overwrite the default value of 5.

Also notice here we are passing values to our arguments by position. It is possible to pass values in two ways - by position and by name. Each of these function calls are evaluated the same way.
'''
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name