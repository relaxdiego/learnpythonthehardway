def do_while(stop_at, step=1):
    i = 0
    numbers = []

    for i in range(0, stop_at, step):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num


do_while(8, 2)
do_while(5)
