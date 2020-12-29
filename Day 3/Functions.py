"""
Functions

def fun_name(p1,p2,...) :
    statements
    return
"""

    #Function to print hello world
# def hello_world:
#     print("Hello, World")
# hello_world()

    #function to welcome a user
# def hello_user(username):
#     print("Hello, " + username)
# hello_user('ABC')

    #function to find factorial(n):
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact

print(factorial(2))