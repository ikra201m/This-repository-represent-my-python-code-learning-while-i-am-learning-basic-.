# #function
# a=5
# b=10
# sum= a+b
# print(sum)
#reduntant mean repeat
# def calsum(a,b):
#     sum=a+b 
#     print(sum) 
#     return sum
# calsum(2,10)
# calsum(5,6)

# def fun(a,b):  #a,b parametr
#     prod=a*b
#     return prod

# print(fun(4,5))  #function call

# def hello_print():
#     print("hello")

# hello_print()

# avaerage of 3 number
# def avg(a,b,c):
#     average= (a+b+c)/3
#     print(avg)
#     return average

# print(avg(1,2,3))
#built in functio print
# print("ikram " ,end= "&")
# print("hossain")
#len type range 
# user defined
#
# wap ro print the length of a list (list is the parameter)

# cities=["dhaka","khulna","rajsahi","chandpur"]
# course=["real","complex","ode","abstract","linear"]
# def call(list):
#     print(len(list))

# call(cities)
# call(course)
#wap to print the element of a list in a single line(line is the parameter)

# cities=["dhaka","khulna","rajsahi","chandpur"]
# def call(list):
#     for item in list:
#         print(item ,end=" ")

# print(call(cities))
# print()
#wap to find the factorial of n
# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


# def call(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#         print(fact)

# call(5)
# wap to conver usd to taka

# def converter(usd_value):
#     for i in range(1,usd_value+1):
#         bdt_taka=120*i
#         print(bdt_taka)

# converter(4)

# def converter(usd_value):
#     bdt_taka=usd_value*120
#     print(usd_value, "USD = ", bdt_taka ,"TAKA")

# converter(3)

# def declar(n):
#     if(n%2==True):
#         print("EVEN")
#     else:
#         print("ODD")

# declar(4) # ekto vul ase if e 

#recursion 
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5) recursive function
#calculate fact of n
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#          return fact(n-1)*n
    
# print(fact(4))

#wa recursive function to calculate the sum of first n natural number
# def calsum(n):
#     if(n==0):
#         return 0
#     return calsum(n-1)+n

# print(calsum(5))

#write a recursive function to print all element of a list(use list and index as paramater)
cities=["dhaka","khulna","rajsahi","chandpur"]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list(cities)




   











