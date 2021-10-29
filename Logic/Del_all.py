from Domain.Cheltuiala2 import get_nr_apartament


# read dupa numarul apartamentului
def read(lst_cheltuieli, nr_apartament: int = None):
    """
    Citeste o cheltuiala  din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii pe care vrem sa o citim
    :return: - cheltuiala apartamentului cu id-ul id_cheltuiala, daca exista
             - lista cu toate cheltuielile daca id_cheltuiala = None
             - None daca nu exista o cheltuiala cu id_cheltuiala
    """
    if not nr_apartament:
        return lst_cheltuieli

    cheltuiala_ap_cu_nr = None
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_ap_cu_nr = cheltuiala

    if cheltuiala_ap_cu_nr:
        return cheltuiala_ap_cu_nr
    return None


def stergere_toate_chelt(lst_cheltuieli, nr_apartament: int):
    """
    Sterge toate cheltuielile pt un anumit apartament
    :param lst_cheltuieli: lista de cheltuieli
    :param nr_apartament: numarul apartamentului caruia vrem sa ii stergem toate cheltuielile
    :return: lista lst_cheltuieli fara cheltuielile cu numarul de apartament nr_apartament
    """
    if read(lst_cheltuieli, nr_apartament) is None:
        raise ValueError(f'Nu exista un apartament cu numarul {nr_apartament} caruia sa ii stergem toate cheltuielile')

    result_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            result_lst.append(cheltuiala)

    return result_lst
