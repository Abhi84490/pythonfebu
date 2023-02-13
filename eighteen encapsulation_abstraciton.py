# #                                                             # encapsulation ----->
# # # hide data through the user
# # # 1.public
# # # class std:
# # #     def __init__(self,name,age):
# # #         self.name=name
# # #         self.age= age
# # # s=std('abhi', 22)
# # # print(s.name)
# #
# #
# # # 2.private
# # class std:
# #     def __info(self,name,age):
# #         #private
# #         return name, age
# #
# #     def details(self,greet):
# #         #public
# #         return greet
# # s=std()
# # print(s.details('hello'))
# # # s.info("abhi", 23)
# #
# # # 3.protected
# #
# #
# #
# # wap to perform encapsulation where you have to find the marks of 2 student if any one of the student is going to fail in any
# # subject then you have hide the data of the subject.
# # std1=int(input("enter the marks of first: "))
# # std2 =int(input("enter the marks of second"))
# # class s1:
# #     def __init__(self,__x,y):
# #         self.x=__x
# #         self.y=y
# # class s2(s1):
# #     def __init__(self,x,y):
# #         super().__init__(x,y)
# #
# # s=s2(34,53)
# # print(s.x)
#
#
#
# # public , private, protected
# #
# # class a:
# #     # public
# #     def x(self, greet):
# #         return greet
# #     # private
# #     def __y(self, name):
# #         return name
# #     # protected
# #     def _z(self, age):
# #         return age
# #
# # c= a()
# # # print(c.x('hello'))
# # print(c.y('arav'))
# # # print(c.z(22))
#
#
# # wap to find the output of the inheritance clas where 2 classes are defined such a
# # mannner that each one is having some access modifires to ger the output.
#
#
#
# # wap to get the score of 2 player if the player is not able to make run then dont show the data
# # in the output
# # class player1():
# #     def __init__(self,name, run):
# #         self.name= name
# #         self.run= run
# #
# # class player2(player1):
# #     def __init__(self,name,run):
# #         super().__init__(name,run)
# #
# #
# # p= player2('abhi', 56)
# # p=player2('varun',0)
# # print(p.player1)
#
#
#                                 # polymorphism
# # overloading
# # overriding
#
#
# # a=1
# # b=2
# # c=a+b
# # print(c)
# #
# # a="1"
# # b="2"
# # c=a+b
# # print(c)
#
#
# # function overloading
#
# # default arg
#
# # def fun(x,y):
# #     z=x+y
# #     return z;
# # fun(1,2)
# #
# # class std:
# #     def __init__(self,name, age):
# #         self.name= name
# #         self.age= age
# #
# # s = std('s', 678)
# # print(s.name)
#
#
#
# #inheritance----->
#
# class emp:
#     def __init__(self,name, age):
#         self.name= name
#         self.age= age
# class emp2(emp):
#     def __init__(self,name,age,sal):
#         super().__init__(name, age)
#         self.sla=sal
#
# e= emp2('aks',43,344)
# print(e.name)
#


class one:
    def __init__(self,x):
        self.x= x

class two:
    def __init__(self,y):
        self.y= y
class three(one,two):
    def __init__(self,x,y,z):
        # super().__init__(x)
        # super().__init__(y)
        one.__init__(self,x)
        two.__init__(self,y)
# super method only run time
        self.z=z

a=three(2,3,4)
print(a.x)
print(a.y)
print(a.z)


# ABSRRACTION ------> DATA HIDE
from abc import ABC, abstractmethod

# encapsulation ------>data hide1


class one():
    pass
class two():
    def fun2(self):
        print("func 2 is class 2")
    # def __init__(self,name):
    #     self.name=name

class three():
    def fun3(self):
        print("func 3 in class 3")

    # def __init__(self,age):
    #     self.age=age

class foru():
    def fun4(self):
        print("func 4 in class 4")
    # def __init__(self,sal):
    #     self.sal= sal