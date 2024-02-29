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

def citire_calatorie_noua(cod):
    new_time_start = int(input("Data inceput: "))
    new_time_end = int(input("Data sfarsit: "))
    new_destination = input("Destinatie: ")
    new_price = float(input("Pret: "))
    calatorie = Calatorii.create_calatorie(cod,new_time_start,new_time_end,new_destination,new_price)
    return calatorie
