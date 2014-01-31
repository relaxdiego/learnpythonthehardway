# Import the argv module from the sys package
from sys import argv

# Unpack the CLI arguments into these variables
script, input_file = argv

# Define a method named print_all which prints the
# entire contents of the file.
def print_all(f):
    print f.read()

# Move the 'read head' of the file back to the
# first byte/position
def rewind(f):
    f.seek(0)

# Print a line of the file
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open the file as indicated in the CLI argument
current_file = open(input_file)

print "First let's print the whole file:"

# Print all contents
print_all(current_file)

print "\nNow let's rewind, kind of like a tape."

# Move 'read head' back to first position
rewind(current_file)

print "Let's print three lines:\n"

# Print one line at a time until 3rd line of the file.
for current_line in range(1, 4):
    print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)