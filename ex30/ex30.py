people = 30
cars = 40
buses = 55


if cars > people:
    # Print this if cars are more than people
    print "We should take the cars."
elif cars < people:
    # Print this if cars are less than people
    print "We should not take the cars."
else:
    # Print this if cars equal people
    print "We can't decide."

if buses > cars:
    # Print if there are more buses than cars
    print "That's too many buses."
elif buses < cars:
    # Print if there are more cars than buses
    print "Maybe we could take the buses."
else:
    # Print if cars equal buses
    print "We still can't decide."

if people > buses:
    # Print if people are more than buses
    print "Alright, let's just take the buses."
else:
    # Print if buses outnumber people
    print "Fine, let's stay home then."