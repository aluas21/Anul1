#
# from ro.ubb.biblioteca.Domain.entities import Client, Book
# # from ro.ubb.biblioteca.Repository.Carti_repository import Carti_repository
# from ro.ubb.biblioteca.Repository.Repository import Repository
#
#
# class Test_Repository:
#     @staticmethod
#     def test_client_rep():
#         lista_clienti = Repository()
#         lista_clienti.adauga(Client(1, "Alex", 768796234))
#         lista_clienti.adauga(Client(2, "Maria", 9868677812))
#         lista_clienti.adauga(Client(3, "Roxana", 679878423))
#         lista_clienti.adauga(Client(5, "Cristina", 785670149))
#
#         assert lista_clienti.get_by_id(4).get_id() == 4
#         assert lista_clienti.get_by_id(5).get_name() == "Cristina"
#         assert lista_clienti.get_by_id(2).get_cnp() == 9868677812
#
#     @staticmethod
#     def test_carte_rep():
#         # lista_carti = Carti_repository()
#         lista_carti.adauga(Book(1, "ION", "Roman", "Liviu Rebreanu"))
#         lista_carti.adauga(Book(3, "Moara", "nuvela", "Slavici"))
#         lista_carti.adauga(Book(2, "Lucefar", "poezie", "Eminescu"))
#         lista_carti.adauga(Book(5, "Pumb", "poezie", "Bacovia"))
#
#         assert lista_carti.get_by_id(5).get_titlu == "Plumb"
#         assert lista_carti.get_by_id(3).get_autor == "Eminescu"
#         assert lista_carti.get_by_id(1).get_id == 1
#         assert lista_carti.get_by_id(2).get_desc == "poezie"
#         assert lista_carti.get_by_id(3).get_titlu == "Moara"
#
#
# test_2 = Test_Repository
# test_2.test_client_rep()
# test_2.test_carte_rep()
import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.entities import Client
from ro.ubb.biblioteca.Repository.Repository import Repository


class test_Repository_client(TestCase):
    def setUp(self) -> None:
        self.client = Client(1,"Alin", 41232234)
        self.repository = Repository()

    def test_get_all(self):
        self.repository.adauga(self.client)
        self.assertEqual(self.repository.getAll(), [self.client])

    def test_get_by_id(self):
        self.repository.adauga(self.client)
        self.assertEqual(self.repository.get_by_id(self.client.get_id()), self.client)

    def test_adauga(self):
        self.repository.adauga(self.client)
        self.assertEqual(self.repository.get_by_id(self.client.get_id()), self.client)

    def test_modifica(self):
        self.repository.adauga(self.client)
        client2 = Client(1,"Alex",5467890)
        self.repository.modifica(client2)
        self.assertEqual(self.repository.get_by_id(self.client.get_id()), client2)


    def test_stergere(self):
        self.repository.adauga(self.client)
        client2 = Client(2,"Alex",5467890)
        self.repository.adauga(client2)
        self.repository.stergere(client2.get_id())
        self.assertEqual(self.repository.getAll(), [self.client])

class test_Repository_carti(TestCase):
    def setUp(self) -> None:
        pass

    def test_get_all(self):
        pass

    def test_get_by_id(self):
        pass

    def test_adauga(self):
        pass

    def test_modifica(self):
        pass

    def test_stergere(self):
        pass

if __name__ == '__main__':
    unittest.main()