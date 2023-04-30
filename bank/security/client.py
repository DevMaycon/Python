
class AccountBank:
    phone: int
    name: str
    password: str
    
    def __init__(self, id: int, accountData: dict) -> None:
        self.id = id
        self.name = accountData["Name"]
        self.password = accountData["Password"]
        while True:
            text = input(f"Welcome {self.name}, What do you go make? : ".title())
            try:
                getattr(self, text)
            except:
                print("Unknown Option")