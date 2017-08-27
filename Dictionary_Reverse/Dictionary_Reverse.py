#Date: Aug 19,2017
#Project Name: Reverse dictionary
#Author: Olga Lazarenko
#Description: the program contains a finction reverse_dict(dict)that has dict keys
            #and values swapped, the values are not repeated in the initial dictionary


print()
print('call the finction dictionary_reverse(dict) to reverse a dictionary')
print()
dict_reversed={}#define the variable dict_reversed, dictionary type
dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
def dictionary_reverse(dict):# dict is the input dictionary from the user
    print('the input dictionary:')
    print(dict)
    print('--------------------------------------------------')

    dict_reversed={}#define the variable dict_reversed, dictionary type


    list_keys=[]#define the list to store the dict keys values
    list_values=[]#define the list to store the dict values 

    list_keys = list(dict.keys())#populate the list of keys values
    list_values = list(dict.values())#populate the list of values 

    print()
    print('keys list: ', list_keys)# just print the list of keys values for  demonstration  
    print('values list: ',list_values)#just print the list of  values for  demonstration
    print()
    print('now we will swap keys and values for the reversed dictionary')
    print('attention! The order mignt not to be maintained')
    print()


    n=0

    while n< len(list_keys):# we wil populate the dict_reversed with the reversed keys and valuse
                            #from the initial dictionary
                            #we use while loop
    
        new_key=list_values[n]# assign the values from the initial dictionary to keys of the dict_reversed
        new_value = list_keys[n]# assign the key from the initial dictionary to values of the dict_reversed
    
    
        dict_reversed[new_key]= new_value#populate the reversed dictionary (dict_reversed)
        n+=1

    print(' ~ Output ~ ')
    print('the reversed dictionary: ')
    return(dict_reversed)#print the result 


