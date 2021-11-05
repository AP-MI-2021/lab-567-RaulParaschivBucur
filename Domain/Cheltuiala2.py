def creeaza_cheltuiala(nr_apartament: int, id_cheltuiala: int, suma: float, data: str, tip_cheltuiala: str):
    """
    :param nr_apartament: numarul apartamentului, NU trebuie sa fie unic
    :param id_cheltuiala: ID-ul cheltuielii, unic
    :param suma: suma cheltuita, nenula
    :param data: data cheltuielii
    :param tip_cheltuiala: tipul cheltuielii
    :return: o cheltuiala
    """

    return [nr_apartament, id_cheltuiala, suma, data, tip_cheltuiala]


def get_nr_apartament(cheltuiala):
    """
    Getter pt numarul apartamentului
    :param cheltuiala: o cheltuiala
    :return: numarul apartamentului aferent cheltuielii date ca parametru
    """
    return cheltuiala[0]


def get_id(cheltuiala):
    """
    Getter pt id-ul cheltuielii
    :param cheltuiala: o cheltuiala
    :return: id-ul cheltuielii
    """
    return cheltuiala[1]


def get_suma(cheltuiala):
    """
    Getter pt suma cheltuita
    :param cheltuiala: o cheltuiala
    :return: suma cheltuita
    """
    return cheltuiala[2]


def get_data(cheltuiala):
    """
    Getter pt data cheltuielii
    :param cheltuiala: o cheltuiala
    :return: data cheltuielii date ca parametru
    """
    return cheltuiala[3]


def get_tip_cheltuiala(cheltuiala):
    """
    Getter pt tipul cheltuielii
    :param cheltuiala: o cheltuiala
    :return: tipul cheltuielli date ca parametru
    """
    return cheltuiala[4]


def get_str(cheltuiala):
    """
    Getter pt mesajul cu continutul cheltuielii
    """
    return f'Cheltuiala apartament nr: {get_nr_apartament(cheltuiala)} // ID-ul: {get_id(cheltuiala)} // suma ' \
           f'cheltuita: {get_suma(cheltuiala)} // in data: {get_data(cheltuiala)} // Tipul cheltu' \
           f'ielii: {get_tip_cheltuiala(cheltuiala)} '
