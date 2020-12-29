"""While Loop"""
# i = 0 #start
# while i<5: #condition
#     print(i)
#     i += 1 #i=i+1
# print (i)

"""for loop"""
#    "odd numbers in 1 to 20"
# for i in range(1,20,2):
#     print(i)

#    "odd numbers in reverse order"
# for i in range(19,0,-2):
#     print(i)

#   Q1. Sum of n natural numbers
# n = int(input("Enter a natural number : "))
# s = 0
# for i in range(1, n+1):
#     s+=i
# print("Sum of natural numbers from 1 to n = ", s)

#   Q2. Sum of n natural numbers
# n = int(input("Enter a natural number : "))
# f = 1
# for i in range(1, n+1):
#     f*=i
# print("Factorial of n = ", f)

#   "Swapping two numbers"
# n = int(input("Enter a natural number : "))
# m = int(input("Enter a natural number : "))
# print("The two numbers are ")
# print(n, " ", m)
# n, m = m, n
# print("On swapping, ")
# print(n, "", m)

"""Pattern"""
#   "Star pattern"
# n =int(input("Enter number : "))
# for i in range(n):
#     for j in range(n):
#         print('* ', end = ' ')
#     print()

#using string manipulation:
# n =int(input("Enter number : "))
# for i in range(n):
#     print('* '*n)

"""Break and continue statements"""
# for i in range(10):
#     if i%2==0:
#         continue #loop skipping
#     if i==7:
#         break
#     print(i)

#   Q2.Prime number check
# n = int(input("Enter a natural number : "))
# flag = 0
# for i in range(2,n):
#     if n%i==0:
#         flag = 1
#         print("Sorry not a prime number")
#         break
# if flag==0:
#     print("Prime number!")

#   Q3.Prime number in a range
# n = int(input("Enter a natural number : "))
# flag = 0
# for i in range(2,n):
#     if n%i==0:
#         flag = 1
#         print("Sorry not a prime number")
#         break
# if flag==0:
#     print("Prime number!")

"""
strip() : removes the starting and endind white spaces
split() : splits the string on the  basis of character provided
"""
#s = ' today is a good day!! '
# s = '1234'
# print(s)
# print(s.strip())
# print(s.strip().split('y'))

# n = s.strip().split()
# for i in range(len(n)):
#     n[i] = int(n[i])
# x = n[0]
# ans=eval(s)==n[1]
# print(ans)

