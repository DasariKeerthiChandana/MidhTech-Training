# K
row=int(input("enter no of rows:"))
col=int(input("Enter no of coloumns:"))
mid=row//2
for i in range(row):
    for j in range(col):
        if j==0 or (i+j==mid ) or (i-j==mid):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# E
row=int(input("enter no of rows:"))
col=int(input("Enter no of coloumns:"))
for i in range(row):
    for j in range(col):
        if (i==0) or (j==0) or (i==2) or (i==4):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()
# E
row=int(input("enter no of rows:"))
col=int(input("Enter no of coloumns:"))
for i in range(row):
    for j in range(col):
        if (i==0) or (j==0) or (i==2) or (i==4):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()

# R
row=6
col=6
for i in range(row):
    for j in range(col):
        if (i==0) or (j==0) or (i==2) or (i==1 and j==5) or (i==3 and j==1) or (i==4 and j==3) or (i==5 and j==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# T
row=5
col=5
for i in range(row):
    for j in range(col):
        if (i==0) or (j==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# H
row=5
col=5
for i in range(row):
    for j in range(col):
        if (j==0) or (j==4) or (i==2):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# I
row=5
col=5
for i in range(row):
    for j in range(col):
        if (i==0) or (i==4) or (j==2):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


