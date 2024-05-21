import sys
sys.path.append('D:\Important_files\Study\Sem_6\Методологии разработки программного обеспечения\pw3')
from Classes.client import Client


class ClientRepository:

    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def del_client(self, client: Client):
        self.clients.remove(client)

    def find_client(self, client_id):
        for c in self.clients:
            if c.id == client_id:
                return c

    def show_clients(self):
        for c in self.clients:
            print(f"{c.id}; {c.name}; {c.email}; "
                  f"{c.addr}")

