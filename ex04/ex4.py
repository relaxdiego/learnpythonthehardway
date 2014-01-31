# Assign 100 to cars
cars = 100

# Assign a float to space_in_a_car
space_in_a_car = 4.0

# Assign integer values to variables
drivers = 30
passengers = 90

# Assign 70 to cars_not_drive
cars_not_driven = cars - drivers

# Assign 30 to cars_driven
cars_driven = drivers

# Assign 30 * 4.0 (float) to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# Assign integer to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# Print all the things!
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Study drills

# 0) There's an extra underscore in the variable
# 1) 4.0 is a floating point number. It will yield floats when operated on
