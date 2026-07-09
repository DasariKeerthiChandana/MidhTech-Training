# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod # decorator , it marks next line as abstract
#     def start(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print("car starts with a key")
# car1=car()
# car1.start()

from abc import ABC, abstractmethod #name,age,marks, result
class student(ABC):
    @abstractmethod
    def res(self):
        pass
class data(student):
    def res(self,name,age,marks,result):
        self.name=name
        self.age=age
        self.marks=marks
        self.result=result
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)
        print("Result :", self.result)
data1=data()
data1.res("Ravi",20,75,"Pass")
        