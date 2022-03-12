# Print first 2 items from the list
counties = ["Arapahoe","Denver","Jefferson"]
print(counties[:2])

#Appending 'El Paso' to the list
counties.append("El Paso")
print(counties[-1])

# Insert new item to be placed at the 3rd position in the list
# list.insert(index, obj)
counties.insert(2, 'El Paso')
print(counties)

# Remove an item from the list
counties.remove('El Paso')
print(counties)

# Can use pop() method to remove using index values
counties.pop(3)
print(counties)

# Replaces the index value in the bracket with what is inside the quotes
counties[2] = "El Paso"
print(counties)

# Creating a tuple
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
print(counties_tuple[1])

# Creating a dictionary with paris - {key: value , key1: value1, ..}
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

# To get all keys and values use items()
# A list of tuples where the first element in each tuple is the key of the ditionary, and the seond element is the value
# Output is inside dict([]) is what is known as a view object
print(counties_dict.items())

# Get all the keys
counties_dict.keys()

# Get all the values
counties_dict.values()

# Get a specific value - use get() method
counties_dict.get('Denver')

#Create voting_data list
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

# If-else statement - will return if 'El Paso' is in the list - in & not in - are Membership Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# Logical Opertors - and, or, not
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# For loop
for county in counties:
    print(county)

# Using i in for loop returning each item
for i in range(len(counties)):
    print(counties[i])

# Print all they keys in the counties list
for county in counties_dict.keys():
    print(county)

# Get the values of a key
for county in counties_dict:
    print(counties_dict.get(county))

# Print the key:value pair of the dictionary
# We use items() method in for loop - key vand value for each dictionary
for county, voters in counties_dict.items():
    print(county, voters)

# Get each dictionary into a list using for loop
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# Use the range() - To retreive only the values from each dictionary, we used nested for
# First loop: For county_dict in voting_data
# Second loop: for loop, using values() method on variable county_dict
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Import election results

file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file. Open file_to_load
# Using 'r' mode to read file - then closing the file
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Dont have to use the close() everytime we open a file - replace 'open(file)' with with()
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)