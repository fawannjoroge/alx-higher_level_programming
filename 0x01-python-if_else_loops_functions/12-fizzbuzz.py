#!/usr/bin/python
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzBuzz")

        elif i % 3 == 0:
            print("fizz", end=' ')
        elif i % 5 == 0:
            print("buzz", end=' ')
        else:
            print(i, end=' ')
