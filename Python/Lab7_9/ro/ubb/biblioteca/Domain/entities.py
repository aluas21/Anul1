class Book:
    def __init__(self, id_b, titlu, descriere, autor):
        self.__id = id_b
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor

    def set_id(self, id):
        self.__id = id

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_autor(self, autor):
        self.__autor = autor

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_autor(self):
        return self.__autor

    def get_id(self):
        return self.__id

    def __str__(self):
        return "Carte: " + "id: " + str(self.get_id()) + ", titlu: " + str(self.__titlu) + ", autor: " + str(self.__autor) + ", desc: " + str(self.__descriere)


class Client:
    def __init__(self, id_c, nume, cnp):
        self.__id = id_c
        self.__nume = nume
        self.__cnp = cnp

    def set_id(self, id):
        self.__id = id

    def set_nume(self, nume):
        self.__nume = nume

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def get_id(self):
        return self.__id

    def __str__(self):
        return "Client: " + "id: " + str(self.__id) + ", nume: " + str(self.__nume+ ", cnp: " + str(self.__cnp))

