# average from marks list
student_marks=[70,80,95]
total=sum(student_marks)
average=total/len(student_marks)
print("average marks: ", average)

# List Methods
List=[10,20,30]
List.append(70)
print(List)
List.extend([10,80,90])
print(List)
List.insert(2,25)
print(List)
List.remove(20)
print(List)
List.pop(3)
print(List.index(90))

print(List.count(10))

List.sort()
print(List)
List.reverse()
print(List)
copy_list=List.copy()
print(copy_list)
List.clear()
print(List)
