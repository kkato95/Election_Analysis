# Create a filename variable to a direct or indirect path to the file.
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# After we create the file_to_save path, we set open(file_to_save, "w") to a filename, outfile
# Then, we use the filename variable to write "Hello World" to the file using the write() function from the os module.
# Lastly, we use outfile.close() to close the file.

################################################################################################################################

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
txt_file.write("Hello World")

# Write three counties to the file.
txt_file.write("Arapahoe")
txt_file.write("Denver")
txt_file.write("Jefferson")

# Write three counties to the file.
txt_file.write("Arapahoe, Denver, Jefferson")

# Write three counties to the file.
txt_file.write("Arapahoe\nDenver\nJefferson")