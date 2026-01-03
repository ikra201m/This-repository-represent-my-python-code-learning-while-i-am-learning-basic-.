# # # #dictionary and set in pair word and meaning
# # # # dic={
# # # #     "key" : "value",
# # # #     "name" : "ikram",
# # # #     "learning" : "coding",
# # # # }
# # # # print(dic)

# # # dic={
# # #     "name" : "ikram",
# # #     "learning" : "coding",
# # #     "is_adult": True,
# # #     "university" : "Dhaka university",
# # #     "marks" : 3.75,
# # #     12 : 5.00,
# # #     "family" :["father","mother","sister"],
# # #     "friends" : ("rana","maruf","abir","ratul"),
# # # }
# # # print(dic)
# # # print(type(dic)) #there is no order in dictionary its mutable dont allow dupplicate keys


# # # info={
# # #     "name" : "ikram",
# # #     "learning" : "coding",
# # #     "is_adult": True,
# # #     "university" : "Dhaka university",
# # #     "marks" : 3.75,
# # #     12 : 5.00,
# # #     "family" :["father","mother","sister"],
# # #     "friends" : ("rana","maruf","abir","ratul"),
# # # }
# # # print(info["name"])
# # # print(info["marks"])
# # # info["name"] = "ikram" 
# # # print(info)

# # # null_dic={}
# # # print(null_dic)

# # #nested dic

# # student ={
# #     "name" : "ikram",
# #     "subject" : {
# #         "phy" : 95,
# #         "chem" : 99,
# #         "math" :100,
# #     }
# # }
# # print(student)
# # print(student["subject"])
# # print(student["subject"] ["chem"])
# # print(student.keys())
# # print(list(student.keys()))
# # print(len(list(student.keys())))

# # print(student.values())
# # print(student.items())
# # pairs= list(student.items())
# # print(pairs[0])
# # print(student.get("name")) #no errro
# # student.update({"city" : "delhi"})
# # # new_dict={"city" : "delhi","age" : 2}
# # # student.update(new_dict)
# # # print(student)

# # #set in python
# # # # immutable and unique
# # # collection={1,2,3,4}
# # # print(collection)
# # # print(type(collection))
# # # collection={1,2,3,4 ,"ikram","du","math","math"}
# # # print(collection)
# # # print(type(collection))
# # # collection={} #empty dictionary
# # # collection=set() #empty set
# # # print(collection)
# # # print(type(collection))
# # # collection.add(1)
# # # print(collection)
# # # collection.add(2)
# # # collection.add(2)
# # # print(collection)

# # # collection.remove(2)
# # # collection.add("ikram")
# # # collection.add((1,2,3))
# # # #but we cant add a list 

# # # print(collection)
# # # print(len(collection))
# # # collection.clear()
# # # print(collection)
# # # print(len(collection))

# # collection={"hello","ikram","how","are","u"}
# # print(collection.pop())
# print(collection.pop())
# set1={1,2,3,4,}
# set2={2,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))
# store following word meaning in python in a dictionary
# store the following meaning in dictionary
# problem solve
# dic={
#     "table" :["a piece of furnitur", "list of facts & figure"],
#     "cat" : "a small animal"
# }
# print(dic)

# subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(subject)
# print(len(subject))

# problem wap to enter marks of 3 subject from the user and store them in a dictionary.start with an empty dictionary and add one by one .use subject name as keys and marks as value

# marks={}
# x=int(input("enter phy :"))
# marks.update({"phy" : x})
# x=int(input("enter chem : "))
# marks.update({"chem" : x})
# x=int(input("enter math :"))
# marks.update({"math " : x})
# print(marks)
# figure out a way to store 9 and 9.0 as separate values in the set (you can take help of built in data types)

set={9,9.0}
print(set)
set={9,"9.0"}
print(set)
set={("float",9.0),("int",0)}
print(set)







 

 





