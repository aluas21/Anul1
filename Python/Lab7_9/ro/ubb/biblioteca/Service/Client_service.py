from ro.ubb.biblioteca.Repository.Repository import Repository
from ro.ubb.biblioteca.Domain.entities import Client
from ro.ubb.biblioteca.Repository.file_repository_clienti import FileRepositoryClienti


class Client_service:
    # def __init__(self, client_repository : Repository):
    #     self.__client_repository = client_repository
    def __init__(self, client_repository : FileRepositoryClienti):
        self.__client_repository = client_repository

    def get_all(self):
        """
        returneaza lista de angajati
        :return: lista de obiecte de tipul angajat
        """
        return self.__client_repository.getAll()

    def get_client(self, id):
        """
        returneza obiectul de tipul obiect care are id-ul corespunzator cu cel dar, in cazul in care exista
        :param id:
        :return:
        """
        return self.__client_repository.get_by_id(id)

    def adaugare(self, id, nume, cnp):
        """
        adauga un nou client
        :param id:
        :param nume:
        :param cnp:
        :return:
        """
        client_nou = Client(id, nume, cnp)
        self.__client_repository.adauga(client_nou)


    def modificare(self, id, nume, cnp):
        """
        modifica un client dupa id
        :param id: id-ul clinet
        :param nume: nume client
        :param cnp: cnp-ul client
        :return:
        """
        client_nou = Client(id, nume, cnp)
        self.__client_repository.modifica(client_nou)

    def stergere(self, id):
        """
        sterge din lista de clienti clientul cu id-ul dat
        :param id: id- ul unui angajat
        :return:
        """
        self.__client_repository.stergere(id)
