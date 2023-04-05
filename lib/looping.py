#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while (counter > 0):
       print(counter)
       counter -= 1
    print("Happy New Year!")   


def square_integers(int_list):
    return [num * num for num in int_list]
    
    

def fizzbuzz():
    i = 1
    while (i<=100):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
        i += 1                

