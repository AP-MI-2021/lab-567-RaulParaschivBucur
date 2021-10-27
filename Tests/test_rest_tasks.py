from Domain.Cheltuiala2 import get_nr_apartament
from Logic.CRUD import read
from Logic.rest_tasks import stergere_toate_chelt
from Tests.test_CRUD import get_dat3


# necesita modificari
def test_sterge_toate_chelt():
    lst_cheltuieli = get_dat3()
    nr_ap_chelt_de_sters = 4
    deleted = stergere_toate_chelt(lst_cheltuieli, nr_ap_chelt_de_sters)
    ok = True
    for cheltuiala in deleted:
        if get_nr_apartament(cheltuiala) == nr_ap_chelt_de_sters:
            ok = False
    assert ok


def test_rest_tasks():
    test_sterge_toate_chelt()
