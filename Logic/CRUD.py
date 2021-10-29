from Domain.Cheltuiala2 import creeaza_cheltuiala, get_id


def create(lst_cheltuieli, nr_apartament: int, id_cheltuiala: int, suma, data, tip_cheltuiala):
    """
    Creaza o noua cheltuiala
    :param nr_apartament: numarul apartamentului, NU trebuie sa fie unic
    :param id_cheltuiala: id-ul cheltuielii, trebuie sa fie unic
    :param suma: suma cheltuita, nenula
    :param data: data cheltuielii
    :param tip_cheltuiala: tipul cheltuielii
    :return: o cheltuiala formata din lst_cheltuieli la care se adauga o noua cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament, id_cheltuiala, suma, data, tip_cheltuiala)

    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int = None):
    """
    Citeste o cheltuiala  din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii pe care vrem sa o citim
    :return: cheltuiala apartamentului cu id-ul id_cheltuiala sau lista cu toate cheltuielile daca id_cheltuiala=None
    """
    cheltuiala_ap_cu_id = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_ap_cu_id = cheltuiala

    if cheltuiala_ap_cu_id is None:
        return lst_cheltuieli
    else:
        return cheltuiala_ap_cu_id


def update(lst_cheltuieli, new_cheltuiala):
    """
    Modifica o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param new_cheltuiala: cheltuiala care se va modifica
    :return: o lista cu cheltuiala actualizata
    """
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_lst_cheltuieli.append(cheltuiala)
        else:
            new_lst_cheltuieli.append(new_cheltuiala)

    return new_lst_cheltuieli


def delete(lst_cheltuieli, id_cheltuiala: int):
    """
    Sterge o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista da cheltuieli
    :param id_cheltuiala: id-ul cheltuielii pe care vrem sa o stergem
    :return: lista lst_cheltuieli fara cheltuiala cu id-ul id_cheltuiala
    """
    result_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            result_lst.append(cheltuiala)

    return result_lst
