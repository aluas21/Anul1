class Imprumut:
    def __init__(self, id_imprumut, id_client, id_carte):
        self.__id_imprumut = id_imprumut
        self.__id_client = id_client
        self.__id_carte = id_carte
        self.__nr_exemplare = 0

    def get_id_imprumut(self):
        return self.__id_imprumut

    def get_id_client(self):
        return self.__id_client

    def get_id_carte(self):
        return self.__id_carte

    def get_nr_exemplare(self):
        return self.__nr_exemplare

    def set_id_imprumut(self, id_imprumut):
        self.__id_imprumut = id_imprumut

    def set_id_client(self, id_client):
        self.__id_client = id_client

    def set_id_carte(self, id_carte):
        self.__id_carte = id_carte

    def set_nr_exemplare(self, nr_exemplare):
        self.__nr_exemplare = nr_exemplare

    def __str__(self):
        return "Client: " + str(self.__id_client) + ", Cartea: " + str(self.__id_carte) + ", numar de exemplare: " + str(self.__nr_exemplare)
