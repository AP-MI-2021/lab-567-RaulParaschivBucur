from Domain.Cheltuiala import creeaza_cheltuiala, get_nr_apartament


def create(lst_cheltuieli, nr_apartament: int, suma, data, tip_cheltuiala):
    """
    Creaza o noua cheltuiala
    :param nr_apartament: numarul apartamentului, trebuie sa fie unic
    :param suma: suma cheltuita, nenula
    :param data: data cheltuielii
    :param tip_cheltuiala: tipul cheltuielii
    :return: o cheltuiala formata din lst_cheltuieli la care se adauga o noua cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament, suma, data, tip_cheltuiala)

    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, nr_apartament: int=None):
    """
    Citeste o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param nr_apartament: nr apartamentului dorit
    :return: cheltuiala apartamentului cu numarul nr_apartament sau lista cu toate cheltuielile daca nr_apartament=None
    """
    cheltuiala_ap_cu_nr = None
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_ap_cu_nr = cheltuiala

    if cheltuiala_ap_cu_nr is None:
        return lst_cheltuieli
    else:
        return cheltuiala_ap_cu_nr


def update(lst_cheltuieli, new_cheltuiala):
    """
    Modifica o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param nr_apartament: cheltuiala care se va amodifica, nr apartamentului trebuie sa fie unul existent
    :return: o lista cu cheltuiala actualizata
    """
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != get_nr_apartament(new_cheltuiala):
            new_lst_cheltuieli.append(cheltuiala)
        else:
            new_lst_cheltuieli.append(new_cheltuiala)

    return new_lst_cheltuieli


def delete(lst_cheltuieli, nr_apartament: int):
    """
    Sterge o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista da cheltuieli
    :param nr_apartament: nr apartamentului pe care vrem sa il stergem
    :return: lista lst_cheltuieli fara cheltuiala cu numarul nr_apartament
    """
    result_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            result_lst.append(cheltuiala)

    return result_lst
