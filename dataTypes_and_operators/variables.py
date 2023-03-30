'''
Variables I
Variables are used all the time in Python! Below is the example you saw in the video where we performed the following:

mv_population = 74728

Here mv_population is a variable, which holds the value of 74728. This assigns the item on the right to the name on the left, which is actually a little different than mathematical equality, as 74728 does not hold the value of mv_population.

In any case, whatever term is on the left side, is now a name for whatever value is on the right side. Once a value has been assigned to a variable name, you can access the value from the variable name.

----------------------------------------------------------
Variables II
In this video you saw that the following two are equivalent in terms of assignment:

x = 3
y = 4
z = 5
and

x, y, z = 3, 4, 5
However, the above isn't a great way to assign variables in most cases, because our variable names should be descriptive of the values they hold.

Besides writing variable names that are descriptive, there are a few things to watch out for when naming variables in Python.

1. Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.

2. You can’t use reserved words or built-in identifiers that have important purposes in Python, which you’ll learn about throughout this course. A list of python reserved words is described here. Creating names that are descriptive of the values often will help you avoid using any of these words. A quick table of these words is also available below.

3. The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

YES

my_height = 58
my_lat = 40
my_long = 105

NO

my height = 58
MYLONG = 40
MyLat = 105
Though the last two of these would work in python, they are not pythonic ways to name variables. The way we name variables is called snake case, because we tend to connect the words with underscores.
---------------------------------------------------
Assignment Operators
Below are the assignment operators from the video. You can also use *= in a similar way, but this is less common than the operations shown below. You can find some practice with much of what we have already covered
https://www.programiz.com/python-programming/operators

x+=2 :: x=x+2
x-=2 :: x=x-2

'''
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)
