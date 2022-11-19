#python program to get fibonacci series between 0 to 50
# first_num,second_num=0,1
# while second_num<50:
#     print( second_num,end=',')
    # first_num,second_num=second_num,first_num+second_num



#python program to reverse a word entered by the user.
#using negative indexing

# word=input("enter a word/string")
# reverse= word[::-1]
# print(reverse)


#program to count the no. of even and odd numbers from a series of numbers.
numbers= (1,2,5,4,7,8,12,18,19,6,9,13)
count_odd=0
count_even=0
for i in numbers:
    if i % 2==0:
        count_even+=1
    else:
        count_odd+=1
print("even numbers in series",count_even)
print("odd numbers in series",count_odd)
