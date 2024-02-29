def create_calatorie(cod,time_start, time_end, destination, price):
    """

    :param cod:
    :param time_start:
    :param time_end:
    :param destination:
    :param price:
    :return:
    """
    return {
        "cod" : cod,
        "time_start": time_start,
        "time_end": time_end,
        "destination": destination,
        "price": price
    }

def update_calatorii(lista_calatorii, i, calatorie):
    lista_calatorii[i] = calatorie

#----------Functii SET------------
def set_cod(calatorie, cod):
    calatorie["cod"] = cod

def set_time_start(calatorie, time_start):
    calatorie["time_start"] = time_start

def set_time_end(calatorie, time_end):
    calatorie["time_end"] = time_end

def set_destination(calatorie, destination):
    calatorie["destination"] = destination

def set_price(calatorie, price):
    calatorie["price"] = price


#-----------Functii GET-------------
def get_cod(calatorie):
    return calatorie["cod"]

def get_time_in(calatorie):
    return calatorie["time_start"]

def get_time_out(calatorie):
    return calatorie["time_end"]

def get_destination(calatorie):
    return calatorie["destination"]

def get_price(calatorie):
    return calatorie["price"]

def add_calatorie(lista_calatorii, calatorie):
    lista_calatorii.append(calatorie)
