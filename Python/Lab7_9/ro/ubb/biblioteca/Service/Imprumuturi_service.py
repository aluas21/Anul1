from ro.ubb.biblioteca.Domain.imprumuturi import Imprumut
from ro.ubb.biblioteca.Repository.flie_repository_imprumuturi import FileRepositoryImprumuturi
from ro.ubb.biblioteca.Repository.Imprumuturi_repository import Imprumut_repository


class Imprumut_service:
    # def __init__(self, imprumut_repository : flie_repository_imprumuturi):
    #     self.__imprumut_repository = imprumut_repository
    def __init__(self, imprumut_repository : FileRepositoryImprumuturi):
        self.__imprumut_repository = imprumut_repository

    def get_all(self):
        """
        returneaza lista de imprumuturi
        :return:
        """
        return self.__imprumut_repository.get_all()

    def adaugare(self, id_imprumut, id_client, id_carte):
        """
        adauga un nou client
        :param id:
        :param nume:
        :param cnp:
        :return:
        """
        imprumut = Imprumut(id_imprumut, id_client, id_carte)
        self.__imprumut_repository.adauga(imprumut)

    def stergere(self, id_client, id_carte):
        """
        sterge din lista de clienti clientul cu id-ul dat
        :param id: id- ul unui angajat
        :return:
        """
        self.__imprumut_repository.sterge(id_client, id_carte)


    def get_nr_carti_by_id(self, id_carte):
        k = 0
        for imprumut in [*self.__imprumut_repository.get_all()]:
            if imprumut.get_id_carte() == id_carte:
                k += 1
        return k

    def carte_max_imprumut(self):
        max = 0
        lista_id_carti = []
        for carte in [*self.get_all()]:
            id_carte = carte.get_id_carte()
            nr_carte = self.get_nr_carti_by_id(carte.get_id_carte())
            if nr_carte > max:
                max = nr_carte
                lista_id_carti.clear()
                lista_id_carti.append(id_carte)
            elif nr_carte == max :
                if id_carte in lista_id_carti:
                    pass
                else:
                    lista_id_carti.append(id_carte)
        return lista_id_carti

    def get_nr_carti_by_id_client(self, id_client):
        kontor = 0
        for imprumut in [*self.get_all()]:
            if id_client == imprumut.get_id_client():
                kontor += 1
        return kontor

    def sterge_client(self, id_client):
        for imprumut in [*self.__imprumut_repository.get_all()]:
            if imprumut.get_id_client() == id_client:
                self.__imprumut_repository.sterge_definitiv(imprumut.get_id_imprumut())

    def sterge_carte(self, id_carte):
        for imprumut in [*self.__imprumut_repository.get_all()]:
            if imprumut.get_id_carte() == id_carte:
                self.__imprumut_repository.sterge_definitiv(imprumut.get_id_imprumut())