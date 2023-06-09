'''
Iterators and Generators
Iterables are objects that can return one of their elements at a time, such as a list. Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

An iterator is an object that represents a stream of data. This is different from a list, which is also an iterable, but is not an iterator because it is not a stream of data.

Generators are a simple way to create iterators using functions. You can also define iterators using classes, which you can read more about here.

Here is an example of a generator function called my_range, which produces an iterator that is a stream of numbers from 0 to (x - 1).
'''
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
'''
Notice that instead of using the return keyword, it uses yield. This allows the function to return values one at a time, and start where it left off each time it’s called. This yield keyword is what differentiates a generator from a typical function.

Remember, since this returns an iterator, we can convert it to a list or iterate through it in a loop to view its contents. For example, this code:
'''
for x in my_range(5):
    print(x)

'''
Why Generators?
You may be wondering why we'd use generators over lists. Here’s an excerpt from a stack overflow page that addresses this:

Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.
'''
#-------------------------------------------------------------------------------------
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
#-------------------------------------------------------------------------------------
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
#-------------------------------------------------------------------------------------
