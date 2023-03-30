'''
Try Statement
We can use try statements to handle exceptions. There are four clauses you can use (one more in addition to those shown in the video).

try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.
'''
while True:
    try:
        x= int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number !')
    finally:
        print('\n Attempted input')
#-------------------------------------------------------------------
'''
Specifying Exceptions
We can actually specify which error we want to handle in an except block like this:

'''
while True:
    try:
        x= int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number !')
    finally:
        print('\n Attempted input')
'''
try:
    # some code
except ValueError:
    # some code
Now, it catches the ValueError exception, but not other exceptions. If we want this handler to address more than one type of exception, we can include a parenthesized tuple after the except with the exceptions.

try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code
Or, if we want to execute different blocks of code depending on the exception, you can have multiple except blocks.

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
'''
def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)