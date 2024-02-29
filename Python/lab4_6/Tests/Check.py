from Operation import Logical_op
def check_all():
    check_del_destination()
    check_del_durata()
    check_numb_destination()
    check_dest_price_sort()
    check_cautare_time_out()
    check_cautare_dest_pret()

def check_del_destination():
    assert Logical_op.del_destination('2',[{'cod': 1, 'time_start': 1, 'time_end': 1, 'destination': '1', 'price': 1.0}, {'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}]) == [{'cod': 1, 'time_start': 1, 'time_end': 1, 'destination': '1', 'price': 1.0}]
    assert Logical_op.del_destination('11',[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 1, 'time_start': 1, 'time_end': 1, 'destination': '11', 'price': 1.0}]) == [{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}]

def check_del_durata():
    assert Logical_op.del_durata(6,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]) ==[{'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]
    assert Logical_op.del_durata(1,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]) == [{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]

def check_del_price():
    #!!!!!
    assert Logical_op.del_price(35,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 64.0}]) ==[{'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]
    assert Logical_op.del_price(100,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]) == [{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]

def check_cautare_interval():
    assert Logical_op.cautare_interval(10,13,[{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}, {'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3', 'price': 3.0}]) ==[{'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3', 'price': 3.0}]
    assert Logical_op.cautare_interval(5,17,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]) == [{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]

def check_cautare_dest_pret():
    assert Logical_op.cautare_dest_pret('2',100,[{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}, {'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3', 'price': 200.0}]) ==[{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}]
    assert Logical_op.cautare_dest_pret('12',45,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '7', 'price': 32.0}]) == [{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}]

def check_cautare_time_out():
    assert Logical_op.cautare_time_out(2,[{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}, {'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3', 'price': 3.0}]) == [{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}]
    assert Logical_op.cautare_time_out(100,[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 1, 'time_start': 1, 'time_end': 1, 'destination': '11', 'price': 1.0}]) == [{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 1, 'time_start': 1, 'time_end': 1, 'destination': '11', 'price': 1.0}]


def check_numb_destination():
    assert Logical_op.numb_destination('12',[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]) == 2
    assert Logical_op.numb_destination('789',[{'cod': 2, 'time_start': 10, 'time_end': 12, 'destination': '12', 'price': 32.0}, {'cod': 3, 'time_start': 6, 'time_end': 13, 'destination': '12', 'price': 32.0}]) == 0

def check_dest_price_sort():
    assert Logical_op.dest_price_sort([{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0},{'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3','price': 3.0}],1,100) == [{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0},{'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3', 'price': 3.0}]
    assert Logical_op.dest_price_sort([{'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3','price': 3.0}, {'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0}],1,100) == [{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0},{'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3', 'price': 3.0}]

def check_average_price_destination():
    #!!!!!
    assert Logical_op.average_price_destination([{'cod': 2, 'time_start': 2, 'time_end': 2, 'destination': '2', 'price': 2.0},{'cod': 3, 'time_start': 3, 'time_end': 3, 'destination': '3','price': 3.0}],'2') == 2.0

def check_big_price_dif_destination():
    ...