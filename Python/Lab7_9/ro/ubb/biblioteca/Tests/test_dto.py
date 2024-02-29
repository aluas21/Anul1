import unittest
from unittest import TestCase

from ro.ubb.biblioteca.Domain.dto import Client_carti


class TestClient_carti(TestCase):

    def setUp(self) -> None:
        self.client = Client_carti(1,"Alin",1)

    def test_set_id(self):
        self.client.set_id(2)
        self.assertEqual(self.client.get_id(), 1)

    def test_set_nume_client(self):
        self.client.set_nume_client("Alex")
        self.assertEqual(self.client.get_nume_client(), "Alex")

    def test_set_nr_carti(self):
        self.client.set_nr_carti(3)
        self.assertEqual(self.client.get_nr_carti(), 3)

    def test_get_id(self):
        self.assertEqual(self.client.get_id(), 1)

    def test_get_nume_client(self):
        self.assertEqual(self.client.get_nume_client(), "Alin")

    def test_get_nr_carti(self):
        self.client.set_nr_carti(3)
        self.assertEqual(self.client.get_nr_carti(), 3)

if __name__ == '__main__':
    unittest.main()