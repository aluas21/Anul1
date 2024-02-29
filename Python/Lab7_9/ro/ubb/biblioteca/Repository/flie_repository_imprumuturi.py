from ro.ubb.biblioteca.Domain.imprumuturi import Imprumut
from ro.ubb.biblioteca.Repository.Imprumuturi_repository import Imprumut_repository

class FileRepositoryImprumuturi(Imprumut_repository):
    def __init__(self, file_name):
        super(FileRepositoryImprumuturi, self).__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                array = line.split(",")
                imprumut = Imprumut(int(array[0]), int(array[1]), int(array[2]))
                imprumut.set_nr_exemplare(1)
                self._lista_imprumuturi[imprumut.get_id_imprumut()] = imprumut

    def scrie(self, imprumut):
        with open(self.__file_name, "a") as f:
            f.write("\n" + str(imprumut.get_id_imprumut()) + "," + str(imprumut.get_id_client()) + "," + str(imprumut.get_id_carte()))

    def sterge_definitiv(self, id_imprumut):
        super().sterge_definitiv(id_imprumut)
        with open(self.__file_name, "w") as f:
            ok = 0
            for imprumut in self._lista_imprumuturi.values():
                if ok == 0:
                    f.write(str(imprumut.get_id_imprumut()) + "," + str(imprumut.get_id_client()) + "," + str(imprumut.get_id_carte()))
                else:
                    f.write("\n" + str(imprumut.get_id_imprumut()) + "," + str(imprumut.get_id_client()) + "," + str(imprumut.get_id_carte()))
                ok += 1
        self.__load_data()

    def adauga(self, imprumut):
        super().adauga(imprumut)
        self.scrie(imprumut)




