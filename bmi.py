# BMI.py
# Weely Task 02
# This program calcluates a person's Body Mass Index (BMI) by inputting height(cm) and weigh(kg). 
# author: Fionn McCarthy

# we must convert the the input to an integer
weight = int(input('please enter weight(kg):'))
height = int(input('please enter height(cm):'))

#we must get convert height to metres and square it and input this variable into formula 
heightinmetressquared = float((height /100)**2)
newNumber = float(weight / heightinmetressquared)

#print BMI to 2 decimal places 
print ('BMI is {:.2f}.'.format(newNumber))