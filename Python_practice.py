counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}



#if "Arapahoe" in counties or "El Paso" in counties:

#    print("Arapahoe or El Paso is in the list of counties.")

#else:

#    print("Arapahoe and El Paso are not in the list of counties.")



# The county variable is declared and set equal to the first item in the list of counties.
#for county in counties:
# As long as there are item in the list of counties the code will continue to iterate through the list till it is exhausted of items.
#    print(county)



#for county, voters in counties_dict.items():
#    print(county, voters)

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")

#else:
#    print("Arapahoe and El Paso are not in the list of counties.")



# Using the built in function of range(). To demonstrate we will first create a longer for loop to solve the problem
#numbers = [0, 1, 2, 3, 4]

#for num in numbers:
#    print(num)
# As directed, the for loop listed out each number from the variable numbers until that list got to the end and closed the loop.
#But, using the built in function of range() for leaner code.
#for num in range(5):
#    print(num)
# The function is returning a sequence of numbers, 
# starting from 0 by default, 
# and incrementing by 1, and stops before the specified number.



# Indexing can also be used to iterate through a list.
# If the list contains strings, we'll need to get the length of this list as an integer for the range() function to iterate.
#for i in range(len(counties)):
# The i variable is used to indicate the index (or the values 0, 1, and 2) in the length of the counties list.
# Inside the range() funtion, we get the length of the list of counties, which is integer 3.
#    print(counties[i])
# Then, we iterate through the list, where the variable i is equal to 0 for the first index.
# The 0 is passed into the print(counties[i]) statement, where i= 0, and "Arapahoe" is printed first,
# and the loop continues printing each item til there are no more, and closes the loop.

# The letter i for the variable was used for simplicity.
# The variable used to iterate through a for loop is chosen arbitrarily, 
# and can be anything, but best practice is keeping it in context of the situation.
# We can iterate through a tuple the same way we iterate through a list.



# We can also use a for loop to iterate over a dictionary to get all the keys, all the values, or all the keys and values.

# Get the Keys of a dictionary
# To get only the keys from a dictionary using a for loop, 
# the loop can be written like the code written to iterate over lists or tuples.
#for county in counties_dict:
#   print(county)

# The keys() method can also be used to iterate over a dictionary to get the keys:
#for county in counties_dict.keys():
#    print(county)
# When using the keys() method, it doesn't matter what variable name we use in the for loop.
# The keys() method will print each key in order.

# Get the Values of a dictionary
# To get the values of a dictionary, we can use the values() method to iterate over the dictionary and only grab values.
#for voters in counties_dict.values():
#    print(voters)
# Also, when using the values() method, it doesn't matter what variable name we use in the for loop.
# The values() method will print each value in order.

# Other methods of referencing the values:

# Using the format dictionary_name[key], include the key "county" in the for loops print statement.
# This will return the value of the key in the output.
#for county in counties_dict:
#    print(counties_dict[county])

# Another method is to use the get() method on the dicitonary in the for loop.
#for county in counties_dict:
#    print(counties_dict.get(county))



# Get the Key-Value Pairs of a Dictionary:
# We use the items() method in the for loop to get the key-value pairs.
# Which follows this general format:
#for key, value in dictionary_name.item():
#    print(key, value)
# When you use the items() method, you can use any two variables to refernce the "key" and "value" respectively.
#for county, voters in counties_dict.items():
#    print(county, voters)
# Remember, the first variable declared in the for loop is assigned to the keys.
# And the second variable is assigned to the values.
# Print output made into an actual sentence with both key and value.
#for county, voters in counties_dict.items():
#    print((county) + " county has " + str(voters) + " registerd voters.")
# Here on up has been copied to Python cheatsheet worksheet.

# Iterate through a List of Dictionaries
# A for loop can be used to iterate through a list of dictionaries. With a for loop we can:
# Retrieve each dictionary in the list
# Retrieve only the values of each dictionary
# Retrieve the key-value pairs of each dictionary

