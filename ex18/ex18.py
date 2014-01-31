def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_one(arg1):
    print "arg1; %r" % arg1
    
def print_none():
    print "I got nuthin' for you, man."
    
print_two("Mark", "Maglana")
print_two_again("Mark", "Maglana")
print_one("Mark")
print_none()