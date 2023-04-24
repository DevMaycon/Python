from security.client import *
import json

def msg(text: str):
        if text == "1":
            phone = input("Phone: ")
            username = input("Username: ")
            password = input("Password: ")
            Login(phone=phone, username=username, password=password)
        elif text == "2":
            phone = input("Phone: ")
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            Login.create_account(phone=phone, name=username, email=email, password=password)
        else:
            return

class Login:
    clients: list
    
    @classmethod
    

    @classmethod
    def create_account(cls,
        name: str,
        email: str,
        password: str,
        phone: int
        ):
        data_file = "security/data/data.json"
        with open(data_file, "r") as file:
            clients = json.load(file)
            clients[phone] = {"Name":name,
                              "Password":password,
                              "Email":email,
                              "Phone":phone,
                              "money": 0
                              }
            with open(data_file, "w") as file:
                json.dump(clients, file, indent=4)
        
    def __init__(self, phone: int, username: str, password: str):
        data_file = "security/data/data.json"
        with open(data_file, "r") as data:
            clients = json.load(data)
            if phone in clients:
                if username == clients[phone]["name"] and password == clients[phone]["password"]:
                    AccountBank(phone, clients[phone])
                    pass
            else:
                print("Incorrect password or username!")


