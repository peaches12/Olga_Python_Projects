#Date: Aug 1, 2017
#Program Name: Convert Time
#Author: Olga Lazarenko
#Description: the program uses the  function convert_to_seconds(hours,minutes,seconds)
#               to convert the time into seconds

print('to convert the input time into seconds,')
print('call the function convert_to_seconds(hours,minutes,seconds)')
print()
print('---------------------------')

def convert_to_seconds(hours,minutes,seconds):
    #the fuction takes the input in hours, min, seconds from the user
    #and converts to seconds
    print()
    result =hours*60*60+minutes*60+seconds #the formula for conversion
    print('it will be '+ str(result) + ' seconds')
    return







