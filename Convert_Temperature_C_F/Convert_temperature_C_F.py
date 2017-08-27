# Date: Aug 23,2017
# Project Name: Convert Temperature
# Author: Olga Lazarenko
# Description: the program contains two functions:
#               the function to_c(temp) converts the temperature rom F to C
#               the function to_f(temp) converst the temperature from C to F


print('to convert from F to C call the function to_c(temp)')
print('to convert from C to F call the function to_f(temp)')
print()

def to_c(temp):
    '''to_c(temp) -> str
    this function converts the temperature from F to C,
    temp is the input temperature value from the user '''
    
    C =5/9*(temp-32)   #the formula to caluclate 
    C=round(C,1)        #we want the result with one decimal number
    print(str(temp)+'F will be '+str(C)+'C')#the result of calculation will be returned from the function
    return 

def to_f(temp):
    ''' to_f(temp)--> str
    function converts the temperature from C to F
   temp is the input temperature values from the user '''

    F = 32+5/9*(temp)   # the formula to calculate 
    F=round(F,1)        # the result will we rounded to one decimal number
    print(str(temp)+'C  will be '+str(F)+ 'F')#the result is retured from the function
    return 



