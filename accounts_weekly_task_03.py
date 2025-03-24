# accounts.py 
# program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: Anna Lozenko


def account_output (account_number:str):
    masked_number = f"xxxxxx{account_number[-4:]}"
    print(masked_number)

account_number = input("Please enter the 10 digit account number: ")

account_output(account_number) 


