def welcome_message():
    print("Welcome to python class")
welcome_message()

# prime number

def is_prime():
    num=int(input("enter number"))
    if num <= 1:
        return 
    for i in range(2,num):
        if num%i==0:
            print("Not prime")
            return
    print("prime")
is_prime()

# def prime(n):
#     count = 0

#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1

#     if count == 2:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")

# num = int(input("Enter a number: "))
# prime(num)


# using arguments

def student_details(name,course):
    print("name: ", name)
    print("course:", course)
student_details("Keerthi","python")
student_details("susmitha","Java")

# Return gives a value back

def add(a,b):
    return a+b
print("Addition:",add(10,20))

def sub(a,b):
    return a-b
print("subtraction:",sub(30,20))

def mul(a,b):
    return a*b
print("Multiplication:",mul(10,20))

def div(a,b):
    return a/b
print("Division:",div(40,20))

# prime using parameter and return

def is_prime(num):
    if num <= 1:
        return "Not prime"
    for i in range(2,num):
        if num%i==0:
            return "Not prime"
    return "prime"
print(is_prime(1))


# Recursion: Calling function again and again in function itself

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print("Factorial of 5:",factorial(5))