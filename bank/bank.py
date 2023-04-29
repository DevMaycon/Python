from security.login import Login, msg
from time import sleep

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
text= input("[1] sign in\n[2] Create a Account\nSeja bem vindo, oque ira fazer? : ")
msg(text)