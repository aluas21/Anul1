from ro.ubb.biblioteca.Repository.Carti_repository import Carti_repository
from ro.ubb.biblioteca.Repository.Repository import Repository
from ro.ubb.biblioteca.Service.Carti_service import Carti_service
from ro.ubb.biblioteca.Service.Client_service import Client_service


class Test_Service():
    @staticmethod
    def test_client():
        lista = Repository()
        client_service = Client_service(lista)
        client_service.adaugare(1, "Maria", 678968)
        client_service.adaugare(2, "Maria", 698767)

        lista_clienti = client_service.get_all()
        for client in lista_clienti:
            assert client.get_nume() == "Maria"

    @staticmethod
    def test_carte():
        lista = Carti_repository()
        carti_service = Carti_service(lista)
        carti_service.adaugare(1,"Ion", "roman", "autor")
        carti_service.adaugare(2,"Ion", "b", "c")

        lista_carti = carti_service.get_all()
        for carte in lista_carti:
            assert carte.get_titlu == "Ion"


test_3 = Test_Service()
test_3.test_client()
test_3.test_carte()
