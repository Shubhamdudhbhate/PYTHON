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
        print(f"Hello,\nI am Shubham and I am 20 years old, I am from VJTI, Mumbai.\n"
              f"I want to become an IT Engineer in Google or Microsoft.\n"
              f"For this, I took admission in this college. Otherwise, I had options "
              f"to take admission in lower branches of IITs or higher branches in NITs.\n"
              f"But for my dreams, I compromised those big and high-value colleges.")


class Car(Student):
    def __init__(self, name=None, age=None, edu=None, brand=None):
        super().__init__(name, age, edu)
        self.acc = False
        self.brk = False
        self.cluch = False
        self.Brand = brand

    def Start(self):
        self.acc = True
        self.brk = True
        self.cluch = True
        print(f"The #{self.Brand}# Car Started....")


class Account(Car):
    def __init__(self, name, age, edu, brand, balance, acc_no):
        super().__init__(name, age, edu, brand)
        self.balance = balance
        self.accountNo = acc_no
        print(f"New Account was created...\nBalance: Rs.{self.balance}\nAcc.No.: {self.accountNo}\n")

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was Debited From Account No. {self.accountNo}")
        self.getAmmount()

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was Credited To Account No. {self.accountNo}")
        self.getAmmount()

    def getAmmount(self):
        print(f"Total Amount(Rs.) in Account No. {self.accountNo} is: {self.balance}")


# 🌟 Creating an Account object with student + car + account properties
student = Account("Shubham", 20, "IIT-B-Tech", "BMW", 10000, "ABC123")

# 🎓 Student behavior
student.speak()
print("1.")
student.get_info1()
print("2.")
student.get_info2()
print("3.")
student.get_info3()

# 🧠 Static method
print("4. Static Method Call:")
student.Data()

# 🚗 Car functionality
print("\n5. Car Functionality:")
student.Start()

# 💰 Banking functionality
print("\n6. Banking Functionality:")
student.debit(3000)
student.credit(7000)


#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--

class A:
    def __init__(self):
        super().__init__()
        print("A")

class B:
    def __init__(self):
        super().__init__()
        print("B")

class C(A, B):   # Multiple Inheritance
    def __init__(self):
        super().__init__()
        print("C")

c = C()


#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--


class Car :
    def __init__ (self,type):
      
      self.type = type

 
    @staticmethod

    def Start():
        print("Car Started...")


    @staticmethod
    def Stop():
        print("Car Stoped...")
  

class Toyota(Car):

    def __init__(self, name, type):
     super().__init__(type)
     self.name = name


car1= Toyota("Fortuner","NEW")
car1.Start()
car1.Stop()
print(car1.type)
print(car1.name)

#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--


class Person:
    name = "Annonymous"

    def Changename(self,name):
        #self.name = name    # wrong
        #Person.name = name   # Right
        self.__class__.name = name    #Right


    def changename(self,name):
      self.name = name  # only change itself attribute not class attribute


    @classmethod                         # this change actual class atributes
    def ClassChangeAttribute(cls,name):  # cls or anything you write  
       cls.name=name


print("\n \n Start......\n")

p1 = Person()
p1.Changename("Shubham")
print(p1.name)
print(Person.name)



print("Next......\n")



Person.name="Anonymous"
p2 = Person()
p2.changename("DON(Mumbai)")
print(p2.name) 
print(Person.name)  #same as above  self :-can't change actual class 


print("Next......\n")



Person.name="Anonymous"
p3 = Person()
p3.ClassChangeAttribute("SHUBHAM")
print(p3.name)
print(Person.name)



#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________--


class Marks:
    
    def __init__(self,Phy,CO,Math):
        self.Phy = Phy
        self.CO = CO
        self.Math = Math
        self.percents = str((self.Phy +  self.CO +   self.Math)/3 ) + "%"  # wrong Method

    def ClalcPercent(self):                                                #  correct
        return str((self.Phy +  self.CO +   self.Math)/3 ) + "%"


    @property    #  we Don't need to call Function  Again and Again        #  correct
    def Percentage(self):
         return  str((self.Phy +  self.CO +   self.Math)/3 ) + "%"
  


   
print("\n")

stu1 = Marks(84,71,62)
print(stu1.percents)
print(stu1.ClalcPercent())
print(stu1.Percentage,"\n \n")


stu1.Math = 70
print(stu1.percents)
print(stu1.ClalcPercent())
print(stu1.Percentage,"\n")

stu1.Phy  = 99
stu1.Math = 100
stu1.CO  = 100

print(stu1.Percentage)










