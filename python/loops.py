# for loop
for i in range(1,11):
    if i==5 or i==6:
        break
    print(i)

for i in range(1,11):
    if i==5 or i==6:
        continue
    print(i)
# for loop with list
students=["Alice","bob","charlie"]
print("loop with list",students)
for student in students:
    print("Welcome",student)

#while loop
count=10
while count>=0:
    print("count:",count)
    count-=1


seconds=5
while seconds>0:
    print("Timer:",seconds)
    seconds-=1 
print("Timer finished")


food = input("Enter your food item (Press 'q' to quit): ")
while not food=="q":
    print("You like", food)
    food = input("Enter your food item (Press 'q' to quit): ")
print("Thank you!")
feedback = int(input("Enter feedback b/w (1-10): "))
while feedback < 1 or feedback > 10:
    print(f"{feedback} is invalid")
    feedback = int(input("Enter feedback b/w (1-10): "))
print("You gave feedback:", feedback)

# to print row*col using symbol
row=int(input("Enter the no of rows:"))
col=int(input("Enter the no of coloumns:"))
symbol=input("Enter symbol:")
for i in range(row):
    for j in range(col):
        print(symbol,end="")
    print()
# Dialpad
n=1
for i in range(3):
    for j in range(3):
        print(n,end=" ")
        n+=1
    print()
print("* 0 #")
