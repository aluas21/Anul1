from ro.ubb.biblioteca.Domain.entities import Client
from ro.ubb.biblioteca.Repository.Repository import Repository


class FileRepositoryClienti(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                array = line.split(",")
                client = Client(int(array[0]), array[1], int(array[2]))
                self._entitati[client.get_id()] = client

    def scrie(self, client):
        with open(self.__file_name, "a") as f:
            f.write("\n" + str(client.get_id()) + "," + client.get_nume() + "," + str(client.get_cnp()))

    def stergere(self, client):
        super().stergere(client)
        with open(self.__file_name, "w") as f:
            ok = 0
            for client in self._entitati.values():
                if ok == 0:
                    f.write(str(client.get_id()) + "," + client.get_nume() + "," + str(client.get_cnp()))
                else:
                    f.write("\n" + str(client.get_id()) + "," + client.get_nume() + "," + str(client.get_cnp()))
                ok += 1
        self.__load_data()

    def adauga(self, client):
        super().adauga(client)
        self.scrie(client)

    def modifica(self, client):
        super().modifica(client)
        with open(self.__file_name, "w") as f:
            ok = 0
            for client in self._entitati.values():
                if ok == 0:
                    f.write(str(client.get_id()) + "," + client.get_nume() + "," + str(client.get_cnp()))
                else:
                    f.write("\n" + str(client.get_id()) + "," + client.get_nume() + "," + str(client.get_cnp()))
                ok += 1
        self.__load_data()



