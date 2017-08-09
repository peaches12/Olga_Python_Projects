print('Week 8')
print('Problem 2')
print('Fibonaci number')
print()

N=int(input('Enter an integer of Fibonaci number you want to find: '))
print()
print('call the finction fib_number(N)')

#define a function fib_number():\
fib_list=[]
def fib_number(N):
    #define a list
    fib_list=[]
    fib_list.append(0)
    fib_list.append(1)

    n=N-1
    i=2
    fib_element=int()
    while i <= n:
        fib_element= fib_list[i-1]+fib_list[i-2]
        fib_list.append(fib_element)
        i+=1
    print(fib_list)
    print()

    result=int()
    result = fib_list[n]

    return( str(N)+ 'th  number at Fibonaci list is: ', fib_list[n])






