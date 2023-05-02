from os import system
from time import sleep
import json

class AccountBank:
    phone: int
    name: str
    password: str
    
    def __init__(self, id: int, accountData: dict) -> None:
        self.id = id
        self.name = accountData["Name"]
        self.password = accountData["Password"]
        self.accountdata = accountData
        
        print(f"\n\t\tWelcome {self.name}")
        sleep(4)
        while True:
            self._clear_screen()
            print(f"Money :", self.accountdata["money"], "\n")
            print("(w) --> Withdraw Money\n")
            action = input(f"{self.name}, what do you go make? : ".title())
            
            getattr(self, action)()
            sleep(4)
            
            #    print("Unknown Option")
            #    sleep(2)
            self._update_data(self.id)
    
    # Help Functions
    def _update_data(self, id: str):
        with open("security/data/data.json", "r") as file:
            content = json.load(file)[id]
            
        self.accountdata = content
        return
        
    def _clear_screen(self):
        system("clear")
    
    def _save_data(self, attr: str, value: int or str):
        with open("security/data/data.json", "r") as file:
            content = json.load(file)
            content[self.id][attr] = value
            with open("security/data/data.json", "w") as file_write:
                json.dump(content, file_write, indent=4)
        return "data changed with successful"
    
    def w(self):
        value = int(input("insert value :"))
        if (self.accountdata["money"] - int(value)) >= 0: 
            self._save_data(attr='money', value=(self.accountdata["money"] - int(value)))
            print(f"You withdraw ${value} dollars")
        else:
            print("You don't have sufficient money!")