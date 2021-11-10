from Domain.Cheltuiala2 import get_nr_apartament, creeaza_cheltuiala
from Logic.Add_value_for_date import adunare_valoare
from Logic.CRUD import create
from Logic.Del_all import stergere_toate_chelt
from Logic.Max_chelt_each_type import max_suma_chelt_pt_fiecare_tip_chelt
from Logic.Show_monthly_sum import lista_apartamente, lista_sume_lunare
from Logic.Sort_desc import sortare_desc_dupa_suma
from Tests.test_CRUD import get_dat3

# teste pt Del_all
from UserInterface.Interfata import handle_new_list, handle_undo, handle_redo


def test_sterge_toate_chelt():
    lst_cheltuieli = get_dat3()
    nr_ap_chelt_de_sters = 4
    deleted = stergere_toate_chelt(lst_cheltuieli, nr_ap_chelt_de_sters)
    ok = True
    for cheltuiala in deleted:
        if get_nr_apartament(cheltuiala) == nr_ap_chelt_de_sters:
            ok = False
    assert ok

    # testam daca se afiseaza exceptie pt nr_apartament inexistent
    nr_ap = 1999
    try:
        _ = stergere_toate_chelt(lst_cheltuieli, nr_ap)
        assert False
    except ValueError:
        assert True

# teste pt Sort_desc


def test_sortare_desc_dupa_suma():
    lst_cheltuieli = [creeaza_cheltuiala(4, 1005, 670, '2021-10-7', 'Intretinere'),
                      creeaza_cheltuiala(2, 1001, 2900, '2021-12-11', 'Canal'),
                      creeaza_cheltuiala(2, 1002, 9900, '2021-12-11', 'Intretinere'),
                      creeaza_cheltuiala(4, 1004, 1670, '2021-10-7', 'Canal')]

    lst_dupa_sortare = [
        creeaza_cheltuiala(2, 1002, 9900, '2021-12-11', 'Intretinere'),
        creeaza_cheltuiala(2, 1001, 2900, '2021-12-11', 'Canal'),
        creeaza_cheltuiala(4, 1004, 1670, '2021-10-7', 'Canal'),
        creeaza_cheltuiala(4, 1005, 670, '2021-10-7', 'Intretinere')]

    result = sortare_desc_dupa_suma(lst_cheltuieli)
    assert result == lst_dupa_sortare

# teste pt Add_value_for_date


def test_adunare_valoare():
    lst_cheltuieli = [creeaza_cheltuiala(4, 1005, 670, '2021-10-7', 'Intretinere'),
                      creeaza_cheltuiala(2, 1001, 2900, '2021-12-11', 'Canal'),
                      creeaza_cheltuiala(2, 1002, 9900, '2021-12-11', 'Intretinere'),
                      creeaza_cheltuiala(4, 1004, 1670, '2021-10-7', 'Canal')]

    valoare = 1
    data = '2021-12-11'
    lst_dupa_adunare = adunare_valoare(lst_cheltuieli, valoare, data)
    assert lst_dupa_adunare == [creeaza_cheltuiala(4, 1005, 670, '2021-10-7', 'Intretinere'),
                                creeaza_cheltuiala(2, 1001, 2901, '2021-12-11', 'Canal'),
                                creeaza_cheltuiala(2, 1002, 9901, '2021-12-11', 'Intretinere'),
                                creeaza_cheltuiala(4, 1004, 1670, '2021-10-7', 'Canal')]

    # testam daca se afiseaza exceptie pt data inexistenta
    data_test = 'inexistent'
    try:
        _ = adunare_valoare(lst_cheltuieli, valoare, data_test)
        assert False
    except ValueError:
        assert True

# teste pt Max_chelt_each_type


def test_max_suma_chelt_pt_fiecare_tip_chelt():
    lst_cheltuieli = get_dat3()
    assert max_suma_chelt_pt_fiecare_tip_chelt(lst_cheltuieli) == [('Intretinere', 2900.0), ('Canal', 2900.0),
                                                                   ('Alte cheltuieli', 310.0), ('Gaz', 283.0)]

# teste pt Show_monthly_sum


def test_lista_apartamente():
    lst_cheltuieli = [creeaza_cheltuiala(4, 1005, 670, '2021-10-7', 'Intretinere'),
                      creeaza_cheltuiala(2, 1001, 2900, '2021-12-11', 'Canal'),
                      creeaza_cheltuiala(2, 1002, 9900, '2021-12-11', 'Intretinere'),
                      creeaza_cheltuiala(4, 1004, 1670, '2021-10-7', 'Canal')]
    assert lista_apartamente(lst_cheltuieli) == [4, 2]


def test_lista_sume_lunare():
    lst_cheltuieli = [creeaza_cheltuiala(4, 1005, 670, '10.10.2021', 'Intretinere'),
                      creeaza_cheltuiala(2, 1001, 2900, '1.1.2021', 'Canal')]
    lst_ap = [4, 2]
    assert lista_sume_lunare(lst_cheltuieli, lst_ap) == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 670, 0, 0],
                                                         [2900, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def test_undo_redo():
    lst_cheltuieli = [creeaza_cheltuiala(4, 1005, 670, '10.10.2021', 'Intretinere'),
                      creeaza_cheltuiala(2, 1001, 2900, '1.1.2021', 'Canal')]

    list_versions = [lst_cheltuieli]
    current_version = 0

    lst_cheltuieli_new = create(lst_cheltuieli, 2, 1008, 223, '1.1.2021', 'Gaz')
    list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli_new)
    assert current_version == 1
    assert list_versions == [lst_cheltuieli, lst_cheltuieli_new]

    lst_cheltuieli, current_version = handle_undo(list_versions, current_version)
    assert current_version == 0
    assert lst_cheltuieli == [creeaza_cheltuiala(4, 1005, 670, '10.10.2021', 'Intretinere'),
                              creeaza_cheltuiala(2, 1001, 2900, '1.1.2021', 'Canal')]

    lst_cheltuieli, current_version = handle_redo(list_versions, current_version)
    assert current_version == 1
    assert lst_cheltuieli == [creeaza_cheltuiala(4, 1005, 670, '10.10.2021', 'Intretinere'),
                              creeaza_cheltuiala(2, 1001, 2900, '1.1.2021', 'Canal'),
                              [2, 1008, 223, '1.1.2021', 'Gaz']]


def test_rest_tasks():
    test_sterge_toate_chelt()
    test_sortare_desc_dupa_suma()
    test_adunare_valoare()
    test_max_suma_chelt_pt_fiecare_tip_chelt()
    test_lista_apartamente()
    test_lista_sume_lunare()
    test_undo_redo()
