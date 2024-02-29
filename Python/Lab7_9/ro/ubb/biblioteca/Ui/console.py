from ro.ubb.biblioteca.Domain.entities import Client, Book
from ro.ubb.biblioteca.Exceptii.duplicate_error import Duplicate_Error
from ro.ubb.biblioteca.Repository.Repository import Repository
from ro.ubb.biblioteca.Service.Carti_service import Carti_service
from ro.ubb.biblioteca.Service.Client_service import Client_service
from ro.ubb.biblioteca.Service.Clienti_carti_service import Clienti_carti_service
from ro.ubb.biblioteca.Service.Imprumuturi_service import Imprumut_service


class Consola:
    def __init__(self, clienti_service: Client_service, carti_service: Carti_service, imprumut_service : Imprumut_service, clienti_carti_service : Clienti_carti_service):
        self.__clienti_service = clienti_service
        self.__carti_service = carti_service
        self.__imprumut_service = imprumut_service
        self.__clienti_carti_service = clienti_carti_service

#---------------AFISARI---------------
    def print_lista_clienti(self):
        print("Clientii inregistrati sunt urmatorii:")
        print(*self.__clienti_service.get_all(), sep='\n')

    def print_lista_carti(self):
        print("Cartile inregistrate sunt urmatoarele:")
        print(*self.__carti_service.get_all(), sep='\n')

    def print_lista_imprumuturi(self):
        print("Imprumuturile inregistrate sunt urmatoarele:")
        print(*self.__imprumut_service.get_all(), sep='\n')

    def print_menu(self):
        print(" 1. Adaugare")
        print(" 2. Stergere")
        print(" 3. Modificare")
        print(" 4. Cautare")
        print(" 5. Imprumutare")
        print(" 6. Returnare")
        print(" 7. Cele mai imprumutate carti")
        print(" 8. Clientii in ordine alfabetica si dupa nr de carti")
        print(" 9. Primi 20% cei mai activi clienti")
        print(" a. Afisare lista clienti")
        print(" b. Afisare lista carti")
        print(" c. Afisare imprumuturi")
        print(" x. Anulare")

#--------------ADAUGARE----------------
    def adaugare_client(self):
        try:
            id = int(input("Id: "))
            nume = input("Nume: ")
            cnp = int(input("CNP: "))
            self.__clienti_service.adaugare(id, nume, cnp)
        except Duplicate_Error as e:
            print(e)

    def adaugare_carte(self):
        try:
            id = int(input("Id: "))
            titlu = input("Titlu: ")
            desc = input("Descriere: ")
            autor = input("Autor: ")
            self.__carti_service.adaugare(id, titlu, desc, autor)
        except Duplicate_Error as e:
            print(e)

    def optiune_1(self):
        print("     1. Adaugare client")
        print("     2. Adaugare carte")
        optiune = input("    Alegeti optiunea dorita")
        print(" ")
        if optiune == '1':
            self.adaugare_client()
        elif optiune == '2':
            self.adaugare_carte()
        else:
            print("Aceasta optiune nu este implementata, incercati din nou!")

#-------------STERGERE----------------
    def sterge_client(self):
        try:
            id = int(input("Introduceti id-ul clientului"))
            self.__clienti_service.stergere(id)
            self.__imprumut_service.sterge_client(id)
        except ValueError as e:
            print(e)

    def sterge_carte(self):
        try:
            id = int(input("Introduceti id-ul clientului"))
            self.__carti_service.stergere(id)
            self.__imprumut_service.sterge_carte(id)
        except ValueError as e:
            print(e)

    def optiune_2(self):
        print("     1. Sterge client")
        print("     2. Sterge carte")
        optiune = input("    Alegeti optiunea dorita")
        print("")
        if optiune == '1':
            self.sterge_client()
        elif optiune == '2':
            self.sterge_carte()
        else:
            print("Aceasta optiune nu este implementata, incercati din nou!")

#------------MODIFICARE--------------
    def modificare_client(self):
        try:
            id = int(input("ID: "))
            nume = input("Nume: ")
            cnp = int(input("Cnp: "))
            self.__clienti_service.modificare(id,nume,cnp)
        except ValueError as e:
            print(e)

    def modificare_carte(self):
        try:
            id = int(input("Id: "))
            titlu = input("Titlu: ")
            desc = input("Desc: ")
            autor = input("Autor: ")
            self.__carti_service.modificare(id, titlu, desc, autor)
        except ValueError as e:
            print(e)

    def optiune_3(self):
        print("     1. Modificare client")
        print("     2. Modificare carte")
        optiune = input("    Alegeti optiunea dorita")
        print("")
        if optiune == '1':
            self.modificare_client()
        elif optiune == '2':
            self.modificare_carte()
        else:
            print("Aceasta optiune nu este implementata, incercati din nou!")

