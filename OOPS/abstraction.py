# Abstract class is formed when it has at least one  abstract method (method inside which no piece of code is written ),and it inherits from ABC 
# we cannot make objecrt of abstract class.
# 



from abc import ABC,abstractmethod

class Bank(ABC):            # inherits from ABC

    def database(self):
        print("connected to database.")
    
    @abstractmethod
    def security():
        pass

