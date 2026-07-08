student={"name":"Keerthi","age":20}
print(student["name"])

student_record={"name":"Pradeep","marks":75}
student_record["marks"]=98
student_record["grade"]="A+"
print("Student record:",student_record)

employee={"id":101,"name":"Rahul","department":"IT","salary":50000}
print("Employee Details:",employee)
print("Employee name:",employee["name"])
employee["city"]="Hyderabad"
print("After adding city:")
print(employee)
employee["salary"]=55000
print("After updating salary:")
print(employee)