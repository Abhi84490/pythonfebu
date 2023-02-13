# list mutable or not

# x=[2,3,4,67,'hello', 'python']
# print(x)
#
# # mutable condition
# x[-1]= 'sql'
# print(x)


# x=[2,3,4,67,'hello', 'python']
# # x[-1:-2]= ['naman','chaman']
# x[1:2]= ['naman','chaman'
# ]
# print(x)

# list method
# append
# x=[2,3,4,67,'hello', 'python']
# x.append('mohan')
# print(x)

# index
# x=[2,3,4,67,'hello', 'python']
# x.index('3')
# print(x)

# x=[20,30,40,50,'TARUN', 'lalit']
# x.index('lalit')
# print(x)

# x=[20,40,50,60,'karna','gaurav']
# x.pop(0)
# print(x)

# x=[20,40,50,60,'karna','gaurav']
# x.remove('gaurav')
# print(x)

# x=[20,40,50,60,'karna','gaurav']
# x.index('gaurav')
# print(x)

# x=[20,15,45,6,8,9,24,78]
# x.sort()
# print(x)


# x=[20,15,45,6,8,9,24,78]
# x.sort(reverse=True)
# print(x)

# wap to reverse a list
# x= [1,4,5,7,90]
# print(x[::-1])

# wap to swap a first & last number of the list
# x=[1,2,3,4,5,6,7,8,9]
# x[0],x[-1]= x[-1],x[0]
# print(x)

# wap to find max number in a list?
x=[1,2,3,4,5,6,7,8,9]
max=x[0]
for i in x:
    if i>max:
        max=i
print("greates num" ,max)
#
# # wap; to find min number in a list
# x= [1,2,3,4,5,6,7,8,9]
# min=x[0]
# for i in x:
#     if i<min:
#         min=i
# print("min number",min)
#
# # wap to sum the number present in a list
# # x=[1,2,3,4,5]
# # y=0
# # for i in x:
# #     y=i+y
# #     print(y)
#
# # # wap to print even number in a list
# x=[1,2,3,4,5,6,7,8,9]
# for i in x:
#     if i%2==0:
#         print(i)
#
# # # wap to print odd number in a list
# x=[1,2,3,4,5,6,7,8,9]
# for i in x:
#     if i%2!=0:
#         print(i)

# wap  to find common element in the list
# a=[34,45,89,56]
# b=[67,89,23,90]
#
# a=[34,45,89,56]
# b=[67,89,23,90]
# for i in a:
#     for j in b:
#         if i==j:
#             print("similar element" ,i)
# else:
#         print("not similar")



# odd even + count

# x=[89,90,67,55,62]
# count_even=0
# count_odd=0
# for i in x:
#     if i%2==0:
#         print("even number", i)
#         count_even= count_even+1
#     else:
#         print("odd number",i)
#         count_odd= count_odd +1
#
# print("cont even numver " ,count_even)
# print("count odd number" , count_odd)

# wap to create a single element list
# x= [1]
# count = 0
# print(x)
# count= count+1
# print(count)


# wap to create a empty list
# x=[]
# count=0
# print(type (x),x,count)



                                            # tuple
# x=(1,2,3,4,5,6,7)
# # print(type(x),x)
# # print(x[0:5:2])
#
# # index
# # count
#
# # x.index(1)
# # print(x)
#
# x.count(2)
# print(x.count)


# wap to add a data in a tuple
# x=(1,2,3,4,5,6)
# x.append(7)
# print(x)

# x=(1,2,3,4,5,6)
# b=list(x)
# b.append(23)
# print(b)
# wap to delete the data in a tuple
# wap to add more than one in a list

# x=[56,78,43,567,89,23]
# for i in x:pp
#     y=x.append(56,54,45)
#     print(y)

# x=[56,78,43,567,89,23]
# for i in range():
#     y = x.append(56)
#     print(y)

# a=[1,2,3,4,5,6]
# b=[10,11,12]
# for i in b:
#     a.append(i)
# print(a)


# a=[1,2,3,4,5,6]
# a.extend([13,12,34,54])
# print(a)

                                            # dictionary

# x={'name':"a",
#    "age": 23}
# print(type(x),x)


# wap to make a dict of emp having name, emp_id, & sal.
# emp= {"name": "abhi", "emp_id": 4444, "sal": 23454}
# print(emp['name'])


# wap ot make single element dict
# a={'name':"abhi"}
# print(a)
# # wap to make empty dict
# a={}
# print(a)


                                                # dict method
# clear
# copy
# get
# items
# key
# pop
# update
# values

# emp= {"name": "abhi", "emp_id": 4444, "sal": 23454}
# # emp.keys()
# print(emp.keys())
# print(emp.items())
# print(emp.update("name", "sky"))

# x={'name':"a", "age":23, "sal": 2345343}
# print(x.get(1))
# print(x.get('name'))


# update

# a={'book': 'abc', 'author': "jack"}
# b= {'bookprice': 23453434}
# a.update(b)
# print(a)

# copy
# a={'book': 'abc', 'author': "jack"}
# # b= {'bookprice': 23453434}
# s= a.copy()
# print(s)

                                                       # set
# a={45,68,44352,23451,4132,'abhi', 'barun'}
# print(type(a),a)