# str1="this is a string."
# str2='apnacollege'
# str3="""this is a string"""

# # we can use single/double /triple 
# print(str1)

str5="this is a string .\nwe are creating python"
print(str5)
#\n for 2nd line and \t for tab
#concetation (2 str sum)
str1="apna"
str2="college"
print(str1+str2)
print(len(str1))
#it also count secial caracter and also space

#indexing give value of every position of str
str="apna college"
ch=str[0]
print(ch)
print(str[0])
#slicing str er tokra kora
print(str[1:5])
print(str[5:12])
print(str[5:])
print(str[2:len(str)])
str="apple"
print(str[-5:])
#string function
str="i am studying python from apna college"
print(str.endswith("ege"))
print(str.endswith("pp"))
print(str.capitalize())
str=str.capitalize()
print(str.replace("o","a"))
print(str.replace("python","java"))
print(str.find("o")) # ei latter ta ache oi word er index bole dey
print(str.count("o"))
print(str.count("Q"))
#practise
#wap to input users first name and print its length




# name=input("enter a name :")
# print("length of my name is :",len(name))

# wap to find the occurance of $ in a string



doller="if ikram have 500 $ then he can buy a iphone by 600$ and 100 $ is loan"
print(doller.count("$"))

#conditional statement (if else elif)

age=24
if(age >= 18):
        print("can vote and apply for licence")
        print("can drive")

light="green" 
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("loo")

num=5
if(num>2):
     print("greater than 2")
elif(num>3):
     print("greater 3")

     
light="pink" 
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("loo")
else:
     print("light is broken") #indentation (proper spacing)


marks=int(input("enter student marks :"))
if(marks >= 90):
    grade="A"
elif(marks  >=80 and marks <90):
    grade="B"
elif(marks>=70 and marks <80):
     grade="C"
else:
     grade="D"
print("Grade of the studet is ", grade)








