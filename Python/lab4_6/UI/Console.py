from Operation import Logical_op
from Domain import Calatorii

def citire_calatorie(lista_calatorii):
    ok = 0;
    while ok == 0:
        ok = 1
        cod = int(input("Codul calatoriei: "))
        for calator in lista_calatorii:
            if Calatorii.get_cod(calator) == cod:
                ok = 0
        if ok == 0:
            print("Acest cod este deja folosit, incercati din nou.")

    time_start = int(input("Data inceput: "))
    time_end = int(input("Data sfarsit: "))
    destination = input("Destinatie: ")
    price = float(input("Pret: "))


    while time_start>time_end:
        print("Datele introduse nu sunt corespunzatoare, incercati iar")
        time_start = int(input("Data inceput: "))
        time_end = int(input("Data sfarsit: "))

    calatorie = Calatorii.create_calatorie(cod,time_start,time_end,destination,price)
    return calatorie

#--------AFISARI MENIU-----------
def print_lista(lista_calatorii):
    for calatorie in lista_calatorii:
        print(calatorie)

def print_opt():
    print(" 1. Adaugare calatorie")
    print(" 2. Stergere calatorie")
    print(" 3. Cautare calatorie")
    print(" 4. Rapoarte calatorii")
    print(" 5. Filtrare calatorii")
    print(" 6. Undo")
    print(" 7. Afisare Lista Calatorii")
    print(" x. Cancel")

def print_opt_1():
    print("      1. Introduceti Calatorie")
    print("      2. Modificati Calatorie")

def print_opt_2():
    print("      1. Stergere calatorii cu destinatia...")
    print("      2. Stergere calatorii cu nr de zile mai mic decat...")
    print("      3. Stergere calatorii cu pretul mai mare decat...")

def print_opt_3():
    print("      1. Afisare calatorii intre datele introduse")
    print("      2. Afisare calatorii cu destinatia si pretul dat")
    print("      3. Afisare calatorii dupa data de sfarsit")

def print_opt_4():
    print("      1. Tiparire nr calatorii dupa destinatie data")
    print("      2. Tiparire calatorii intre data introdusa in ordine crescatoare")
    print("      3. Tiparire medie de pret dupa o destinatie data")

def print_opt_5():
    print("      1. Tiparirea calatoriilor cu un preț mai mare decât cel dat")
    print("         și o destinație diferită de cea citită de la tastatură" )

def opt_1(lista_calatorii):
    print_opt_1()
    try:
        optiune2 = int(input("Alegeti optiunea dorita"))
        if optiune2 == 1:
            calatorie = citire_calatorie(lista_calatorii)
            Calatorii.add_calatorie(lista_calatorii, calatorie)
        elif optiune2 == 2:
            cod_u = int(input("Introduceti codul calatoriei"))
            Logical_op.modificare(cod_u, lista_calatorii)
    except ValueError as er:
        print("Datele introduse nu sunt corespunzatoare, incercati iar,", er)

def opt_2(lista_calatorii):
    print_opt_2()
    try:
        optiune2 = int(input("Alegeti optiunea dorita"))
        if optiune2 == 1:
            destination = input("Introduceti destinatia dorita:")
            lista_calatorii=Logical_op.del_destination(destination, lista_calatorii)
        elif optiune2 == 2:
            durata = int(input("Introduceti durata minima"))
            lista_calatorii=Logical_op.del_durata(durata, lista_calatorii)
        elif optiune2 == 3:
            pret = int(input("Introduceti pretul"))
            lista_calatorii=Logical_op.del_price(pret, lista_calatorii)
    except ValueError as er:
        print("Datele introduse nu sunt corespunzatoare, incercati iar,", er)

def opt_3(lista_calatorii):
    print_opt_3()
    try:
        optiune2 = int(input("Alegeti optiunea dorita"))
        if optiune2 == 1:
            time_in = int(input("Introduceti data inceput: "))
            time_out = int(input("Introduceti data sfarsit: "))
            print(Logical_op.cautare_interval(time_in, time_out, lista_calatorii))
        elif optiune2 == 2:
            destination = input("Introduceti destinatia: ")
            price = float(input("Introduceti pretul maxim: "))
            print(Logical_op.cautare_dest_pret(destination, price, lista_calatorii))
        elif optiune2 == 3:
            time_out = int(input("Introduceti data_sfarsit"))
            print(Logical_op.cautare_time_out(time_out, lista_calatorii))
    except ValueError as er:
        print("Datele introduse nu sunt corespunzatoare, incercati iar,", er)

def opt_4(lista_calatorii):
    print_opt_4()
    try:
        optiune2 = int(input("Alegeti optiunea dorita"))
        if optiune2 == 1:
            destination = input("Introduceti destinatia: ")
            print("Numarul de calatorii cu aceasta destinatie este " + str(Logical_op.numb_destination(destination,lista_calatorii)))
        elif optiune2 == 2:
            time_start = int(input("Introduceti data de inceput"))
            time_end = int(input("Introduceti data de sfarsit"))
            print_lista(Logical_op.dest_price_sort(lista_calatorii,time_start,time_end))
        elif optiune2 == 3:
            destination = input("Introduceti destinatia: ")
            print("Media pretului pe destinatia introdusa este: " + str(Logical_op.average_price_destination(lista_calatorii,destination)))
    except ValueError as er:
        print("Datele introduse nu sunt corespunzatoare, incercati iar,", er)

def opt_5(lista_calatorii):
    try:
        price = float(input("Introduceti pretul: "))
        destination =  input("Introduceti destinatia: ")
        lista_calatorii = Logical_op.big_price_dif_destination(lista_calatorii,price,destination)
        print_lista(lista_calatorii)
    except ValueError as er:
        print("Datele introduse nu sunt corespunzatoare, incercati iar,", er)

def start_meniu(lista_undo, lista_calatorii):
    print_opt()
    optiune = input("Selectati optiunea dorita:")
    while optiune != "x":
        if optiune == "1":
            lista_undo=[i for i in lista_calatorii]
            opt_1(lista_calatorii)
        elif optiune == "2":
            lista_undo=[i for i in lista_calatorii]
            opt_2(lista_calatorii)
        elif optiune == "3":
            lista_undo=[i for i in lista_calatorii]
            opt_3(lista_calatorii)
        elif optiune == "4":
            lista_undo=[i for i in lista_calatorii]
            opt_4(lista_calatorii)
        elif optiune == "5":
            lista_undo=[i for i in lista_calatorii]
            opt_5(lista_calatorii)
        elif optiune == "6":
            lista_calatorii = lista_undo
        elif optiune == "7":
            print_lista(lista_calatorii)

        print_opt()
        optiune = input("Selectati optiunea dorita:")


