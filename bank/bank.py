from security.login import Login, msg
from os import system
from time import sleep

system("rm -rf security/__pycache__/")

print("Welcome to this bank!\nPlease Wait a moment")
sleep(2)
welcome = """
_______________________
|                     |
|       Welcome       |
|         Say         |
|       < Bank >      |
|_____________________|

"""
print(welcome)
while True:
    text= input("[1] sign in\n[2] Create a Account\nSeja bem vindo, oque ira fazer? : ")
    msg(text)