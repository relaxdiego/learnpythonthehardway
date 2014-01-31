# Define the cheese_and_crackers function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print out text and the values of the two arguments
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"

# Call the function with literal integer values as arguments
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"

# Call the function supplying variables as args
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"

# Call the function supplying results of mathematical operations
# as the arguments.
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"

# Call the function supplying the results of mathematical operations
# between variables and integer literals as arguments.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def hello_back(first_name, last_name):
    print "Hello, %s %s!" % (first_name, last_name)

hello_back("Mark", "Maglana")
hello_back(raw_input("First name? "), raw_input("Last name? "))
# Skipping the 8 other ways to call the method. I get it. :-)
