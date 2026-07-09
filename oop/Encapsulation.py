# class BankAccount:
#     def __init__(self,owner,bank_name,account_no, balance):
#         self.owner=owner
#         self.bank_name=bank_name
#         self.account_no=account_no
#         self.__balance=balance
#     def show_balance(self):
#         print("Owner:",self.owner)
#         print("Bank Name:",self.bank_name)
#         print("Account Number:",self.account_no)
#         print("Balance:",self.__balance)
# account1=BankAccount("keerthi","Canara Bank",1222321456,10000000)
# account1.show_balance()

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self._account_type="Savings"
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance += amount
#     def withdraw(self,amount):
#         if 0<amount<=self.__balance:
#             self.__balance -= amount
#             print("Withdrawl successful")
#         else:
#             print("Insufficient balance")
#     def show_balance(self):
#         print("Balance:",self.__balance)
# account=BankAccount("John",1000)
# print("Owner:",account.owner)
# print("Account type:",account._account_type)
# account.deposit(500)
# account.withdraw(300)
# account.show_balance()


# class student:
#     def __init__(self,name,age,marks,result):
#         self.name=name
#         self.age=age
#         self.marks=marks
#         self.result=result
#     def show_res(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Marks:",self.marks)
#         print("Result:",self.result)
# student_data=student("Ravi",20,75,"pass")
# student_data.show_res()

# using access specifiers
class student:
    def __init__(self,name,age,marks,result):
        self.name=name #public
        self._age=age  # protected
        self.__marks=marks # private
        self.result=result
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self._age)
        print("Marks:",self.__marks)
        print("Result:",self.result)
student_details=student("Ravi",20,75,"pass")
student_details.show_details()


        
