new_list = ['a', 'b', 'c', 0 , 1, 2]
            #0    1    2   3   4  5
            #-6   -5   -4  -3  -2  -1  here because 0 doesn't have - value in maths  

print(new_list[1])
print(new_list[-2]) #COUNT FROM BACKWARDS
print(new_list[1:3]) #start:stop
new_list[0] = 'z'#re-assigning value
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5] #add 5 to the my_list
my_list[0] = 'z' 
print(my_list)
print(bonus)