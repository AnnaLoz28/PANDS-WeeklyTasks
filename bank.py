# bank.py
# Program that computes the sum of two amounts inputed in cents by the user and produces an output in Euro, printing the following message:
# "The sum of these amounts is € (sum)."
# Author: Anna Lozenko

def sum_amounts():
    try:
        # Input amounts in cents
        amount1 = int(input("Enter the first amount (in cent):"))
        amount2 = int(input("Enter the second amount (in cent):"))
    except ValueError: # validate that the amounts entered are in cents and integer numbers 
        print("Error! Please enter a valid amount (in cent).")
        exit()
    # Compute the sum in euros
    sum = (amount1 + amount2) / 100

    # Output the result
    print(f"The sum of these amounts is € {sum:.2f}.")  # result formatted to 2 decimal places

sum_amounts()