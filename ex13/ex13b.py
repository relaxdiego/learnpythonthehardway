from sys import argv

filename, first, second = argv

what = raw_input("Which argument do you want? (first, second) ")

if what == 'first':
    print first
else:
    print second
