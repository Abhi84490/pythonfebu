# wap to make a class of simplified airthmetic operation
# and try to get the output of that class through the object

# class arithmetic():
#     def function(self,a,b):
#         add= a+b
#         sub= a-b
#         mul= a*b
#         div= a/b
#         print("add----", add, "sub-----", sub, "mul-----", mul, "div-----", div)
# a=arithmetic()
# print(a.function(3,4))
# a.function(3,4)
# user input
# class airthmetic():
#     def function(self):
#         a= int(input("enter the first number"))
#         b= int(input("enter the second number"))
#         add= a+b
#         sub= a-b
#         mul= a*b
#         div=a/b
#         print("add---",add, "sub---",sub, 'mul----', mul, 'div----',div)
# a= airthmetic()
# # print(a.fuction())
# a.function()



# #wap to make a class of car and find its actual price, if the car is of more than 10 lakh then there is a tax of 14%
# on the car and if the cost of car is less than 10 lakhs then there is some discount of 7.8% on the car. find the actual price of the paid by the user
# price=int(input("enter the car price :"))
class car:
    def info(self,price):

        if price>1000000:
            print(" 14% tax", (price*14)/100)
        elif price<1000000:
            print("7.5% tax",price+ (price*7.5)/100)
        else:
            print("discount")
c= car()
c.info(500000)
