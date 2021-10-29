from Domain.Cheltuiala2 import get_suma


def sortare_desc_dupa_suma(lst_cheltuieli):
    """
    Sorteaza cheltuielile din lst_cheltuieli dupa suma cheltuita
    """
    return sorted(lst_cheltuieli, key=get_suma, reverse=True)
