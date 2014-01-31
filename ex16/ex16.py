# Import the argv module from the sys package
from sys import argv

# Unpack the CLI arguments to these variables
script, filename = argv

# Print out a warning for the user
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Wait for the ENTER key
raw_input("?")

# Print notice and open the file for writing
print "Opening the file..."
target = open(filename, 'w')


# Print notice and delete contents of the file
#
# COMMENTED OUT since it's not necessary when
# opening a file in write ('w') mode.
#
# print "Truncating the file.  Goodbye!"
# target.truncate()


# Print notice
print "Now I'm going to ask you for three lines."

# Ask for user input three times
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Print notice
print "I'm going to write these to the file."

# Write the three inputs separated by a newline
target.write("%s\n%s\n%s" % (line1, line2, line3))


# Print notice and close the file
print "And finally, we close it."
target.close()