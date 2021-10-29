from Domain.Cheltuiala2 import get_data


def adunare_valoare(lst_cheltuieli, valoare: float, data: str):
    """
    Aduna o valoare la toate cheltuielile din o data calendaristica
    :param lst_cheltuieli: Lista de cheltuieli
    :param valoare: Valoarea care trebuie adunata
    :param data: Data calendaristica a cheltuielilor asupra carora vom aduna valoarea
    :return: Lista in care fiecare cheltuiala din data aleasa are valoarea valoare adunata sumei sale cheltuite
    """
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala[2] += valoare

    return lst_cheltuieli
