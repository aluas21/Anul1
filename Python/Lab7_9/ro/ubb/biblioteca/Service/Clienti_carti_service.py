from ro.ubb.biblioteca.Domain.dto import Client_carti
from ro.ubb.biblioteca.Repository import file_repository_clienti, flie_repository_imprumuturi
from ro.ubb.biblioteca.Repository.Imprumuturi_repository import Imprumut_repository
from ro.ubb.biblioteca.Repository.Repository import Repository
from ro.ubb.biblioteca.Repository.flie_repository_imprumuturi import FileRepositoryImprumuturi


class Clienti_carti_service():
    def __init__(self, clienti_carti_repository : Repository(), clienti_repository : file_repository_clienti, imprumut_repository = FileRepositoryImprumuturi):
        self.__clienti_carti_repository = clienti_carti_repository
        self.__clienti_repository = clienti_repository
        self.imprumut_repository = imprumut_repository

    def get_numar_carti(self, id_client):
        k = 0
        for imprumut in [*self.imprumut_repository.get_all()]:
            if imprumut.get_id_client() == id_client:
                k += 1
        return k

    def generare_lista_sortare(self):
        for client in [*self.__clienti_repository.getAll()]:
            client_carti = Client_carti(client.get_id(), client.get_nume(), self.get_numar_carti(client.get_id()))
            if self.__clienti_carti_repository.get_by_id(client.get_id()) is None:
                self.__clienti_carti_repository.adauga(client_carti)

        list_sort = self.__clienti_carti_repository.getAll()
        for i in range(0, len(list_sort)-1):
            for j in range(i+1, len(list_sort)):
                if list_sort[i].get_nume_client() > list_sort[j].get_nume_client():
                    client_carti = list_sort[i]
                    list_sort[i] = list_sort[j]
                    list_sort[j] = client_carti
                elif list_sort[i].get_nume_client() == list_sort[j].get_nume_client():
                    if list_sort[i].get_nr_carti() < list_sort[j].get_nr_carti():
                        client_carti = list_sort[i]
                        list_sort[i] = list_sort[j]
                        list_sort[j] = client_carti
        return list_sort

    def clienti_activi(self):
        for client in [*self.__clienti_repository.getAll()]:
            client_carti = Client_carti(client.get_id(), client.get_nume(), self.get_numar_carti(client.get_id()))
            if self.__clienti_carti_repository.get_by_id(client.get_id()) is None:
                self.__clienti_carti_repository.adauga(client_carti)

        list_sort = self.__clienti_carti_repository.getAll()
        for i in range(0, len(list_sort)-1):
            for j in range(i+1, len(list_sort)):
                if list_sort[i].get_nr_carti() < list_sort[j].get_nr_carti():
                    client_carti = list_sort[i]
                    list_sort[i] = list_sort[j]
                    list_sort[j] = client_carti
                elif list_sort[i].get_nr_carti() == list_sort[j].get_nr_carti():
                    if list_sort[i].get_nr_carti() > list_sort[j].get_nr_carti():
                        client_carti = list_sort[i]
                        list_sort[i] = list_sort[j]
                        list_sort[j] = client_carti
        lungime = len(list_sort)
        lungime = int((1/5)*lungime)
        return list_sort[:lungime]

    def sterge_client(self, id_client):
        for client_carti in [*self.__clienti_repository.get_all()]:
            if client_carti.get_id() == id_client:
                self.__clienti_carti_repository.sterge_definitiv(client_carti.get_id_imprumut())



