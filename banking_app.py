from secrets import choice


class User:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def call_user(self) -> str:
        print(f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender}")


class Bank(User):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)
        self.balance = 0
        
    def withdraw(self, amount):
        self.balance -= amount
        print(f"A withdraw of {amount} was made")
        print(f"The balance is: {self.balance}")
    
    def deposite(self, amount):
        self.balance += amount
        print(f"A deposite of {amount} was made")
        print(f"The balance is: {self.balance}")
        


petter = Bank("Petter", 28, "Male")
run = True

while run:
    print("-------MENU-------")
    val = input(print("Create a new user: Press 1"))
    if val == 1:
        name = input(print("Whats the users name"))
        age = input(print("Whats the users age"))
        gender = input(print("Whats the users gender"))
        
        

print(petter.call_user())
petter.deposite(10)
petter.withdraw(5)

