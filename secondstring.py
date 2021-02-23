# secondstring.py
# Weekly Task 03.
# This program asks a user to input a string and outputs every second letter in reverse order. 
# author: Fionn McCarthy - G00301126.

# The input function is used below in order to get the user to ednter a sentence.
input_string = input('Please enter a sentence:')

# From research I gathered teh formula used here for string slicing is - str_object[start_pos:end_pos:step].
# As we want the full length of the string we do no enter the 'start_pos' or the 'end_pos' as we will use teh full string.
# The '-' below is used to reverse teh string.
# The '2' is used to print every second letter. 
# Combining the above we now reverse the string and print every second letter. 

print(input_string[::-2])


# https://www.journaldev.com/23584/python-slice-string for the string slicing formula
# https://docs.python.org/3/library/functions.html python built in functions