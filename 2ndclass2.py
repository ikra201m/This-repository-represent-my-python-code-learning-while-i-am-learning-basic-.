#wap to check if a number entered by the user is odd or even
n=int(input("enter a number :"))
rem=n % 2
if(rem==0):
     print("n is even")
else:
     print("odd")

#wap to find the greatest of 3 number entered by the user
a=int(input("enter a number :"))
b=int(input("enter 2nd  :"))
c=int(input("enter 3rd number"))
if(a>=b and a>=c):
    print("greater is :",a)
elif(b>=c):
    print("2nd is largest",b)
else:
    print("big is",c)


#wap that a number is multiple of seven

x=int(input("enter a number"))
rem= x % 7
if(rem==0):
    print("number is 7 multiple")
else:
    print("not")


