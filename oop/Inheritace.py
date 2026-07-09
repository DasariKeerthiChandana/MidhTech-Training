# we use inheritance to reuse existing code, it reduces duplication and makes code easier to maintain 

# hierarchial-one parent,many children
class animal:
    def eat(self):
        print("Animal eats food")
class Dog(animal):
    def bark(self):
        print("Dog barks")
class cat(animal):
    def meow(self):
        print("cat meows")
class lion(animal):
    def shout(self):
        print("Lion Rages")
dog1=Dog()
cat1=cat()
lion1=lion()
dog1.eat()
dog1.bark()
cat1.eat()
cat1.meow()
lion1.shout()

class student:
    def details(self,name,age):
        self.name=name
        self.age=age
class result(student):
    def display(self,marks,result):
        self.marks=marks
        self.result=result
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
        print("Result:",self.result)
res=result()
res.details("Ravi",20)
res.display(75,"pass")

# single inheritance-one parent,one child
class employee:
    def work(self):
        print("Employee works")
class developer(employee):
    def code(self):
        print("Developer writes code")
obj=developer()
obj.work()
obj.code()


# Multiple-many parents,one child
class hr:
    def emp1(self):
        print("employee 1")
class recruit:
    def emp2(self):
        print("Employee 2")
class office(hr,recruit):
    def emp3(self):
        print("Employee 3")
obj=office()
obj.emp1()
obj.emp2()
obj.emp3()

# Multilevel-grandparent,parent,child
class employee:
    def work(self):
        print("level 1")
class employee2(employee):
    def roam(self):
        print("level 2")
class employee3(employee2):
    def review(self):
        print("level 3")
obj=employee3()
obj.work()
obj.roam()
obj.review()

# hybrid- combining two inheritance types(single,multiple)
class employee:
    def login(self):
        print("Employee login")
class hr(employee):
    def recruit(self):
        print("HR Recruits")
class developer(employee):
    def code(self):
        print("developers codes")
class office(hr,developer):
    def work(self):
        print("work done in office")
obj=office()
obj.login()
obj.recruit()
obj.code()
obj.work()