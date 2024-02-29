from ro.ubb.biblioteca.Exceptii.duplicate_error import Duplicate_Error


class Repository:
    def __init__(self):
        self._entitati= {}

    def getAll(self):
        '''
        returneaza lista de clienti
        :return: o lista de obiecte de tipul angajat
        '''
        # daca am scrie return self.__angajati am returna un dictionar de angajati
        # iar layerele "de mai sus" au nevoie de o lista
        return list(self._entitati.values())

    def get_by_id(self, id_entitate):
        '''
        returneaza angajatul cu id-ul dat
        :param id_entitate:
        :return:
        '''
        # return self.__clienti.get(id_client,None)
        if id_entitate in self._entitati:
            return self._entitati[id_entitate]
        return None

    def adauga(self, entitate):
        '''
        adauga un client in lista
        :param entitate:
        :return:
        '''
        if self.get_by_id(entitate.get_id()) is not None:
            raise Duplicate_Error("Exista deja un client cu acest id!")
        self._entitati[entitate.get_id()] = entitate

    def modifica(self, entitate):
        """
        modifica un angajat dupa id
        :param entitate:
        :return:
        """
        if self.get_by_id(entitate.get_id()) is None:
            raise ValueError(" Nu exista un client cu acest id!")
        self._entitati[entitate.get_id()] = entitate

    def stergere(self, entitate):
        """
        sterge un client dupa id
        :param entitate:
        :return:
        """
        if self.get_by_id(entitate) is None:
            raise ValueError(" Nu exista un client cu acest id!")
        self._entitati.pop(entitate)
