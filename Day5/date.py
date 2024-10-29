# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime 

# Current date 
x = datetime.datetime.now()
print(x)

# format output 
print(x.strftime("%d"))

