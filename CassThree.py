#list some type of array 
marks=[94.4, 87.5, 95.2, 66.5,45.1]
print(marks)
print(len(marks))
print(marks[0])
print(marks[2])
student=["karan",95.6,17, "arjun" ]
print(student)
# string immutable(never change)
#list mutable(change)
print(student[0])
student[0]="arjun" 
print(student)
#here is mutable of list
#list silicing
mark=[12, 13,14,15,16]
print(mark[:4])
# print(mark[1:4])
# print(mark[:5])
# print(mark[-3:])
# list=[2,1,3]
# #list.append(4) #append some the 4 last in list
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list=["banana","litchi","apple"]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# ##
list=[2,1,3]
list.insert(1,5)
print(list)
list.remove(1)
print(list)
list.pop(2)
print(list)

#tuples
tup=(1,2,3,4,5)
print(type(tup))
print(tup[0])
print(tup[1])
#tuple also immutable like string
tup=()
print(tup)
print(type(tup))
tup=(1,) #comma na dile etake intger hisbe niye nibe
print(tup)
tup=(1,2,3,4,45)
print(tup[1:3])
print(tup.index(3)) #3 element
print(tup.count(2))
#wap to ask the user to enter a name of their 3 favorite movies and store them in a list
# a=input("first movies")
# b=input("second movies")
# c=input("third movie")
# list=[a,b,c]
# print(list)
#wap to check if a list contains a palindrome of elemennts. palindrome samne se piche se ekoi

list1=[1,2,3,2,1]
list2=[1,2,3,4,5]
copy_list1= list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindromic")
else:
    print("not")

copy_list2=list2.copy()
copy_list2.reverse()
if(copy_list2==list2):
    print("palindrome")
else:
    print("not")

grade=("C","D","A","A","B","B","A")
print(grade.count("A"))
list=["C","D","A","A","B","B","A"]
print(list)
list.sort()
print(list)



 


