from abc import ABC, abstractmethod

# Abstract Class
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    def receipt(self):
        print("Payment receipt is being generated...")

class Bkash(PaymentSystem):
    def pay(self, amount):
        print(f"Payment of {amount} Taka has been made using bKash.")
        
class Nagad(PaymentSystem):
    def pay(self, amount):
        print(f"Payment of {amount} Taka has been made using Nagad.")

# ব্যবহার
user1 = Bkash()
user1.pay(500)
user1.receipt()

user2 = Nagad()
user2.pay(1000)