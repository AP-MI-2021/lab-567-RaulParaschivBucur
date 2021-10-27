# 2
from Domain.Cheltuiala2 import get_nr_apartament


def stergere_toate_chelt(lst_cheltuieli, nr_apartament: int):
    """
    Sterge toate cheltuielile pt un anumi apartament
    :param lst_cheltuieli: lista de cheltuieli
    :param nr_apartament: numarul apartamentului caruia vrem sa ii stergem toate cheltuielile
    :return: lista lst_cheltuieli fara cheltuielile cu numarul de apartament nr_apartament
    """
    result_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            result_lst.append(cheltuiala)

    return result_lst
