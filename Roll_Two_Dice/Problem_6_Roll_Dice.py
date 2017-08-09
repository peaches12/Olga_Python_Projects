
import random



print('*************************')
print('Project Name:    Dice Game')
print('Author:          Olga Lazarenko')
print('Date:            Aug 5,2017')
print('Description:     The program will simulate rolling two 6-sided dices 1000 times')
print('                 and keep track of how many times each sum occurs,')
print('                 and  print out a table of occurences/counts of totals')
print('                 (can be from 2 to 12)')
print('*************************')

print()


list_total=[]
roll=1
while roll <= 1000:
    dice1 = random.randint(1,12)
    dice2 = random.randint(1,12)
    
    total = int()
    total = dice1+dice2
    
    list_total.append(total)
    roll = roll + 1

list_count=[]
list_rolls=[]
count = int()
for i in range(2,13):
    list_rolls.append(i)
    count=list_total.count(i)
    list_count.append(count)

print('rolls: ', list_rolls)
print('counts: ', list_count)
print()
print('Roll\tOccurence ')
print('_ _ _  _ _ _ _ _ ')
n=0
while n<len(list_rolls):
    
    print(list_rolls[n],'\t',list_count[n])
    
    n+=1
print()
print('~  game is over  ~')


    






                       
