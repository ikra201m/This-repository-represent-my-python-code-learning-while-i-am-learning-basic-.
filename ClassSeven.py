#file i/o input and output
#text file .txt ,.docx,.log etc
#binary files .mp4 .mov .png .jpeg ect
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()
# f=open("demo.txt","r")
# data=f.read(6)  # 6 dewa mane first 6 ta letter pora
# print(data)
# f.close()
# f=open("demo.txt","r")
# line1=f.readline()  # read line one line at a time
# print(line1)
# f.close()
# 
# f=open("demo.txt","r")
# line1=f.readline()  # read line one line at a time
# print(line1)
# line2=f.readline()  # read line one line at a time
# print(line2)
# line3=f.readline()  # read line one line at a time
# print(line3)
# f.close()
# writinig to a file
# f=open("demo.txt","w")
# f.write("i go to my lab tommorow")
# f.close()
# f=open("demo.txt","a")
# f.write("\ni go to my lab tommorow,hurrah")
# f.close()
# f=open("sample.txt","w")
# f.write("\ni go to my lab tommorow,hurrah")
# f.close()

# f=open("demo.txt","r+")
# f.write("abc")
# f.close

# r+ read +overwrite (pointer start ) no truncate
#w+ read + overwrite truncate
# a+ read+append (pointer end ) no truncate

#with syntax

# with open("sample.txt","r") as f:
#     data=f.read()
#     print(data)
# with open("sample.txt","w") as f:
#     data=f.write("new data")

#deleting a file
    #using the os module 
#module like a code library is a file written by another programmer that genarally has a function we can use 
# import os 
# os.remove("sample.txt")
#qs
with open("practice.txt","w") as f:
    f.write("hi every one \n we are learning python file i\o \n using java  \n i like program")