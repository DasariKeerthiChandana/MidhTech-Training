numbers=[1,2,3]
print("example:",list(map(lambda x:x*2,numbers)))

marks=[70,80,90]
bonus_marks=list(filter(lambda mark:mark>=35,marks))
print("marks:",bonus_marks)