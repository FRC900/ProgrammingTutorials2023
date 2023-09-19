#!/usr/bin/env python3

def multiply_list(numbers):
    # numbers is a list
    # write code here! :)

    return numbers_multiplied_together

# If you run this Python program, it will test your code

def test():
    output = multiply_list([9, 0, 0])
    assert output == 0 # this is a Python keyword that throws an error if its condition is false

    output = multiply_list([1, 2, 3, 4, 5])
    assert output == 120

    output = multiply_list([3, 10, 3, 5, 2])
    assert output == 900

    print("Test passed! Nice job, your code works :)")

test()
