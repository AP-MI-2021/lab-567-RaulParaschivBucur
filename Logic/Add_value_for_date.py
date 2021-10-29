from Domain.Cheltuiala2 import get_data


# read dupa data cheltuielii
def read(lst_cheltuieli, data: str = None):
    """
    Citeste o cheltuiala  din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii pe care vrem sa o citim
    :return: - cheltuiala apartamentului cu id-ul id_cheltuiala, daca exista
             - lista cu toate cheltuielile daca id_cheltuiala = None
             - None daca nu exista o cheltuiala cu id_cheltuiala
    """
    if not data:
        return lst_cheltuieli

    cheltuiala_ap_cu_data = None
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala_ap_cu_data = cheltuiala

    if cheltuiala_ap_cu_data:
        return cheltuiala_ap_cu_data
    return None


def adunare_valoare(lst_cheltuieli, valoare: float, data: str):
    """
    Aduna o valoare la toate cheltuielile din o data calendaristica
    :param lst_cheltuieli: Lista de cheltuieli
    :param valoare: Valoarea care trebuie adunata
    :param data: Data calendaristica a cheltuielilor asupra carora vom aduna valoarea
    :return: Lista in care fiecare cheltuiala din data aleasa are valoarea valoare adunata sumei sale cheltuite
    """
    if read(lst_cheltuieli, data) is None:
        raise ValueError(f'Nu exista cheltuieli in data {data} carora sa le adunam valoarea aleasa')

    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala[2] += valoare

    return lst_cheltuieli
