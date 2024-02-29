def read_list(sir, lungime):
    for i in range (0,lungime):
        sir[i] = int(input("elementul " + str(i+1) + ":"))

def same_digits(a, b):
    """
    Subprogramul returneaza 1 daca cei doi parametri contin aceleasi cifre, indiferent de numarul
    lor de aparitii, si 0 in caz contrar
    :param a: int
    :param b: int
    :return: int
    """
    x = [0]*11         # se initializeaza doi vectori de frecventa pentru cifrele celor doi parametrii
    y = [0]*11
    a1 = a
    b1 = b
    while a1 != 0:          # cu ajutorul vectorilor de frecventa retinem aparitia fiecarei cifre din parametri
        x[int(a1%10)] = 1
        a1 = a1 / 10

    while b1 != 0:
        y[int(b1%10)] = 1
        b1 = b1 / 10

    i = 0
    while i <= 9:           # se parcurg cei doi vectori de frecventa iar daca nu doi termeni sunt diferiti
        if x[i] != y[i]:    # insemana ca cei doi p parametri nu au aceleasi cifre
            return 0
        i += 1
    return 1

"""SUBPROGRAME 15 16"""


"""
+----+------------------------------------------------------------------------------+--+--+--+
| T1 | Determinare secventa de lungime maxima formata dintr-un sir strict crescator |  |  |  |
|    | care este urmat de un sir descrescator (sau secventa munte)                  |  |  |  |
+----+------------------------------------------------------------------------------+--+--+--+
| T2 | Computer implementation: init, add, and total                                |  |  |  |
+----+------------------------------------------------------------------------------+--+--+--+
| T3 | User interface implementation                                                |  |  |  |
+----+------------------------------------------------------------------------------+--+--+--|
"""
def secv_up_down(sir,length):
    """
    Subprogramul returneaza secventa de lungime maxima formata dintr-un sir strict crescator
    care este urmat de un sir descrescator (sau secventa munte)
    :param sir: dictionary
    :param length: int
    :return: lg_max: int
    """
    cresc = 0
    desc = 0
    lg = 1              # retine lungimea curenta
    lg_max = 0          # retine lungimea maxim
    ok = 0              # verifica daca exista cel putin o astfel de secventa care sa indeplineasca conditia
    for i in range(0, length - 1):
        if sir[i] < sir[i+1]:           # daca doua el. consec. sunt crescatoare
            if desc == 1:               # se verfica daca cele anteriore nu au fost descrescatoare
                desc = 0
                ok = 1
                if lg > lg_max:         # se salveaza lungimea maxima daca este cazul
                    lg_max = lg
                lg = 2                  # in caz afiramtiv se intializeaza un al sir
            else:
                if cresc == 1:          # daca nu a existat un sir desc. acesta creste lungimea sirului crescator
                    lg += 1
                else:
                    cresc = 1           # in cazul in care aceasta secventa crescatoare nu a existat, se initializeaza
                    lg = 2
        else:
            if sir[i] > sir[i+1] and cresc == 1:    # in cazul in care sirul descreste si a crescut cel ptuin odata
                lg += 1                             # se adauga lungimii curente secventa descrescatore
                ok = 1
                desc = 1
    if ok == 0:
        return 0                        # se retuneaza 0 in cazul in care nu a fost gasita o astfel de secventa
    if lg > lg_max and desc == 1:       # se verifica si ultima secventa
        lg_max = lg
    return lg_max

"""
+----+------------------------------------------------------------------------------+--+--+--+
| T1 | Determinare lungimea maxima a secventei in care termenii contin aceleasi cif |  |  |  |
+----+------------------------------------------------------------------------------+--+--+--+
| T2 | Computer implementation: init, add, and total                                |  |  |  |
+----+------------------------------------------------------------------------------+--+--+--+
| T3 | User interface implementation                                                |  |  |  |
+----+------------------------------------------------------------------------------+--+--+--|"""
def secv_same_digits(sir, lungime):
    """
    Subprogramul returneaza lungimea maxima a secventei in care termenii contin aceleasi cifre
    :param sir: dictionary
    :param lungime: int
    :return: lg_max: int
    """
    lg = 1
    lg_max = 0
    ok = 0
    for i in range(0, lungime - 1):             # se parcurge sirul pana la penultima valoare deoarece
        if same_digits(sir[i],sir[i+1]):        # se verifica pentru fiecare termen daca are aceleasi cifre urmatorul termen
            lg += 1
            ok = 1
        else:
            if lg_max < lg:                     # in caz contrar se actualizeaza lungimea maxima daca este cazul
                lg_max = lg
            lg = 1
    if ok == 0:
        return 0
    if lg_max < lg:
        lg_max = lg
    return lg_max

