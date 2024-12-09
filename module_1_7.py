immutable_var = (1,24.3245,'a',True)
print('Immutable tuple:',immutable_var)
immutable_var2 = (1,[24.3245,4566,567],'a',True)
#immutable_var2[0][1] = 1 #Нельзя изменить так как часть не изменяемого списка
print('Immutable tuple2:',immutable_var2)
immutable_var2[1][0] = 1
print('Immutable tuple2:',immutable_var2)
mutable_list = [1,24.3245,'a',True]
print('Mutable list:',mutable_list)
mutable_list[1] = 2
print('Mutable list:',mutable_list)