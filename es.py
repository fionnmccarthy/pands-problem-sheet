# es.py
# Weekly Task 07.
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# author: Fionn McCarthy - G00301126.

# As it was not speciifed I counted the number of e's and E's within the text file. 

filename = str(input("Please enter the name of the text file:")) # this line instructs the user to input the name of the text file

with open(filename, "r") as f:  #this line opens the file inputted (filename) in read mode ("r")
    filedata = f.read() #read() reads the file and returns the specified number of bytes in the file 
    letter_count = filedata.count("e") + filedata.count("E") #count() counts the number of e's in the data that was read from the file
    print(letter_count) 


# References 
# http://textfiles.com/stories/psf.txt text file source accessed on 11/03/2021
# https://www.w3schools.com/python/ref_file_read.asp read() on 11/03/2021
# https://www.w3schools.com/python/ref_list_count.asp count() on 11/03/2021

