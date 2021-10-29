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


def get_nr_apartament(Cheltuiala):
    """
    Getter pt numarul apartamentului
    :param Cheltuiala: o cheltuiala
    :return: numarul apartamentului aferent cheltuielii date ca parametru
    """
    return Cheltuiala[0]


def get_id(Cheltuiala):
    """
    Getter pt id-ul cheltuielii
    :param Cheltuiala: o cheltuiala
    :return: id-ul cheltuielii
    """
    return Cheltuiala[1]


def get_suma(Cheltuiala):
    """
    Getter pt suma cheltuita
    :param Cheltuiala: o cheltuiala
    :return: suma cheltuita
    """
    return Cheltuiala[2]


def get_data(Cheltuiala):
    """
    Getter pt data cheltuielii
    :param Cheltuiala: o cheltuiala
    :return: data cheltuielii date ca parametru
    """
    return Cheltuiala[3]


def get_tip_cheltuiala(Cheltuiala):
    """
    Getter pt tipul cheltuielii
    :param Cheltuiala: o cheltuiala
    :return: tipul cheltuielli date ca parametru
    """
    return Cheltuiala[4]


def get_str(Cheltuiala):
    """
    Getter pt mesajul cu continutul cheltuielii
    """
    return f'Cheltuiala apartament nr: {get_nr_apartament(Cheltuiala)} // ID-ul: {get_id(Cheltuiala)} // suma cheltuita: {get_suma(Cheltuiala)} // in data: {get_data(Cheltuiala)} // Tipul cheltuielii: {get_tip_cheltuiala(Cheltuiala)}'
