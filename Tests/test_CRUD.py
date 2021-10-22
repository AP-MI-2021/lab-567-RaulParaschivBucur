from Domain.Cheltuiala import creeaza_cheltuiala
from Logic.CRUD import create


def get_dat3():
    return [creeaza_cheltuiala(1, 200, 2021-10-11, 'Intretinere'),
            creeaza_cheltuiala(2, 2900, 2021-12-11, 'Consum'),
            creeaza_cheltuiala(3, 230, 2020-10-11, 'Canalizare'),
            creeaza_cheltuiala(4, 1670, 2021-10-7, 'Mobila'),
            creeaza_cheltuiala(5, 283, 2021-3-11, 'Gaz')]


def test_create():
    lst_cheltuieli = get_dat3()
    params = (7, 555, 2021-10-11, 'Intretinere')
    new_cheltuiala = creeaza_cheltuiala(*params)
    new_lst_cheltuieli = create(lst_cheltuieli, *params)

    assert new_cheltuiala in new_lst_cheltuieli


test_create()