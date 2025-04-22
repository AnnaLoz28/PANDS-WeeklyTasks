# bank.py
# Program that computes the sum of two amounts inputed in cents by the user and produces an output in Euro, printing the following message:
# "The sum of these amounts is € (sum)."
# Author: Anna Lozenko

amount1 = int(input("Enter the first amount (in cent):"))
amount2 = int(input("Enter the second amount (in cent):"))

sum = (amount1 +  amount2)/100 

print (f"The sum of these amounts is € {sum}.")
