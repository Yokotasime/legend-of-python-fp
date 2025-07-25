
# File managing ways via Python


sent_message = 'Hey Bitch this is a secret message'  # Define the original message
file_path = 'sent_message.txt'  # Set the file path for writing/reading the message

with open('sent_message.txt', 'w') as file:  # Open the file in write mode
    file.write(sent_message)  # Write the original message to the file

with open(file_path, 'r+') as file:  # Open the file in read + write mode
    original_message = file.read()  # Read and store the original message
    file.seek(0)  # Move the cursor to the beginning of the file

unsent_message = 'This message is unsent'  # Define the new "unsent" message

with open(file_path, 'r+') as file:  # Reopen the file in read + write mode
    file.truncate(len(unsent_message))  # Truncate the file to the length of the new message
    file.write(unsent_message)  # Write the new message to the file

print('Original Message: ', original_message)  # Display the original message in the terminal
print('Unsent Message: ', unsent_message)  # Display the new "unsent" message in the terminal
