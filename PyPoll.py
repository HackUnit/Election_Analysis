# The data we need to retrieve. 

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

# Initialize a total vote counter

total_votes = 0

# Candidate Options

candidate_options = []

# Declare an empyty dictionary

candidate_votes = {}



# Open the election results and read the file.

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
    
    # Read the header row.

    headers = next(file_reader)

    # Print each row in the CSV file.

    for row in file_reader:

        # Add to the total vote count.
        
        total_votes += 1

        # Print the canidates name from each row

        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to
        # the candidate list

        if candidate_name not in candidate_options:

            # Add the candidate name to the list of candidates

            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.

            candidate_votes[candidate_name] = 0

        # Add a vote to that candidates count.

        candidate_votes[candidate_name] += 1



for candidate_name in candidate_votes:

    # Retrieve vote count and percentage.

    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes.

    vote_percentage = float(votes) / float(total_votes) * 100

    # Print each candidates, their voter count, and percentage of votes to the terminal.   

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")



    # Determine winnning vote count, winning percentage, and cadidate

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes

        winning_candidate = candidate_name

        winning_percentage = vote_percentage

# Print the winning candidates' results to the terminal.

winning_candidate_summary = (

    f"-------------------------\n"

    f"Winner: {winning_percentage}\n"

    f"Winning Vote Count: {winning_count:,}\n"

    f"Winning Percentage: {winning_percentage:.1f}%\n"

    f"-------------------------\n")


print(winning_candidate_summary)



# Write some data to the file

#outfile.write("Counties in the Election\n-------------------------\n")

#outfile.write("Arapahoe\nDenver\nJefferson")


# Close the file

# file_to_load.close()

# Open the election results and read the file.

#with open(file_to_load) as election_data:

    # Print the file object.
#    print(election_data)