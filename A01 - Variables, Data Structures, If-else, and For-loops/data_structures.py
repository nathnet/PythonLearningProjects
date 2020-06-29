# Data structures are formats of how one could go about organizing their own data.
# Knowing what format to use and when to use on certain problems is important.
# There are not necessarily a fixed way to implement your solution.
# They all depend on how you frame your issues and what would you want to apply to your solution.
# There are 4 built-in data structures in Python. They are lists, tuple, dictionary, and set.

# The first data structure we will be going to cover is "Lists"
# If you have already used other languages, some of them might be called "Arrays"
# Lists, just as its name suggests, are containers that hold values in the same fashion
# as how you would write down a list of something.

# LISTS

# Lists are indexed, meaning that they have identification number and that you could access
# through their number. It also allows duplicate values.
# The way to initialize it is
this_is_a_name_list = ["name1", "name2", "name3", "name4", "name5"]

# You can print out an entire list by doing this:
print(this_is_a_name_list)

# Or you can print out parts of the list by doing this: (In Python, numbering starts from 0)
print(this_is_a_name_list[1:5])

# Or like this:
print(this_is_a_name_list[0])

# Now it is time for you to create your own list of 2 colors.
'''Your Code Goes Here'''

# After you have created your list, that is not the end to it.
# You can do much more to your list!
# For example, you can add something to the list as well!
this_is_a_name_list.append("name6")
print(this_is_a_name_list)

# Or you can even check the length (how many elements) of your list!
print(len(this_is_a_name_list))

# For the next task, you should add another color into your list.
# But before doing that, check the length of your list.
# And after you add another color to your list, check the length again!
'''Your Code Goes Here'''

print()

# TUPLES

# Tuples, like lists, are indexed. However, the difference is that tuples are immutable.
# This means that once a tuple is created, you can no longer make changes to it.
# To initialize a tuple, you type
this_is_a_name_tuple = ("name1", "name2", "name3", "name4", "name5")

# Notice how I used brackets () rather than square brackets []
# You can print it just like how you do with lists.
print(this_is_a_name_tuple)
print(this_is_a_name_tuple[1:5])
print(this_is_a_name_tuple[0])

# These should match what you saw up there in lists.
# Since you cannot add or remove elements from tuples,
# any attempt to do so will result in an error.
# this_is_a_name_tuple.append("name6")

# The function below is used to count how many of this element are there
# in this tuple.
print(this_is_a_name_tuple.count("name1"))

# Try making a tuple of 3 colors
'''Your Code Goes Here'''

print()

# DICTIONARIES

# Dictionaries are different from the two listed data structures above.
# Dictionaries are unordered, but still indexed. You can also make further changes to
# dictionaries as you have more data in your hands as well.

# Dictionaries are implemented with curly brackets and they are implemented in
# key-value pairs rather than just values as with two structures above.
# In dictionaries, you can contain the same value, but not the same key.
# For example,
this_is_a_name_location_dict = {
    "name1": "Seattle",
    "name2": "Los Angeles",
    "name3": "New York",
    "name4": "London",
    "name5": "Bangkok"
}

# And how you print is the same
print(this_is_a_name_location_dict)

# You can even access the one that you want to know specifically
print(this_is_a_name_location_dict["name3"])
# or
print(this_is_a_name_location_dict.get("name3"))

# You can change its value through:
this_is_a_name_location_dict["name1"] = "Austin"
print(this_is_a_name_location_dict)

# Or even add more!
this_is_a_name_location_dict["name6"] = "Berlin"
print(this_is_a_name_location_dict)

# Now it is, again, your turn to create a dictionary of... your contacts!
# i.e. name: phone number or name: email
# Try it with adding and checking length as well! Recall that length
# checking function is len(variable)
'''Your Code Goes Here'''

# SETS

# Sets are unindexed and unordered! One more thing about it is that it does not
# tolerate same value! This is a clear example of what set would not be used for.
this_is_a_name_set = {"Sam", "John", "Lily", "Edgar", "Sam"}
print(this_is_a_name_set)
# As the set will remove whatever value is a duplicate of another.

# You can access individual value by mentioning the value itself
print("Sam" in this_is_a_name_set)
print("Josh" in this_is_a_name_set)
# This will tell you whether such a value exist in your data structure or not

# To add a value, you type
this_is_a_name_set.add("Josh")
print("Josh" in this_is_a_name_set)
print(this_is_a_name_set)

# Unlike dictionary, you cannot change value. The only way is to remove and add a new one.
this_is_a_name_set.remove("John")
print(this_is_a_name_set)
this_is_a_name_set.add("Kruger")
print(this_is_a_name_set)

# The last assignment in data_structures is for you to create a... YES! a set!
# Create a set containing 5 zip codes!
'''Your Code Goes Here'''

# If you would like to learn more about data structures in Python,
# I found a good cheat sheet on https://intellipaat.com/blog/tutorial/python-tutorial/data-structures-with-python-cheat-sheet/

# Now that you have learned about data structures, you can either choose to learn more about its functionalities
# with the link above or W3Schools.com. Otherwise, you can proceed to the next assignment "if-else.py"!