from ro.ubb.biblioteca.Domain.entities import Book
from ro.ubb.biblioteca.Repository.Repository import Repository


class FileRepositoryCarti(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                array = line.split(",")
                carte = Book(int(array[0]), array[1], array[3], array[2])
                self._entitati[carte.get_id()] = carte

    def scrie(self, carte):
        with open(self.__file_name, "a") as f:
            f.write(str(carte.get_id()) + "," + carte.get_titlu() + "," + carte.get_autor() + "," + carte.get_descriere())

    def stergere(self, carte):
        super().stergere(carte)
        with open(self.__file_name, "w") as f:
            ok = 0
            for carte in self._entitati.values():
                f.write(str(carte.get_id()) + "," + carte.get_titlu() + "," + carte.get_autor() + "," + carte.get_descriere())
        self.__load_data()

    def adauga(self, carte):
        super().adauga(carte)
        self.scrie(carte)

    def modifica(self, carte):
        super().modifica(carte)
        with open(self.__file_name, "w") as f:
            for carte in self._entitati.values():
                f.write(str(carte.get_id()) + "," + carte.get_titlu() + "," + carte.get_autor() + "," + carte.get_descriere())

        self.__load_data()



