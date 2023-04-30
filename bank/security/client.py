import base64

class AccountBank:
    phone: int
    name: str
    password: str
    
    def __init__(self, id: int, accountData: dict) -> None:
        self.id = id
        self.name = accountData["Name"]
        self.password = accountData["Password"]
        while True:
            text = input(f"Olá{self.name}, oque ira fazer? :\n")
            try:
                getattr(self, text)
            except:
                pass