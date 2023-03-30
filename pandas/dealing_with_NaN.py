'''
As mentioned earlier, before we can begin training our learning algorithms with large datasets, we usually need to clean the data first. This means we need to have a method for detecting and correcting errors in our data. While any given dataset can have many types of bad data, such as outliers or incorrect values, the type of bad data we encounter almost always is missing values. As we saw earlier, Pandas assigns NaN values to missing data. In this lesson we will learn how to detect and deal with NaN values.

We will begin by creating a DataFrame with some NaN values in it.
'''
import pandas as pd
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items
'''
We can clearly see that the DataFrame we created has 3 NaN values: one in store 1 and two in store 3. However, in cases where we load very large datasets into a DataFrame, possibly with millions of items, the number of NaN values is not easily visualized. For these cases, we can use a combination of methods to count the number of NaN values in our data. The following example combines the .isnull() and the sum() methods to count the number of NaN values in our DataFrame
'''
# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

# We print x
print('Number of NaN values in our DataFrame:', x)
'''
In the above example, the .isnull() method returns a Boolean DataFrame of the same size as store_items and indicates with True the elements that have NaN values and with False the elements that are not. Let's see an example:
'''
store_items.isnull()
'''
In Pandas, logical True values have numerical value 1 and logical False values have numerical value 0. Therefore, we can count the number of NaN values by counting the number of logical True values. In order to count the total number of logical True values we use the .sum() method twice. We have to use it twice because the first sum returns a Pandas Series with the sums of logical True values along columns, as we see below:
'''
store_items.isnull().sum()
'''
The second sum will then add up the 1s in the above Pandas Series.

Instead of counting the number of NaN values we can also do the opposite, we can count the number of non-NaN values. We can do this by using the .count() method as shown below:
'''
# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())
'''
Now that we learned how to know if our dataset has any NaN values in it, the next step is to decide what to do with them. In general we have two options, we can either delete or replace the NaN values. In the following examples we will show you how to do both.

We will start by learning how to eliminate rows or columns from our DataFrame that contain any NaN values. The .dropna(axis) method eliminates any rows with NaN values when axis = 0 is used and will eliminate any columns with NaN values when axis = 1 is used. Let's see some examples

'''
# We drop any rows with NaN values
store_items.dropna(axis = 0)

# We drop any columns with NaN values
store_items.dropna(axis = 1)
'''
Notice that the .dropna() method eliminates (drops) the rows or columns with NaN values out of place. This means that the original DataFrame is not modified. You can always remove the desired rows or columns in place by setting the keyword inplace = True inside the dropna() function.

Now, instead of eliminating NaN values, we can replace them with suitable values. We could choose for example to replace all NaN values with the value 0. We can do this by using the .fillna() method as shown below.
'''
# We replace all NaN values with 0
store_items.fillna(0)
'''
We can also use the .fillna() method to replace NaN values with previous values in the DataFrame, this is known as forward filling. When replacing NaN values with forward filling, we can use previous values taken from columns or rows. The .fillna(method = 'ffill', axis) will use the forward filling (ffill) method to replace NaN values using the previous known value along the given axis. Let's see some examples:
'''
# We replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)
'''
Notice that the two NaN values in store 3 have been replaced with previous values in their columns. However, notice that the NaN value in store 1 didn't get replaced. That's because there are no previous values in this column, since the NaN value is the first value in that column. However, if we do forward fill using the previous row values, this won't happen. Let's take a look:
'''
# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)
'''
We see that in this case all the NaN values have been replaced with the previous row values.

Similarly, you can choose to replace the NaN values with the values that go after them in the DataFrame, this is known as backward filling. The .fillna(method = 'backfill', axis) will use the backward filling (backfill) method to replace NaN values using the next known value along the given axis. Just like with forward filling we can choose to use row or column values. Let's see some examples:
'''
# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)
'''
Notice that the NaN value in store 1 has been replaced with the next value in its column. However, notice that the two NaN values in store 3 didn't get replaced. That's because there are no next values in these columns, since these NaN values are the last values in those columns. However, if we do backward fill using the next row values, this won't happen. Let's take a look:
'''
# We replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)
'''
Notice that the .fillna() method replaces (fills) the NaN values out of place. This means that the original DataFrame is not modified. You can always replace the NaN values in place by setting the keyword inplace = True inside the fillna() function.

We can also choose to replace NaN values by using different interpolation methods. For example, the .interpolate(method = 'linear', axis) method will use linear interpolation to replace NaN values using the values along the given axis. Let's see some examples:
'''
# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)
'''
Notice that the two NaN values in store 3 have been replaced with linear interpolated values. However, notice that the NaN value in store 1 didn't get replaced. That's because the NaN value is the first value in that column, and since there is no data before it, the interpolation function can't calculate a value. Now, let's interpolate using row values instead:
'''
# We replace NaN values by using linear interpolation using row values
store_items.interpolate(method = 'linear', axis = 1)

'''
Just as with the other methods we saw, the .interpolate() method replaces NaN values out of place.
'''
#------------------------------------------------------------------------
import pandas as pd
import numpy as np

# Since we will be working with ratings, we will set the precision of our
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame.

# Create a dictionary with the data given above
dat = { 'Book Title': books,
        'Author': authors,
        'User 1': user_1,
        'User 2': user_2,
        'User 3': user_3,
        'User 4': user_4}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:

book_ratings.fillna(book_ratings.mean(), inplace = True)

















