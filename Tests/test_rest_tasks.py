from Logic.CRUD import read
from Logic.rest_tasks import stergere_toate_chelt
from Tests.test_CRUD import get_dat3


def test_sterge_toate_chelt():
    lst_cheltuieli = get_dat3()
    nr_chelt_de_sters = 4
    chelt_de_sters = read(lst_cheltuieli, nr_chelt_de_sters)
    deleted = stergere_toate_chelt(lst_cheltuieli, nr_chelt_de_sters)

    assert chelt_de_sters not in deleted


def test_rest_tasks():
    test_sterge_toate_chelt()
