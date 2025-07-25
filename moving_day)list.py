import csv  # Importing the csv module to handle CSV file operations

# Defining the packing list data as a list of lists (table format)
data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    # Try to open the CSV file in read mode to check if it already exists
    with open('moving_day.csv', 'r', newline='') as file:
        reader = csv.reader(file)  # Create a CSV reader object
        for row in reader:  # Loop through each row and print it
            print(row)
except FileNotFoundError:
    # If the file does not exist, notify the user and create a new one
    print("Packing list file not found. Create a new one.")
    
    # Open the file in write mode to create it and write the initial data
    with open('moving_day.csv', 'w') as file:
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerows(data)  # Write all rows of the 'data' list
    print("Packing list created successfully.")  # Confirmation message
