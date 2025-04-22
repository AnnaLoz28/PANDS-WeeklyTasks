# count_characters.py
# Program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.
# Author: Anna Lozenko

import sys

def count_characters(file_name, char_to_count):
    try:
        with open (file_name, 'r') as f: # I am assuming that the text file exists and opening it in the read mode
            content = f.read()
            count = content.count(char_to_count)    
        print(f'The file {file_name} contains {count} characters {char_to_count}.')
    except FileNotFoundError: # if the file.txt does not exist, an error should be raised
        print('The file does not exist.')



argument_count = len(sys.argv) # defining the length for the list of arguments 
# contains all arguments passed via command line. At index [0] we have the python script file name, at index [1] we have the file to read.
if argument_count < 2: # should have at least 2 arguments or an error will be raised 
    raise Exception('Incorrect number of arguements passed. Expected 1 argument: file_name')

file_name = sys.argv[1] # defining the argument we want at index [1], i.e. the file_name'

count_characters(file_name, 'e')
