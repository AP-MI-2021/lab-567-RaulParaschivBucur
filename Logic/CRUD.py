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
    if read(lst_cheltuieli, id_cheltuiala) is not None:
        raise ValueError(f'Exista deja o cheltuiala cu ID-ul {id_cheltuiala}')

    cheltuiala = creeaza_cheltuiala(nr_apartament, id_cheltuiala, suma, data, tip_cheltuiala)

    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int = None):
    """
    Citeste o cheltuiala  din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii pe care vrem sa o citim
    :return: - cheltuiala apartamentului cu id-ul id_cheltuiala, daca exista
             - lista cu toate cheltuielile daca id_cheltuiala = None
             - None daca nu exista o cheltuiala cu id_cheltuiala
    """
    if not id_cheltuiala:
        return lst_cheltuieli

    cheltuiala_ap_cu_id = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_ap_cu_id = cheltuiala

    if cheltuiala_ap_cu_id:
        return cheltuiala_ap_cu_id
    return None


def update(lst_cheltuieli, new_cheltuiala):
    """
    Modifica o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param new_cheltuiala: cheltuiala care se va modifica
    :return: o lista cu cheltuiala actualizata
    """
    if read(lst_cheltuieli, get_id(new_cheltuiala)) is None:
        raise ValueError(f'NU exista o cheltuiala cu ID-ul {get_id(new_cheltuiala)} pe care sa o actualizam')

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
    if read(lst_cheltuieli, id_cheltuiala) is None:
        raise ValueError(f'NU exista o cheltuiala cu ID-ul {id_cheltuiala} pe care sa o stergem')

    result_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            result_lst.append(cheltuiala)

    return result_lst
