a=int(input("Enter sub 1"))
b=int(input("Enter sub 2"))
c=int(input("Enter sub 3"))
d=int(input("Enter sub 4"))
e=int(input("Enter sub 5"))
f=int(input("Enter sub 6"))
total=a+b+c+d+e+f
print(total)
percent=(total/600)*100
print(percent)

# assignment operator
score=10
score+=5
print("score is:",score)

wallet=500
wallet-=120
wallet+=200
print("Final wallet balance:", wallet)

#comparison operator
a=int(input("enter a"))
b=int(input("enter b"))
print("equal", a==b)
print("greater",a>b)
print("lesser",a<b)

age=int(input("Enter age"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Logical operator
attendance=70
fees_paid=True
eligible=attendance>=75 and fees_paid
print("Eligible for exam:",eligible)

#Identity operator
a=["apple","mango","cherry"]
b=["apple","mango","cherry"]
c=b
print(a is b) #False due to different memory locations
print(b is c) #true because object is same that is b

# Membership operator
present=["apple","banana","cherry"]
search="cherry"
print(search in present)

# Bitwise operator
read=1
write=2
execute=3
user_permission=read|write
print("can read: ", bool(user_permission & read))
print("can write:",bool(user_permission | write))
print("can execute:",bool(user_permission & execute))

