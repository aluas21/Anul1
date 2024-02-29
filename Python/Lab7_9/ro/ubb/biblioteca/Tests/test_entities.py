import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.entities import Book, Client


class test_book(TestCase):
    def setUp(self) -> None:
        self.carte = Book(1, "Ion", "roman", "Liviu")

    def test_get_id(self):
        self.assertEqual(self.carte.get_id(), 1)

    def test_get_titlu(self):
        self.assertEqual(self.carte.get_titlu(), "Ion")

    def test_get_descriere(self):
        self.assertEqual(self.carte.get_descriere(), "roman")

    def test_get_autor(self):
        self.assertEqual(self.carte.get_autor(), "Liviu")

    def test_set_id(self):
        self.carte.set_id(2)
        self.assertEqual(self.carte.get_id(), 2)

    def test_set_descriere(self):
        self.carte.set_descriere("ROMAN")
        self.assertEqual(self.carte.get_descriere(), "ROMAN")

    def test_set_titlu(self):
        self.carte.set_titlu("ION")
        self.assertEqual(self.carte.get_titlu(), "ION")

    def test_set_autor(self):
        self.carte.set_autor("LIVIU")
        self.assertEqual(self.carte.get_autor(), "LIVIU")


class test_client(TestCase):
    def setUp(self) -> None:
        self.client = Client(1, "Alin", 1122334455)

    def test_get_nume(self):
        self.assertEqual(self.client.get_nume(), "Alin")

    def test_get_cnp(self):
        self.assertEqual(self.client.get_cnp(), 1122334455)

    def test_get_id(self):
        self.assertEqual(self.client.get_id(), 1)

    def test_set_id(self):
        self.client.set_id(2)
        self.assertEqual(self.client.get_id(), 2)

    def test_set_nume(self):
        self.client.set_nume("ALIN")
        self.assertEqual(self.client.get_nume(), "ALIN")

    def test_set_cnp(self):
        self.client.set_cnp(1122334466)
        self.assertEqual(self.client.get_cnp(), 1122334466)


if __name__ == '__main__':
    unittest.main()