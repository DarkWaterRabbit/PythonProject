my_dict ={'R1':123,'R2':435,'R3':21424}
print(my_dict)
print('R2 =',my_dict['R2'],my_dict.get('R4','R4 нет'))
my_dict.update({'R4':345, 'R5':545,'R6':36})
print(my_dict)
A =my_dict.pop('R2')
print(A)
print(my_dict)

my_set ={3,34,5,5,5,5,5.5,5.5,6.7,6.7,'D2','D2','D2',True,False,True,False,True,False,True,False}
print(my_set)
my_set.update({23,45,(2345,'Раз')})
print(my_set)
my_set.discard(5)
print(my_set)