# square_root.py
# program that takes a positive floating-point number as input and outputs an approximation of its square root, without using built in functions.
# the approach is based on the Newton's root-finding algorithm which produces successively better approximations of the square root of a number. The improvement of the result is obtained through multiple iterations. 
# sources : https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
#           https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# author: Anna Lozenko

n = float(input("Please enter a positive floating point number: "))

def sqroot (n):
    guess = n / 2   # we take n/2 as initial guess for square root
    closerGuess = 0.5 * (guess + n/guess)  # Newton's formula 
    while closerGuess != guess: # we iterate until we find the square root value
        guess = closerGuess
        closerGuess = 0.5 * (guess + n/guess)
    return guess

print("The square root of {} is {}.".format(n, sqroot(n)))