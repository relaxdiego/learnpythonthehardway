# Assign string containing 10 to x. Basically,
# these all assign strings with formatted numbers
# in them.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # strings in string (2x)

# Print the joke
print x
print y

# Clarify in case the joke wasn't clear
print "I said: %r." % x                     # string in string
print "I also said: '%s'." % y              # string in string

# Assign boolean and string with formatting specifier
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print string and the boolean
print joke_evaluation % hilarious

# Assign strings to variables
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate string then print
print w + e     # The + operator between strings is the concatenation operator