"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Storing a variable
label <assignment operator> value or expression
a = 1
b = 2
c = a + b
c = a + b -> 1 + 2 -> 3 -> c = 3

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
def addition(a, b):
    #return our sum to the caller
    return a + b

print(addition(3, 2))
print(addition(-3, -6))
print(addition(7, 3))
