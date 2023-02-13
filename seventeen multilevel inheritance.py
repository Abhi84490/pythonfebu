# class gpc:
#     def __init__(self,name):
#         self.name = name
# class pc(gpc):
#     def __init__(self, name, age):
#         super().__init__(age)
#         self.age = age
# class cc:
#     def __init__(self,sal):
#         self.sal=sal
# p = pc('abhi',234)
# # p.age()
# print(p.name)

# gpc---->
# class gpc:
#     def __init__(self, name):
#         self.name = name
#
#
# class pc(gpc):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#
# class cc:
#     def __init__(self, sal):
#         self.sal = sal
#
#
# p = pc("abh", 22)
# print(p.name)


# pc------>cc
# class gpc:
#     def __init__(self,name):
#         self.name=name
#
# class pc:
#     def __init__(self,age):
#         # super().__init__(name)
#         self.age = age
#
# class cc:
#     def __init__(self,age,sal):
#         super().__init__(age)
#         self.sal = sal
#
# p=cc(98,0)
# p.age
# print(p.age)

# pc----->cc

# class gpc:
#     def __init__(self,name):
#         self.name=name
#
# class pc:
#     def __init__(self, age):
#         self.age= age
#
# class cc(pc):
#     def __init__(self,age,sal):
#         super().__init__(age)
#         self.sal=sal
#
# p= cc(23,7777)
# print(p.age)

# gpc---->pc----->cc
# class gpc:
#     def __init__(self,name):
#         self.name= name
#
# class pc(gpc):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age= age
#
# class cc(pc):
#     def __init(self,name,age,sal):
#         super().__init__(name,age)
#         self.sal= sal
#
# p =cc('abhi', 22, 23324)
# print(p.name)


# wap ot perform multilevel inheritance and try to get attributes of each class
class first():
    def __init__(self,name):
        self.name= name
class second(first):
    def __init__(self,name,age):
        super().__init__(name)
        self.age= age
class third(second):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks= marks

c=third('abhi',33,43434)
print(c.name)
# wap to make a 3 class which one of the clas is totally empty and also try to inherit the attribut of each class