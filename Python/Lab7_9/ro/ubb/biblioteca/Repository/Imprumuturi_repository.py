class Imprumut_repository:
    def __init__(self):
        self._lista_imprumuturi = {}

    def get_all(self):
        """
        returneaza lista cu toate imprumuturile
        :return:
        """
        return list(self._lista_imprumuturi.values())

    def find_by_id_imprumut(self, id_imprumut):
        """
        returneaza True in cazul in care a fost gasit un imprumut cu id-ul dat
        :param id_imprumut:
        :return:
        """
        return self._lista_imprumuturi.get(id_imprumut, None)

    def find_by_id_client(self, id_client):
        """
        returneaza True in cazul in care a fost gasit un imprumut cu id-ul dat
        :param id_client:
        :return:
        """
        return self._lista_imprumuturi.get(id_client, None)

    def find_by_id_carte(self, id_carte):
        """
        returneaza True in cazul in care a fost gasit un imprumut cu id-ul dat
        :param id_carte:
        :return:
        """
        return self._lista_imprumuturi.get(id_carte, None)

    def get_by_id_client(self, id_client):
        """
        returneaza imprumutul cu id-ul daca, in cazul in care exsta
        :param id_client:
        :return:
        :raise: arunca o eroare in cazul in care acest id nu exista
        """
        if self.find_by_id_client(id_client) is None:
            raise KeyError("Acest imprumut nu exista!")
        return self._lista_imprumuturi[id_client]

    def get_by_id_carte(self, id_carte):
        """

        :param id_carte:
        :return:
        """
        if self.find_by_id_carte(id_carte) is None:
            raise KeyError("Acest imprumut nu exista!")
        return self._lista_imprumuturi[id_carte]

    def sterge_definitiv(self, id_imprumut):
        """
        sterge un imprumut definitiv din lista de imprumuturi. Asta se intampla de obicei
        cand este sters un client sau o carte din listele respective
        :param imprumut:
        :return:
        """
        self._lista_imprumuturi.pop(id_imprumut)

    def adauga(self, imprumut):
        """
        adauga un nou imprumut in lista de imprumuturi
        :param imprumut:
        :return:
        """
        if self.find_by_id_imprumut(imprumut.get_id_imprumut()) is None:    # verifica ca id ul introdus sa nu fie folosit
            if self.find_by_id_client(imprumut.get_id_client()) is None:    # cazul in care nu exista acest client
                self._lista_imprumuturi[imprumut.get_id_imprumut()] = imprumut         # se creeaza un imprumut
                self._lista_imprumuturi[imprumut.get_id_imprumut()].set_nr_exemplare(1)
            else:                                                           # cazul in ca exista acest client
                if self.find_by_id_carte(imprumut.get_id_carte()) is None:  # cazul in care clientul nu a imprumutat cartea
                    self._lista_imprumuturi[imprumut.get_id_imprumut()] = imprumut     #se creeaza un nou imprumut
                    self._lista_imprumuturi[imprumut.get_id_imprumut()].set_nr_exemplare(1)
                else:                                                           # cazul in care clientul a imprumutat deja aceasta carte
                    ok = 0
                    for imprumut2 in self._lista_imprumuturi.values():
                        if imprumut2.get_id_client() == imprumut.get_id_client() and imprumut2.get_id_carte() == imprumut.get_id_carte():
                            imprumut = imprumut2
                            ok = 1
                            break
                    if ok == 1:
                        self._lista_imprumuturi[imprumut.get_id_imprumut()].set_nr_exemplare(imprumut.get_nr_exemplare()+ 1)
                    else:
                        self._lista_imprumuturi[imprumut.get_id_imprumut()] = imprumut  # se creeaza un nou imprumut
                        self._lista_imprumuturi[imprumut.get_id_imprumut()].set_nr_exemplare(1)
        else:
            raise KeyError("Exista deja acest id")

    def sterge(self, id_client, id_carte):
        """
        sterge un imprumut dupa id-ul clientului si id-ul cartii
        :param id_client:
        :param id_carte:
        :return:
        """

        if self.find_by_id_client(id_client) is None:
            raise KeyError("Acest Client nu a imprumutat carti")
        else:
            ok = 0
            imprumut = self.get_by_id_client(id_client)
            for imprumut in self._lista_imprumuturi.values():
                if imprumut.get_id_client() == id_client and imprumut.get_id_carte() == id_carte:
                    ok = 1
                    break
            if ok == 1:
                imprumut.set_nr_exemplare(imprumut.get_nr_exemplare()-1)
                if imprumut.get_nr_exemplare() < 0:
                    imprumut.set_nr_exemplare(0)
                self._lista_imprumuturi[imprumut.get_id_imprumut()] = imprumut
