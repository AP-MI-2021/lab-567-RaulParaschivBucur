from Domain.Cheltuiala2 import get_tip_cheltuiala, get_suma


def max_suma_chelt_pt_fiecare_tip_chelt(lst_cheltuieli):
    """
    Afla suma maxima cheltuita pt fiecare tip de cheltuiala
    :param lst_cheltuieli: Lista de cheltuieli
    :return: o lista cu tupluri de forma: (x,y) unde:
            - x --> tipul cheltuielii
            - y --> suma maxima cheltuita pt acel tip de cheltuiala
    """
    result_lst = []
    for c1 in lst_cheltuieli:
        maxim = get_suma(c1)
        tuplu = (get_tip_cheltuiala(c1), maxim)
        for c2 in lst_cheltuieli:
            if (get_suma(c2) > maxim) and (get_tip_cheltuiala(c1) == get_tip_cheltuiala(c2)):
                maxim = get_suma(c2)
                tuplu = (get_tip_cheltuiala(c2), maxim)
        if tuplu not in result_lst:
            result_lst.append(tuplu)

    return result_lst


def afiseaza_max_chelt(lst):
    for elem in lst:
        print(f'Tip cheltuiala: {elem[0]}, cea mai mare cheltuiala: {elem[1]}')
