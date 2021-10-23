def creeaza_cheltuiala(nr_apartament: int, suma, data, tip_cheltuiala):
    """
    :param nr_apartament: numarul apartamentului, NU trebuie sa fie unic
    :param suma: suma cheltuita, nenula
    :param data: data cheltuielii
    :param tip_cheltuiala: tipul cheltuielii
    :return: o cheltuiala
    """
    return {
        'nr_ap': nr_apartament,
        'suma': suma,
        'data': data,
        'tip_chelt': tip_cheltuiala
    }


def get_nr_apartament(Cheltuiala):
    """
    Getter pt numarul apartamentului
    :param Cheltuiala: o cheltuiala
    :return: numarul apartamentului aferent cheltuielii date ca parametru
    """
    return Cheltuiala['nr_ap']


def get_suma(Cheltuiala):
    """
    Getter pt suma cheltuita
    :param Cheltuiala: o cheltuiala
    :return: suma cheltuita
    """
    return Cheltuiala['suma']


def get_data(Cheltuiala):
    """
    Getter pt data cheltuielii
    :param Cheltuiala: o cheltuiala
    :return: data cheltuielii date ca parametru
    """
    return Cheltuiala['data']


def get_tip_cheltuiala(Cheltuiala):
    """
    Getter pt tipul cheltuielii
    :param Cheltuiala: o cheltuiala
    :return: tipul cheltuielli date ca parametru
    """
    return Cheltuiala['tip_chelt']


def get_str(Cheltuiala):
    """
    Getter pt mesajul cu continutul cheltuielii
    """
    return f'Cheltuiala apartament nr: {get_nr_apartament(Cheltuiala)} // suma cheltuita: {get_suma(Cheltuiala)} // in data: {get_data(Cheltuiala)} // Tipul cheltuielii: {get_tip_cheltuiala(Cheltuiala)}'
