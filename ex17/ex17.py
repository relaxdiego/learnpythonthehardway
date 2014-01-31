from sys import argv
from os.path import exists

script, source, target = argv

data = open(source).read()
open(target, 'w').write(data)

print "Copied %d bytes from %s to %s" % (len(data), source, target)

# NOTE: Not explicitly closing files is fine for this exercise but
# is not recommended because some implementations of Python do not
# have reference counters and may result in resource leaks.