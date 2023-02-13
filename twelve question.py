# a=[1,2,3]
# b=a*2
# print(b)

# wap to print all prime number range 10-50

# lower=10
# upper =50
# print('prime number between', lower, 'and', upper , "are")
# for num in range (lower, upper+1):
#     if num>1:
#         for i in range (2,num):
#             if (num%i)==0:
#                 break
#             else:
#                 print(num)

# num=int(input("enter the number: "))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime number")
#             break
#         else:
#             print('prime number', num)
#     # for 1
# else:
#     print("not prime number", num)





                                         # lcm program

# x=45
# y=95
#
# # choose the greatest number
# if x>y:
#     greater = x
# else:
#     greater =y
#    # ture for infinite loop
# while True:
#     if greater % x==0 and greater % y==0:
#         print(lcm)
#         lcm = greater
#         break
#         greater = greater+1
# print(lcm)


# revers number program
num=1234
rev_num=0
while num!=0:
    digit = num%10
    rev_num = rev_num*10+digit
    num//=10

print(rev_num)


# wap to print fizz and buzz, if a number is divisible bu 3 print fizz .
# if a number is dibisible by 5 print buzz and of divisible by both print fizz buzz
# if not divisible by any one print -1 or divisible by 2 print even or divisible by 3 but not by 2 & 5 print odd.
