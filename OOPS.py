class Student:             # Encapsulation for all classes
    species = "Student"   # Not chnging variable .
    count=0               # This is chamging variable .  
    

# Default Constructor

    def __init__(self):
       pass
     

# Parameterized Constructor

    def __init__( self , name=None ,age=None , edu=None ):  # constuctor  # if we not pass third parameter then it will by default give none
        self.name = name
        self.age = age
        self.Education=edu
        Student.count+=1
        print(f"New object of species:-{self.species} , OBJ.{Student.count} created.....\n")


    # def __init__(abcd , edu):  # constuctor  wrong only one constructor
    #     abcd.Education= edu
    


    def speak (self):                      #any function/Method
        print(f"{self.name} makes a sound.")

    def get_info1(self):
        print(Student.species)
        print(f"{self.name} is {self.age} years old and belongs.")



    def get_info2(self):
       print(f"{self.name} is {self.age} years old and studies {self.Education}.")




    def get_info3(self):  # instance method
        if self.Education:
            print(f"{self.name} is {self.age} years old and studies {self.Education}.")
        else:
            print(f"{self.name} is {self.age} years old.")


    @staticmethod

    def Data():
        print(f"Hello,\nI am Shubham and I am 20  year old,I am from VJTI,Mumbai,\nI want to become an IT Engineer in Google or Microsoft, for This I took admission in this college otherwise I had option to take Admission in Lower Branch of IIT AND some higher Branch in NIT's \nBut for my dreams I compramise this big and high value colleges.")
 



st1= Student("Shubham",20)
st1. speak ()

print("1.")
st1.get_info1()

print("2.")
st1.get_info2()

print("3.")
st1.get_info3()
st1.Data()




print("4.")

st2 =  Student("Sujit")
st2. speak ()
st2.get_info2()


print("5.")
st3 = Student()



class car :
    
    def __init__(self):   # Abstraction

        self.acc = False   
        self.brk = False
        self.cluch = False


    def Start(self):
        self.acc = True 
        self.brk = True 
        self.cluch = True     
          
        print("Car Started....")



c1= car()
c1.Start()



class Account():

    def __init__(self, balance, acc):

        self.balance = balance
        self.__accountNo= acc   # Private  (__Private)

        Account.__Manager()     #call to private unction by member function only
        print(f"New Account was created... with \nBalance:-{self.balance} \nAcc.No.:-{self.__accountNo}")



    __Account_Manager_Name="Annonymous" # Private


    def __Manager():                    # Private
        print ("The Manager of Bank is :- ",Account.__Account_Manager_Name)



    def debit(self,amount):
      self.balance -= amount
      print(f"Rs.",amount,f"was Debited From Account NO.{self.__accountNo}")
      print(self.getAmmount())


    def credit(self, amount):
        self.balance+=amount
        print(f"Rs.{amount},was credited From Account NO.{self.__accountNo}")
        print(self.getAmmount())



    def getAmmount(self):
        print(f"Total Amount(Rs.)in Account No.{self.__accountNo} is  : ",self.balance)
        pass
        


Acc = Account(10000,"ABC123")
Acc.debit(5000)
Acc.credit(10000)


print(Acc.balance)        # this  is Public
# print(Acc.__accountNo)  # Private we cant access it
# print(Acc.accountNo)


  





