# square_root.py
# program that takes a positive floating-point number as input and outputs an approximation of its square root, without using built in functions.
# the approach is based on the Newton's root-finding algorithm which produces successively better approximations of the square root of a number. The improvement of the result is obtained through multiple iterations. 
# sources : https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
#           https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# author: Anna Lozenko

n = float(input("Please enter a positive floating point number: ")) 

def sqroot (n):
    if n <= 0: # check that the floating point number entered is positive. If it's not, throw an error message
        print("Error! Please enter a positive floating point number.")
        exit()
    guess = n / 2   # we take n/2 as initial guess for square root
    alpha = 0.1 # precision threshold for stopping the iteration
    while True: # the loop will run until the below condition is met (closerGuess - guess < alpha)
        closer_guess = 0.5 * (guess + n/guess)  # Newton's formula 
        if closer_guess - guess < alpha: # stop the iterations if the change is smaller than alpha
            break
    guess = closer_guess
    return guess


print(f"The square root of {n} is {sqroot(n):.2f}.") # output the result with 2 decimal places