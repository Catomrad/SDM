class Client:

    def __init__(self, id, name:str, age:int, email:str, password:str, addr:str):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.addr = addr

    def __eq__(self, other):
        return self.id == other.id and self.mail == other.mail

# c1 = Client(name="1", email="addr1@mail.com", password="123", addr="home")
# c2 = Client(name="2", email="addr2@mail.com", password="123", addr="home")
# c3 = Client(name="3", email="addr5@mail.com", password="123", addr="home")
# c4 = Client(name="4", email="addr4@mail.com", password="123", addr="home")
# c5 = Client(name="5", email="addr5@mail.com", password="123", addr="home")

# print(c1 == c3, c3 == c5)