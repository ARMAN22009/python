class Atm:

    __customernumber=1                                    #static variable -->>  accessed with classname  eg:Atm.customernumber
                                                        #made for class ,
    
    @staticmethod                           # to access this method we do not need to create object
    def get_customernumber():                               #getter
         return Atm.__customernumber



    # default constructors
    # def  __init__(self):
    #     pass

    # Parameterized  constructors
    def __init__(self):
        self.pin=""
        self.__balance=0

        self.cid=Atm.__customernumber                     
        Atm.__customernumber=Atm.__customernumber+1
        print("your customer id is :",self.cid)


        self.menu()    #agar method ko method ke andar call krna hai to  \\self.\\   likhna pdega
                       #golden rule of oop  >>>>  function(methods) inside a class can only be accessed by the objects of that class
                       #not even the methods which are inside the class can be called by the methods of that class
                       #to call the wunctions we use ||||| self.||||
       

        
    def get_balance(self):
         return self.__balance
    
    def set_balance(self,new_value):
         if type(new_value)==int:
              self.balance=new_value
              return new_value


    def menu(self):
        print("enter 1 to create pin.")
        print("enter 2 to deposit.")
        print("enter 3 to withdraw.")
        print("enter 4 to check balance .")
        print("enter 5 to exit.")
        print("enter 6 to change pin.")

        user_input=int(input())

        if (user_input ==1):
            print("create pin")
            self.create_pin() 

        elif(user_input==2):
            print("deposit")
            self.deposit()
            
        elif(user_input==3):
            print("withdraw")
            self.withdraw()

        elif(user_input==4):
            print("check balance")
            self.check_balance()

        elif(user_input==5):
            print("exit") 

        elif(user_input==6):
            print("change pin")
            self.change_pin()



    def create_pin(self):
                print("enter pin")
                user_pin=int(input())
                self.pin=user_pin
                
                user_balance=int(input("enter balance"))
                self.__balance=user_balance
                self.menu()
                
    def change_pin(self):
                old_pin=int(input("enter old pin"))

                if (old_pin==self.pin):
                    new_pin=int(input("enter new pin"))
                    self.pin=new_pin
                else:
                    print("chala ja ")
                self.menu()

    def deposit(self):
            user_pin=int(input("enter your pin:"))

            if (user_pin==self.pin):
             amount=int(input("amount to be deposited:"))
             self.__balance=self.__balance+amount
             print("total amount:",self.__balance)
            self.menu()
         
    def check_balance(self):
            user_pin=int(input("enter your pin:"))

            if (user_pin==self.pin):
                print("you balance is :",self.__balance)
            self.menu()

    def withdraw(self):
            user_pin=int(input("enter your pin:"))

            if(user_pin==self.pin):
                amount=int(input("amount to be withdrawn:"))
                if (self.__balance>=amount):
                    self.__balance=self.__balance-amount
                    print("total amount:",self.__balance)
                else:
                    print("not sufficient balance :",self.__balance)
            self.menu()

    
         

sbi=Atm() 
hdfc=Atm()

print(sbi.cid)
print(hdfc.cid)
print(Atm._Atm__customernumber)#--->>>   3  
Atm.get_customernumber()

# sbi.get_balance()
# sbi.__balance=0          # now here __balance is not the real balance which was stored in class  rather the realbalance was stored as _Atm__balance .
                         # and here  by creating __balance a new attribute is created inside the class , which is independent from  the real balance.
        
#INSTANCE VARIABLE                                          VS                     STATIC VARIABLE
#made for objects                                                         made for class
#different values for different objects                                   same value for differnt objects
#defined inside constructor                                               defined outside constructor but inside the class
#objectname.variablename                                                  classname.variablename