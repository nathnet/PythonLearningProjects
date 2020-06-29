'''
Comments are essential in communicating with other programmers and yourself in the future 
For commmenting, we have two options. The first one is to use 3 apostrophes like this one ('''''').
The second way will be using # for a single line comment, which will be shown below.
'''

''' 
Here I create a variable called "hi", which contains string "hello world!" in it
If you do print(hi) before you initialize, you will get an error message
Try removing # before the code below to see what it outputs!
'''
# print(hi)
hi = "hello world!"
print(hi)

# Here it is your turn to create a variable called "UW", containing "University of Washington"
# GO!
'''Your Code Goes Here'''

# However, if you would like to print out the word without saving it to a variable, you will need
# to print it out with ' or " surrounding it.
print("Hello World!")

# You can technically create variables of any types without having to worry about what type it is
# It can be String (words), numbers (both integers and decimals) or boolean (true/false)
num = 2020
print(num)
boolean = True
print(boolean)
# You can combine variables with normal strings in print
print('Covid19 lasts for at least half', num)
# Another way to print is:
print(f'Covid19 lasts for at least half {num}')
# Or
print('Covid19 lasts for at least half' + str(num))
# For the last way to print, you will require to convert the variable into strings if they are not strings
# If you are not sure which type it is, type
print(type(num))

# Use them at your discretion

# Now it's your turn! Create variables to tell what your name, your age, and something you can
# reply with true/false. Then, print out "My name is ____. I am ____ years old." and something
# you can reply with boolean at the end!
'''Your Code Goes Here'''

# Next up, you will be learning how to operate a list
# Go to "data_structures.py"