def secv_sub_zero(sir, length):
    lg = 0
    lg_max = 0
    i = 0
    while sir[i] >= 0 and i < length-1:         # se cauta primul element negativ din sir, daca exista
        i += 1
    ok = 0
    if sir[i] < 0:                              # daca s-a gasit un element negativ se initializeaza sirul
        ok = 1
        lg = 1
    for j in range (i+1, length):               # se parcurg elementele de la primul element negativ gasit
        if sir[j] < 0:                          # se verifica daca acesta este negativ
            lg += 1                             # in caz afirmativ, lungimea curenta creste
            ok = 1
        else:
            if lg_max < lg:                     # in caz contrar se actualizeaza lungimea curenta daca este cazul
                lg_max = lg
            lg = 0

    if lg_max < lg:
        lg_max = lg
    if ok == 0:
        return 0
    return lg_max

"""SUBPROGRAME TEST"""

def check_secv_up_down():
    assert secv_up_down([2,3,1,3,2,1,0], 7) == 5
    assert secv_up_down([2,3,4,4,4,4,4], 7) == 0
    assert secv_up_down([7,6,6,6,5,1,0], 7) == 0
    assert secv_up_down([7,6,6,6,1,4,3], 7) == 3
    assert secv_up_down([2,3,1,3,4,5,6], 7) == 3

def check_secv_same_digits():
    assert secv_same_digits([22,2,12,21,2122,1,0], 7) == 3
    assert secv_same_digits([2,3,4,4,6,4,4], 7) == 2
    assert secv_same_digits([7,6,6,6,5,1,0], 7) == 3
    assert secv_same_digits([60,606,9,660,60,60,606], 7) == 4
    assert secv_same_digits([1,2,7,3,4,5,6], 7) == 0

def check_secv_sub_zero():
    assert secv_sub_zero([2,-3,-1,3,-2,-1,-1], 7) == 3
    assert secv_sub_zero([2,3,4,4,4,4,4], 7) == 0
    assert secv_sub_zero([7,-6,-6,-6,-1,4,3], 7) == 4
    assert secv_sub_zero([2,3,1,3,4,5,-6], 7) == 1
    assert secv_sub_zero([-7,6,6,6,5,1,0], 7) == 1

def check_same_digits():
    assert same_digits(12,221) == 1
    assert same_digits(0,10) == 0
    assert same_digits(7,77) == 1
    assert same_digits(360,600063) == 1
    assert same_digits(12,1) == 0




"""MAIN"""
check_same_digits()
check_secv_up_down()
check_secv_same_digits()
check_secv_sub_zero()


if __name__ == '__main__':
    print("CERINTE")
    print("1. Secventa de lungime maxima formata dintr-un sir crescator, urmata de un sir descrescator")
    print("2. Secventa de lungime maxima cu numere ce contin aceleasi cifre")
    print("3. Secventa de lungime maxima ce contine numere negative")

    ok = 0
    print("ALEGETI EXERCITIUL DORIT(1, 2, 3): ")
    while ok == 0:
        ex = int(input())
        if ex == 1 or ex == 2 or ex == 3:
            ok = 1
        else:
            print("Incercati din nou, introduceti un exercitiu valid:")

    lungime = int(input("Introduceti lungimea sirului:"))
    sir = [0]*100
    read_list(sir, lungime)

    while ex != 0:
        if ex == 1:
            print("Lungimea maxima a secventei cerute este: " + str(secv_up_down(sir, lungime)))

        if ex == 2:
            print("Lungimea maxima a secventei cerute este: " + str(secv_same_digits(sir, lungime)))

        if ex == 3:
            print("Lungimea maxima a secventei cerute este: " + str(secv_sub_zero(sir, lungime)))
        print("Pentru a inchide introduceti 0, pentru a relua programul")
        ex = int(input("ALEGETI EXERCITIUL DORIT(1, 2, 3): "))
        if ex != 0:
            lungime = int(input("Introduceti lungimea sirului:"))
            sir = [0] * 100
            read_list(sir, lungime)
