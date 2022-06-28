# The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.

import csv

import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")



# Open the election results and read the file.

with open(file_to_load) as election_data:
    
# Read the file object with the reader function.

    file_reader = csv.reader(election_data)


    # Read and print the header row.

    headers = next(file_reader)

    print(headers)

    
# for row in file_reader:

#    print(row)
#Print each row in the CSV file.



# Write some data to the file

#outfile.write("Counties in the Election\n-------------------------\n")

#outfile.write("Arapahoe\nDenver\nJefferson")


# Close the file

# file_to_load.close()

# Open the election results and read the file.

#with open(file_to_load) as election_data:

    # Print the file object.
#    print(election_data)