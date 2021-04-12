# es.py
# Weekly Task 07.
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# author: Fionn McCarthy - G00301126.

# Input: python es.py psf.txt


import sys #import sys module to take an argument on teh command line
filename = sys.argv[1] # takes the first command line argument 

with open(filename, "r") as f:  #this line opens the file inputted (filename) in read mode ("r")
    filedata = f.read() #read() reads the file and returns the specified number of bytes in the file 
    print(filedata.count('e')) #count() counts the number of e's in the data that was read from the file

# Output: 526


# References 
# http://textfiles.com/stories/psf.txt text file source accessed on 11/03/2021
# https://www.w3schools.com/python/ref_file_read.asp read() on 11/03/2021
# https://www.w3schools.com/python/ref_list_count.asp count() on 11/03/2021
# https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python file on command line 01/04/2021