#-------------CAUTARE------------------
    def cautare_client(self):
        try:
            id = int(input("Id client: "))
            print(self.__clienti_service.get_client(id))
        except ValueError as e:
            print(e)

    def cautare_carte(self):
        try:
            id = int(input("Id carte: "))
            print(self.__carti_service.get_carte(id))
        except ValueError as e:
            print(e)

    def optiune_4(self):
        print("     1. Cautare Client")
        print("     2. Cautare Carte")
        optiune = input("    Alegeti optiunea dorita")
        print("")
        if optiune == '1':
            self.cautare_client()
        elif optiune == '2':
            self.cautare_carte()
        else:
            print("Aceasta optiune nu este implementata, incercati din nou!")

#-------IMPRUMUTURI-------
    def optiune_5(self):
        try:
            id_imprumut = int(input("Id Imprumut : "))
            id_client = int(input("Id Client: "))
            id_carte = int(input("Id Carte: "))
            if self.__clienti_service.get_client(id_client) is not None and self.__carti_service.get_carte(id_carte) is not None:
                self.__imprumut_service.adaugare(id_imprumut, id_client, id_carte)
            else:
                print("Clientul sau cartea introdusa nu sunt inregistrate")
        except ValueError as er:
            print("Datele introduse nu sunt corecte")

#-------RETURNARE---------
    def optiune_6(self):
        try:
            id_client = int(input("Id Client: "))
            id_carte = int(input("Id Carte: "))
            self.__imprumut_service.stergere(id_client, id_carte)
        except KeyError as e:
            print(e)

#-----SORTARE-CARTI-DUPA-NR-IMPRUMUTURI----
    def optiune_7(self):
        print(self.__imprumut_service.carte_max_imprumut())

#-----SORTARE-CLIENTI-NR-CARTI-------
    def optiune_8(self):
        print(*self.__clienti_carti_service.generare_lista_sortare(), sep ='\n')

#----SORTARE-CLIENTI-CARTI-20%------
    def optiune_9(self):
        print(*self.__clienti_carti_service.clienti_activi(), sep ='\n')

#-----ADAUGARE-IN-LISTA-------
    def adauga(self):
        self.__carti_service.adaugare(1, "Ion", "Liviu", "Liviu")
        self.__carti_service.adaugare(2, "Moara", "Ioan", "nuvela")
        self.__carti_service.adaugare(3, "Plumb", "Bacovia", "Poezie")
        self.__clienti_service.adaugare(1, "Alin", 7464536576)
        self.__clienti_service.adaugare(2, "Alex", 7987867578)
        self.__clienti_service.adaugare(3, "Alin", 7987867578)
        self.__clienti_service.adaugare(4, "Maria", 6809237898)
        self.__clienti_service.adaugare(5, "Mara", 7980236983)
        self.__imprumut_service.adaugare(2, 1, 2)
        self.__imprumut_service.adaugare(1, 1, 1)
        self.__imprumut_service.adaugare(3, 2, 1)
        self.__imprumut_service.adaugare(4, 2, 2)
        self.__imprumut_service.adaugare(5, 1, 1)
        self.__imprumut_service.adaugare(6, 2, 2)
        self.__imprumut_service.adaugare(7, 3, 1)
        self.__imprumut_service.adaugare(8, 2, 1)
        self.__imprumut_service.adaugare(9, 3, 1)
        self.__imprumut_service.adaugare(10, 3, 2)
        self.__imprumut_service.adaugare(11, 2, 1)
        self.__imprumut_service.adaugare(12, 3, 3)

#-------teste-------
    def check_all_tests(self):
        self
#--------------MENIU--------------
    def meniu(self):
        #self.adauga()
        self.print_menu()
        optiune = input("Alegeti optiunea dorita")
        while True:
            if optiune == '1':
                self.optiune_1()
            elif optiune == '2':
                self.optiune_2()
            elif optiune == '3':
                self.optiune_3()
            elif optiune == '4':
                self.optiune_4()
            elif optiune == '5':
                self.optiune_5()
            elif optiune == '6':
                self.optiune_6()
            elif optiune == '7':
                self.optiune_7()
            elif optiune == '8':
                self.optiune_8()
            elif optiune == '9':
                self.optiune_9()
            elif optiune == 'a':
                self.print_lista_clienti()
            elif optiune == 'b':
                self.print_lista_carti()
            elif optiune == 'c':
                self.print_lista_imprumuturi()
            elif optiune != 'x':
                print("Aceasta optiune nu este implementata, incercati din nou!")
            elif optiune == 'x':
                break

            self.print_menu()
            optiune = input("Alegeti optiunea dorita")



