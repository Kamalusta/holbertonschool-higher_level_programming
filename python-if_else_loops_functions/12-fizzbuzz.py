#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            nbr = "FizzBuzz"
        elif (i % 5) == 0:
            nbr = "Buzz"
        elif (i % 3) == 0:
            nbr = "Fizz"
        else:
            nbr = i
        print("{} ".format(nbr), end='')