# Get each Dictionary in a List of Dictionaries
# To print each dictionary in "voting_data", use the standard format for iterating over the list of dictionaries with a for loop:

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#        print(county_dict)

# When we execute the code, each dictionary is printed on a separate line:
# {'county': 'Arapahoe', 'registered_voters': 422829}
# {'county': 'Denver', 'registered_voters': 463353}
# {'county': 'Jefferson', 'registered_voters': 432438}

# Since this is a list of dictionaries, use the range() function to iterate over the list.

# Get the Values from a List of Dictionaries
# Nested for loops are used to retrieve only values from each dictionary in the list of dictionaries.
# The first for loop: for county_dict in voting_data:
# This first loop is retrieving each dictionary.
# The second for loop uses the values() method on the variable county_dict in order to get each value.
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
#The executed code:
# >>>
# Arapahoe
# 422829
# Denver
# 463353
# Jefferson
# 432438
# >>>

# Printing each county name fromeach dictionary can be done with print statement for the for loop.
#for count_dict in voting_data:
#    print(count_dict['county'])
#
# When the code is executed:
# Arapahoe
# Denver
# Jefferson

# Printing Methods
# There are different print methods for the print() function.
# These can be used to print in a variety of formats and how to format floating-point.
#
# The print() Function
# We have been using the print() function to print simple statements,
# consisting of strings or a sentence displayed between quotes.
# For example: print("Hello World")
# and a string with integer values converted to a string using concatenation with the "+" sign.
# For example:
# print ("Your interest for the year is $" + str(interest))
#
# Those print() methods are ideal for simple statements,
# but become cumbersome when we need to print items of values from a dictionary.
#
#
# F-strings: Formatted String Literals
# Since 3.7, printing has become much easier with the use of f-string literals, which can be used in place of concatenation.
# The general format for f-strings is as follows:
# 1. The f-string begins with an f followed by a string contained within quotes.
# 2. In the f-string, curly braces are used to add variables or expressions to the f-string.
#
#As an example, let's edit the code to calculate the percentage of votes using f-string literals:
# Original Code
# 
#my_votes = int(input("How many votes did you get in the election? "))
##total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#
# Code reformated with f-strings.
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# Inside the curly braces, the f-string performs the calculation and formats the value as a string.
#
# Using F-Strings with Dictionaries
#
# F-strings can be used to print out the keys or values of a dictionary making code easier to read and write.
#
# Using code written without f strings as an example:
#counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")
#
# Output:
# Arapahoe county has 369237 registered voters.
# Denver county has 413229 registered voters.
# Jefferson county has 390222 registered voters.
#
# Using f-strings we can rewrite the print statements to be more intuitive and clear.
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings
#
# Another use for f-strings is to print multiple strings or lines to the screen:
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)
#
# Output:
# How many votes did the candidate get in the election? 3345
#What is the total number of votes in the election? 23123
#You received 3345 number of votes. The total number of votes in the election was 23123. You received 14.466115988409808% of the total votes.

#
# Format Floating-Point Decimals
#
# In the previous algorithm, the percentage of results had a large floating-point decimal.
# We can format the floating-point decimal with a thousands separator and specify a decimal positon.
# The general format: 
# f'{value:{width}.{percision}}'
# In the format, the width specifies the number of characters used to display the value.
# If a vaule needs more space than the width specifies, the addional space is used.
#
# The precision indicates the number of decimal places to format the value.
# To format the interest to two decimal places, we would use .2f, where f means "floating-point decimal format"
# When formatting a number, we can add the thousands separator with a comma. The comma is placed after the {width}.
# f'{value:{width},.{precision}}'
#
# Lets add a thousands separator for the percentage of votes to two decimal places.

#message_to_candidate = (
#   f'You received {candidate_votes:,} number of votes.'
#    f'The total number of votes in the election was {total_votes:,}.'
#    f'You received {candidate_votes / total_votes * 100:.2f}% of the total votes.')
#
# Output
# You received 3,345 number of votes. The total number of votes in the election was 23,123. You received 14.47% of the total votes.
