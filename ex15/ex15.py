# Import the argv module located in the sys package
from sys import argv

# Unpack the arguments to these two variables
script, filename = argv

# Open the file referred to by 'filename'
txt = open(filename)

# Print a notification
print "Here's your file %r:" % filename

# Print the contents of the file
print txt.read()

# Be a good citizen and close the file handle
txt.close()

# Print another notification
print "Type the filename again:"

# Ask for user input
file_again = raw_input("> ")

# Open the file referred to by 'file_again'
txt_again = open(file_again)

# Print that contents of that file!
print txt_again.read()

# Be a good citizen and close the file handle
txt_again.close()