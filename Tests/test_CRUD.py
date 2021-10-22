from Domain.Cheltuiala import creeaza_cheltuiala, get_nr_apartament
from Logic.CRUD import create, read, update, delete


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


def test_read():
    lst_cheltuieli = get_dat3()
    cheltuiala = lst_cheltuieli[2]

    assert read(lst_cheltuieli, get_nr_apartament(cheltuiala)) == cheltuiala
    assert read(lst_cheltuieli, None) == lst_cheltuieli


def test_update():
    lst_cheltuieli = get_dat3()
    chelt_new = creeaza_cheltuiala(2, 10, 2021-11-11, 'Tip nou')
    updated = update(lst_cheltuieli, chelt_new)

    assert chelt_new in updated
    assert chelt_new not in lst_cheltuieli
    assert len(updated) == len(lst_cheltuieli)


def test_delete():
    lst_cheltuieli = get_dat3()
    nr_chelt_de_sters = 4
    chelt_de_sters = read(lst_cheltuieli, nr_chelt_de_sters)
    deleted = delete(lst_cheltuieli, nr_chelt_de_sters)

    assert chelt_de_sters not in deleted
    assert len(deleted) == len(lst_cheltuieli) - 1
    assert chelt_de_sters in lst_cheltuieli


def test_CRUD():
    test_create()
    test_read()
    test_update()
    test_delete()
