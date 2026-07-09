# # method overriding
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class cat(Animal):
#     def sound(self):
#         print("Cat meows")
# animals=[Animal(), Dog(), cat()]
# for animal in animals:
#     animal.sound()

# method overloading with default values
def add(a,b=0,c=0):
    return a+b+c
print("add(5):",add(5))
print("add(5,10):",add(5,10))
print("add(5,10,15):",add(5,10,15))

# method overriding(Run-time polymorphism)
class student:
    def display(self,name,age,marks,result): # method is overriden and child class is printed
        print("student details")
class result(student):
    def display(self, name, age, marks, result):
        print("Name:",name)
        print("Age:",age)
        print("Marks:",marks)
        print("Result:",result)
res=result()
res.display("Ravi",20,75,"pass")

#method overloading-it uses default values as arguments
def greet(name="keerthi"): # default value if value was not passed 
    print("Hello",name)
greet("ravi")