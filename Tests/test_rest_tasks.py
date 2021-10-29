from Domain.Cheltuiala2 import get_nr_apartament, creeaza_cheltuiala
from Logic.Del_all import stergere_toate_chelt
from Logic.Sort_desc import sortare_desc_dupa_suma
from Tests.test_CRUD import get_dat3


def test_sterge_toate_chelt():
    lst_cheltuieli = get_dat3()
    nr_ap_chelt_de_sters = 4
    deleted = stergere_toate_chelt(lst_cheltuieli, nr_ap_chelt_de_sters)
    ok = True
    for cheltuiala in deleted:
        if get_nr_apartament(cheltuiala) == nr_ap_chelt_de_sters:
            ok = False
    assert ok


def test_sortare_desc_dupa_suma():
    lst_cheltuieli = [creeaza_cheltuiala(4, 1005, 670, 2021-10-7, 'Intretinere'),
                      creeaza_cheltuiala(2, 1001, 2900, 2021-12-11, 'Canal'),
                      creeaza_cheltuiala(2, 1002, 9900, 2021-12-11, 'Intretinere'),
                      creeaza_cheltuiala(4, 1004, 1670, 2021-10-7, 'Canal')]

    lst_dupa_sortare = [
        creeaza_cheltuiala(2, 1002, 9900, 2021-12-11, 'Intretinere'),
        creeaza_cheltuiala(2, 1001, 2900, 2021-12-11, 'Canal'),
        creeaza_cheltuiala(4, 1004, 1670, 2021-10-7, 'Canal'),
        creeaza_cheltuiala(4, 1005, 670, 2021-10-7, 'Intretinere')]

    result = sortare_desc_dupa_suma(lst_cheltuieli)
    assert result == lst_dupa_sortare


def test_rest_tasks():
    test_sterge_toate_chelt()
    test_sortare_desc_dupa_suma()
