class Student:
    species = "Student"
    count = 0

    def __init__(self, name=None, age=None, edu=None):
        self.name = name
        self.age = age
        self.Education = edu
        Student.count += 1
        print(f"New object of species:- {self.species}, OBJ.{Student.count} created.....\n")

    def speak(self):
        print(f"{self.name} makes a sound.")

    def get_info1(self):
        print(Student.species)
        print(f"{self.name} is {self.age} years old and belongs.")

    def get_info2(self):
        print(f"{self.name} is {self.age} years old and studies {self.Education}.")

    def get_info3(self):
        if self.Education:
            print(f"{self.name} is {self.age} years old and studies {self.Education}.")
        else:
            print(f"{self.name} is {self.age} years old.")

    @staticmethod
    def Data():
        print(f"""
Hello,
I am Shubham and I am 20 year old, I am from VJTI, Mumbai,
I want to become an IT Engineer in Google or Microsoft.
For this I took admission in this college.
Otherwise I had options to take admission in lower branches of IITs and higher branches in NITs.
But for my dreams, I compromised those big and high-value colleges.
""")


class Car:
    def __init__(self, brand=None):
        self.acc = False
        self.brk = False
        self.cluch = False
        self.Brand = brand

    def Start(self):
        self.acc = True
        self.brk = True
        self.cluch = True
        print(f"The #{self.Brand}# Car Started....")


class Account(Student, Car):
    __Account_Manager_Name = "Anonymous"  # private class variable

    def __Manager():  # private method
        print("The Manager of Bank is :-", Account.__Account_Manager_Name)

    def __init__(self, name, age, edu, brand, balance, acc_no):
        Student.__init__(self, name, age, edu)  # explicitly call both parents
        Car.__init__(self, brand)
        self.balance = balance
        self.__accountNo = acc_no  # private variable
        Account.__Manager()
        print(f"New Account was created...\nBalance: Rs.{self.balance}\nAcc.No.: {self.__accountNo}\n")

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was Debited From Account NO. {self.__accountNo}")
        self.getAmmount()

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was Credited To Account NO. {self.__accountNo}")
        self.getAmmount()

    def getAmmount(self):
        print(f"Total Amount(Rs.) in Account No. {self.__accountNo} is : {self.balance}")




# Creating an Account object with student + car + account properties
student = Account("Shubham", 20, "IIT-B-Tech", "BMW", 10000, "ABC123")

# Student behavior
student.speak()
print("1.")
student.get_info1()
print("2.")
student.get_info2()
print("3.")
student.get_info3()

# Static method
print("4. Static Method Call:")
student.Data()

# Car functionality
print("\n5. Car Functionality:")
student.Start()

# Banking functionality
print("\n6. Banking Functionality:")
student.debit(3000)
student.credit(7000)

# Access public and private members
print("\n7. Access public balance:", student.balance)
# print(student.__accountNo)  # ❌ will give error (private)
