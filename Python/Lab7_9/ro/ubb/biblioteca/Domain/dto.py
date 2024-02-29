class Client_carti():
    def __init__(self, id_client, nume_client, nr_carti):
        self.__id_client = id_client
        self.__nume_client = nume_client
        self.__nr_carti = nr_carti

    def set_id(self, id_enitate):
        self.__id_entitate = id_enitate

    def set_nume_client(self, nume_client):
        self.__nume_client = nume_client

    def set_nr_carti(self, nr_carti):
        self.__nr_carti = nr_carti

    def get_id(self):
        return self.__id_client

    def get_nume_client(self):
        return self.__nume_client

    def get_nr_carti(self):
        return self.__nr_carti

    def __str__(self):
        return f"Nume Client: {self.__nume_client}, numar carti: {self.__nr_carti}"