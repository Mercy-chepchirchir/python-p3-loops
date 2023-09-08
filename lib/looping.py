#!/usr/bin/env python3
def happy_new_year():
    # code goes here!
    num =10
    while num > 0:
        print (num)
        num-=1
    print ("Happy New Year!")    
    

def square_integers(int_list):
    # code goes here!
    square = []
    for num in int_list:
        square.append(num ** 2)
    return square
    

    
def fizzbuzz():
    # your code here
    num = 1
    for num in range(1,101):
         if num % 3 == 0 and num % 5 == 0:
             print("FizzBuzz")
         elif num % 3 == 0:
            print ("Fizz")
         elif num % 5 == 0:
            print("Buzz")
         else:
            print (num)
    
