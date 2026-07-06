a=20
b=50
c=10
print(max(a,b,c))
print(min(a,b,c))

# if-else
a=20
b=80
c=70
if a>b:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

# if-elif
marks=int(input("Enter marks"))
if marks>=90:
    grade="A"
elif marks>=75:
    grade="B"
elif marks>=60:
    grade="C"
else:
    grade="Need improvement"
print("Grade:",grade)

# Nested if
age=19
citizen=True
if age>=18:
    if citizen:
        print("Allowed to vote")
    else:
        print("Citizenship required")
else:
    print("Age should be above 18")

# calculator
operator=input("select your operator '+,-,*,/' :")
n1=float(input("enter num 1:"))
n2=float(input("enter num 2:"))
if operator=='+':
    n=n1+n2
    print(n)
elif operator=='-':
    n=n1-n2
    print(n)
elif operator=='*':
    n=n1*n2
    print(n)
elif operator=='/':
    n=n1/n2
    print(n)
else:
    print("operator is not valid")


