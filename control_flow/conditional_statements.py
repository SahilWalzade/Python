'''
If Statement
An if statement is a conditional statement that runs or skips code based on whether a condition is true or false. Here's a simple example.
'''
phone_balance = 2
bank_balance=100
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
'''
Let's break this down.

An if statement starts with the if keyword, followed by the condition to be checked, in this case phone_balance < 5, and then a colon. The condition is specified in a boolean expression that evaluates to either True or False.

After this line is an indented block of code to be executed if that condition is true. Here, the lines that increment phone_balance and decrement bank_balance only execute if it is true that phone_balance is less than 5. If not, the code in this if block is simply skipped.
'''
'''
Use Comparison Operators in Conditional Statements
You have learned about Python's comparison operators (e.g. == and !=) and how they are different from assignment operators (e.g. =). In conditional statements, you want to use comparison operators. For example, you'd want to use if x == 5 rather than if x = 5. If your conditional statement is causing a syntax error or doing something unexpected, check whether you have written == or =!
'''
#------------------------------------------------------------------------

'''
If, Elif, Else
In addition to the if clause, there are two other optional clauses often used with an if statement. For example:
'''
season = 'fall'
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')
'''
if: An if statement must always start with an if clause, which contains the first condition that is checked. If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

elif: elif is short for "else if." An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. As you can see in the example, you can have multiple elif blocks to handle different situations.

else: Last is the else clause, which must come at the end of an if statement if used. This clause doesn't require a condition. The code in an else block is run if all conditions above that in the if statement evaluate to False.

'''
#------------------------------------------------------------------------

'''
Indentation
Some other languages use braces to show where blocks of code begin and end. In Python we use indentation to enclose blocks of code. For example, if statements use indentation to tell Python what code is inside and outside of different clauses.

In Python, indents conventionally come in multiples of four spaces. Be strict about following this convention, because changing the indentation can completely change the meaning of the code. If you are working on a team of Python programmers, it's important that everyone follows the same indentation convention!

Spaces or Tabs?
The Python Style Guide recommends using 4 spaces to indent, rather than using a tab. Whichever you use, be aware that "Python 3 disallows mixing the use of tabs and spaces for indentation."


'''
#------------------------------------------------------------------------
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)
#------------------------------------------------------------------------
answer = 35
guess = 30   # this is just a sample answer and guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
   result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"
print(result)
#------------------------------------------------------------------------
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
#------------------------------------------------------------------------
