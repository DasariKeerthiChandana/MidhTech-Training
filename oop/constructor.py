# constructor is special method that runs automatically called when object is created

class student:
    def __init__(self, name, age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print("Name:",self.name)
        print("Age:", self.age)
        print("Place:",self.place)
s1=student("Keerthi",22,"Hyderabad")
s1.display()
s2=student("Ravi",25,"Nellore")
s2.display()
        