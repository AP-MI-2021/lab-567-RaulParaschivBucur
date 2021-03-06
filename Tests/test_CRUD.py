from Domain.Cheltuiala2 import creeaza_cheltuiala, get_id
from Logic.CRUD import create, read, update, delete


def get_dat3():
    return [creeaza_cheltuiala(1, 1000, 200.0, '1.1.2021', 'Intretinere'),
            creeaza_cheltuiala(2, 1001, 2900.0, '1.10.1999', 'Canal'),
            creeaza_cheltuiala(2, 1002, 2900.0, '1.10.2019', 'Intretinere'),
            creeaza_cheltuiala(3, 1003, 230.0, '21.12.2020', 'Canal'),
            creeaza_cheltuiala(4, 1004, 1670.0, '21.10.2021', 'Canal'),
            creeaza_cheltuiala(4, 1005, 670.0, '21.4.2021', 'Intretinere'),
            creeaza_cheltuiala(4, 1006, 310.0, '21.4.2020', 'Alte cheltuieli'),
            creeaza_cheltuiala(5, 1007, 283.0, '9.9.2021', 'Gaz')]


def test_create():
    lst_cheltuieli = get_dat3()
    params = (7, 1020, 5555, '2021-10-11', 'Intretinere')
    new_cheltuiala = creeaza_cheltuiala(*params)
    new_lst_cheltuieli = create(lst_cheltuieli, *params)

    assert new_cheltuiala in new_lst_cheltuieli
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli) + 1

    # testam daca se afiseaza exceptie pt ID duplicat
    params2 = (7, 1020, 234, 'Ceva data', 'Ceva')
    try:
        _ = create(new_lst_cheltuieli, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    lst_cheltuieli = get_dat3()
    cheltuiala = lst_cheltuieli[2]

    assert read(lst_cheltuieli, get_id(cheltuiala)) == cheltuiala
    assert read(lst_cheltuieli, None) == lst_cheltuieli


def test_update():
    lst_cheltuieli = get_dat3()
    chelt_new = creeaza_cheltuiala(2, 1002, 110, '2021-11-11', 'Tip nou')
    updated = update(lst_cheltuieli, chelt_new)

    assert chelt_new in updated
    assert chelt_new not in lst_cheltuieli
    assert len(updated) == len(lst_cheltuieli)

    # testam daca se afiseaza exceptie pt ID inexistent
    c_new = creeaza_cheltuiala(2, 1999, 222, 'blabla', 'Tip')
    try:
        _ = update(lst_cheltuieli, c_new)
        assert False
    except ValueError:
        assert True


def test_delete():
    lst_cheltuieli = get_dat3()
    id_chelt_de_sters = 1002
    chelt_de_sters = read(lst_cheltuieli, id_chelt_de_sters)
    deleted = delete(lst_cheltuieli, id_chelt_de_sters)

    assert chelt_de_sters not in deleted
    assert len(deleted) == len(lst_cheltuieli) - 1
    assert chelt_de_sters in lst_cheltuieli

    # testam daca se afiseaza exceptie pt ID inexistent
    id = 1999
    try:
        _ = delete(lst_cheltuieli, id)
        assert False
    except ValueError:
        assert True


def test_CRUD():
    test_create()
    test_read()
    test_update()
    test_delete()
