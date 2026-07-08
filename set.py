# set is unordered, duplicates are removed
num={1,2,5,3,6,7,7,8,9,10,11,4}
print(num)


courses=["python","java","DevOps","python","java"]
unique_courses=set(courses) # converted list to set
print(unique_courses)


students={101,102,103,104,105,103}
print("original set:",students)
students.add(106)
print("After adding:",students)
students.remove(101)
print("After Removing:",students)
print("Total students:",len(students))
