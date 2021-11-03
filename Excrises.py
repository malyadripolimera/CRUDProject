#list = [1, 2, 3]

#list[-1]

#glo=5

    #s = ''
    #for j in range(i):
    #    s = s+str(i)
    #print(s)
    #print(i*str(i))
#import sys

#sys.exit()

# 1.Add two numbers
#a = int(input("enter number:"))
#b = int(input("enter number:"))

#sum = a+b

#print(sum)

#2.Print Hello world

#print("Hello World")

#3.Check prime number or not from web site

# num = 9
#
# if num > 1:
#  for i in range(2, num):
#     if (num % i) == 0:
#         print(num, "is not prime number")
#         print(i, "times", num//i, "is", num)
#         break
#     else:
#         print(num,"is prime number")
# else:
#     print(num,"not prime number")

#(or) Check prime number Excellent
#
# num = int(input("enter number:"))
#
# if num > 1:
#     if (num % 3) == 0:
#        print(num," is not prime number")
#     else:
#         print(num," is prime number")

#4.Find Factorial Number

#num = int(input("enter number:"))
#num = 5

#factorial = 1

#if num < 0:
 #   print("negative number")
#elif num == 0:
 #   print("factorial zero")
#else:
#for i in range(1, num+1):
#       factorial = factorial * i
 #      print("The Factorial of",num,"is",factorial)

#5.Simple Calculator

#def add(x, y):
 #   return x+y
#def subtract(x, y):
  #  return x-y
#def multiply(x, y):
 #   return x*y
#def division(x, y):
 #   return x/y

#print("select option:")
#print("1.add")
#print("2.subtract")
#print("3.multiply")
#print("4.division")

#choice = input("Enter choice:")
#num1 = int(input("enter 1st number:"))
#num2 = int(input("enter 2nd number:"))

#if choice == '1':
 #   print(num1,"+",num2,"=", add(num1,num2))
#elif choice == '2':
 #   print(num1,"-",num2,"=",subtract(num1,num2))
#elif choice == '3':
 #   print(num1,"*",num2,"=",multiply(num1,num2))
#elif choice == '4':
 #   print(num1,"/",num2,"=",division(num1,num2))
#else:
 #   print("invalid input")

## febnoic squence

 #n = int(input("Enter how many numbers you want in series:"))
 #first = 0
 #second = 1

 #for i in range(n):
  #   print(first)
   #  temp = first
    # first = second
     #second = temp+second

## prime number checking

#num = int(input("Enter number:"))
#prime =True
#for i in range(2,num):
 #   if (num%i) == 0:
  #     prime=False
   #     break
#print("%d is %s number" %(num, prime and 'a prime' or 'not a prime'))# turnator function
#print(1 and 'yes' or 'no') # yes
#print(0 and 'yes' or 'no') # no
#print('' and 'yes' or 'no') # no => Empty String is False
#print(' ' and 'yes' or 'no') # yes => Space is true
#print('m' and 'yes' or 'no') # yes
#print([] and 'yes' or 'no') # no
#print([1] and 'yes' or 'no') # yes
#print(() and 'yes' or 'no')  # no
#print((1) and 'yes' or 'no') # yes
#print({} and 'yes' or 'no') # no
#print({1:2} and 'yes' or 'no') # yes
