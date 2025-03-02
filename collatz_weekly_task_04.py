# weekly task 4
# collatz.py
# Program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step the program calculates the next value by taking the current value and, if it is even, divides it by two, but if it is odd, multiplies it by three and add one.
# Program stops if the current value is one.
# author: Anna Lozenko


number = int(input("Please, enter a positive integer: "))

print(number)

while number != 1:
    if number % 2 == 0:  # even
        number = number // 2
    else:       # odd
        number = (number * 3) + 1
    print(number)