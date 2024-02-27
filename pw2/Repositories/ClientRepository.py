from Classes.client import Client


class ClientRepository:

    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def del_client(self, client: Client):
        self.clients.remove(client)

    def find_client(self, client_name):
        for c in self.clients:
            if c.name == client_name:
                return c

    def show_clients(self):
        for c in self.clients:
            print(f"{c.name}; {c.email}; "
                  f"{c.addr}")
