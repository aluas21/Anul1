from ro.ubb.biblioteca.Domain.entities import Book
from ro.ubb.biblioteca.Repository.Repository import Repository
from ro.ubb.biblioteca.Repository.flie_repository_carti import FileRepositoryCarti


class Carti_service:
    # def __init__(self, carti_repository : Repository):
    #     self.__carti_repository = carti_repository
    def __init__(self, carti_repository : FileRepositoryCarti):
        self.__carti_repository = carti_repository

    def get_all(self):
        """
        returneaza lista de angajati
        :return:
        """
        return self.__carti_repository.getAll()

    def get_carte(self, id_carte):
        """
        returneaza cartea cu id-ul dat, daca exista
        :param id_carte:
        :return:
        """
        return self.__carti_repository.get_by_id(id_carte)

    def adaugare(self, id, titlu, desc, autor):
        """
        adauga un nou client
        :param id:
        :param nume:
        :param cnp:
        :return:
        """
        carte_noua = Book(id, titlu, desc, autor)
        self.__carti_repository.adauga(carte_noua)

    def modificare(self, id, titlu, desc, autor):
        """
        modifica un client dupa id
        :param id: id-ul clinet
        :param nume: nume client
        :param cnp: cnp-ul client
        :return:
        """
        carte_noua  = Book(id, titlu, desc, autor)
        self.__carti_repository.modifica(carte_noua)

    def stergere(self, id):
        """
        sterge din lista de clienti clientul cu id-ul dat
        :param id: id- ul unui angajat
        :return:
        """
        self.__carti_repository.stergere(id)
