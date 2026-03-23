class Customer:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def printaddress(self):
        return print(self.address.get_city(),self.address.pin,self.address.state)             #_Address__city
                                                                                              # ya to getter lga skte hai ya to _classname__obj

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.edit_address(new_city,new_pin,new_state)


class Address:

    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state

    def get_city(self):
        return self.__city
    
    def edit_address(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state


a1=Address("hazaribagh",825301,"jharkhand")
c1=Customer("Arman",20,a1)

c1.printaddress()
c1.edit_profile("manoj","patna","927772","bihar")
c1.printaddress()

# in aggregation one class owns the other class ,they have a relationship in between 