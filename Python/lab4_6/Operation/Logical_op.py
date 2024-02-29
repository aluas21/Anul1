from Domain import Calatorii
from Operation import Terminal

#----------------ADAUGARE----------------

def modificare(cod, lista_calatorii):
    """
    Modifica o calatorie din lista dupa un anumit cod
    :param cod (int): codul unic al unei calatorii
    :param lista_calatorii (list): lista in care se modifica o calatorie
    :return: lista noua
    """
    calatorie = Terminal.citire_calatorie_noua(cod)
    for i in range(0, len(lista_calatorii)):
        if Calatorii.get_cod(lista_calatorii[i]) == cod:
            Calatorii.update_calatorii(lista_calatorii, i, calatorie)
    return lista_calatorii


#---------------STERGERE-----------------
def del_destination(destination, lista_calatorii):
    """
    Sterge toate calatoriile care au o destinatie data
    :param destination (str): destinatia data
    :param lista_calatorii (list): lista ce urmeaza sa fie modificata
    :return: lista noua
    """
    i = 0
    while i < len(lista_calatorii):
        if Calatorii.get_destination(lista_calatorii[i]) == destination:
            del lista_calatorii[i]
            i -= 1
        i += 1
    return lista_calatorii

def del_durata(durata, lista_calatorii):
    """
    Sterge calatoriile cu o durata mai mica decat cea data
    :param durata (int): durata introdusa de utilizator
    :param lista_calatorii (list): lista ce urmeaza sa fie modificata
    :return: lista noua
    """
    i = 0
    while i < len(lista_calatorii):
        if Calatorii.get_time_out(lista_calatorii[i]) - Calatorii.get_time_in(lista_calatorii[i]) < int(durata):
            del lista_calatorii[i]
            i -= 1
        i += 1
    return lista_calatorii

def del_price(price, lista_calatorii):
    """
    Sterge calatoriile care au un pret mai mare decat cel dat
    :param price (float): pretul dat
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :return:
    """
    i = 0
    while i < len(lista_calatorii):
        if Calatorii.get_price(lista_calatorii[i]) > int(price):
            del lista_calatorii[i]
            i -= 1
        i += 1
    return lista_calatorii


#--------------CAUTARE-----------------
def cautare_interval(time_in, time_out, lista_calatorii):
    """

    Afiseaza calatoriile cu intervalul cuprins intr-un interval dat
    :param time_in (int): timpul de inceput
    :param time_out (int): timpul de inceput
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :return:
    """
    new_lista_calatorii = []
    for i in range(0,len(lista_calatorii)):
        if Calatorii.get_time_in(lista_calatorii[i]) >= int(time_in) and Calatorii.get_time_out(lista_calatorii[i]) <= int(time_out):
            new_lista_calatorii.append(lista_calatorii[i])
    return new_lista_calatorii

def cautare_dest_pret(destination, price, lista_calatorii):
    """
    Afiseaza calatoriilor care au destinatia cea introdusa si pretul mai mic decat cel dat
    :param destination: destinatia data
    :param price (float): pretul dat
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :return:
    """
    new_lista_calatorii = []
    for i in range(0,len(lista_calatorii)):
        if Calatorii.get_destination(lista_calatorii[i]) == destination and Calatorii.get_price(lista_calatorii[i]) <= price:
            new_lista_calatorii.append(lista_calatorii[i])
    return new_lista_calatorii

def cautare_time_out(time_out,lista_calatorii):
    """
    Afisarea pachetelor care au o data de sfarsit mai mica decat cea introdusa
    :param time_out: timpul de sfarsit introdus
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :return:
    """
    new_lista_calatorii = []
    for i in range(0, len(lista_calatorii)):
        if Calatorii.get_time_out(lista_calatorii[i]) <= time_out:
            new_lista_calatorii.append(lista_calatorii[i])
    return new_lista_calatorii


#-----------RAPOARTE/TIPARIRE-----------
def numb_destination(destination,lista_calatorii):
    """
    Returneaza numarul de calatorii care au o destinatie data
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :param destination: destinatia data
    :return:
    """
    nr_destionation = 0
    for i in range(0, len(lista_calatorii)):
        if Calatorii.get_destination(lista_calatorii[i]) == destination:
            nr_destionation += 1
    return nr_destionation

def dest_price_sort(lista_calatorii, time_start, time_end):
    """
    Sorteaza dupa pret pachetele care sunt intr-un interval introdus de la tastatura
    :param lista_undo:
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :param time_start (int): timpul de inceput introdus
    :param time_end (int): timpul de sfarsit introdus
    :return:
    """
    new_lista_calatorii = lista_calatorii
    for i in range (0, len(new_lista_calatorii)-1):
        for j in range (0,len(new_lista_calatorii)):
            if Calatorii.get_price(new_lista_calatorii[i]) > Calatorii.get_price(new_lista_calatorii[j]):
                aux = new_lista_calatorii[i]
                new_lista_calatorii[i] = new_lista_calatorii[j]
                new_lista_calatorii[j] = aux
    for i in range(0, len(new_lista_calatorii)):
        if Calatorii.get_time_in(new_lista_calatorii[i]) < time_start or Calatorii.get_time_out(new_lista_calatorii[i]) > time_end:
            del new_lista_calatorii[i]
    return new_lista_calatorii

def average_price_destination(lista_calatorii, destination):
    """
    Returneaza pretul mediu pe o anumita destinatie
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :param destination: destinatia data
    :return:
    """
    total_price = 0
    for i in range(0, len(lista_calatorii)):
        if Calatorii.get_destination(lista_calatorii[i]) == destination:
            total_price += Calatorii.get_price(lista_calatorii[i])
    return float(total_price/numb_destination(lista_calatorii,destination))


#----------------FILTRARE-------------
def big_price_dif_destination(lista_calatorii, price, destination):
    """
    Sterge calatoriile cu pretul mai mare decat dat si cu o destinatie diferita de cea introdusa
    :param lista_undo:
    :param lista_calatorii: lista ce urmeaza sa fie modificata
    :param price (float): pretul introdus
    :param destination: destinatia data
    :return:
    """
    for i in range(0, len(lista_calatorii)):
        if Calatorii.get_price(lista_calatorii[i]) < price or Calatorii.get_destination(lista_calatorii) == destination:
            del lista_calatorii[i]
            i -= 1
    return lista_calatorii

#-----------------UNDO----------------