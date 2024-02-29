import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.imprumuturi import Imprumut


class test_imprumut(TestCase):
    def setUp(self) -> None:
        self.imprumut  = Imprumut(1,2,3)
        self.imprumut.set_nr_exemplare(4)

    def test_get_id_imprumut(self):
        self.assertEqual(self.imprumut.get_id_imprumut(), 1)

    def test_get_id_client(self):
        self.assertEqual(self.imprumut.get_id_client(), 2)

    def test_get_id_carte(self):
        self.assertEqual(self.imprumut.get_id_carte(), 3)

    def test_get_nr_exemplare(self):
        self.assertEqual(self.imprumut.get_nr_exemplare(), 4)

    def test_set_id_imprumut(self):
        self.imprumut.set_id_imprumut(2)
        self.assertEqual(self.imprumut.get_id_imprumut(), 2)

    def test_set_id_client(self):
        self.imprumut.set_id_client(3)
        self.assertEqual(self.imprumut.get_id_client(), 3)

    def test_set_id_carte(self):
        self.imprumut.set_id_carte(4)
        self.assertEqual(self.imprumut.get_id_carte(), 4)

    def test_set_nr_exemplare(self):
        self.imprumut.set_nr_exemplare(5)
        self.assertEqual(self.imprumut.get_nr_exemplare(), 5)

if __name__ == '__main__':
    unittest.main()