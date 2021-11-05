from Domain.Cheltuiala2 import get_str, creeaza_cheltuiala
from Logic.Add_value_for_date import adunare_valoare
from Logic.CRUD import create, read, update, delete
from Logic.Del_all import stergere_toate_chelt
from Logic.Max_chelt_each_type import max_suma_chelt_pt_fiecare_tip_chelt, afiseaza_max_chelt
from Logic.Show_monthly_sum import lista_apartamente, lista_sume_lunare
from Logic.Sort_desc import sortare_desc_dupa_suma


def show_menu():
    print(' ')
    print('1. Adaugare cheltuiala')
    print('2. Stergere cheltuiala')
    print('3. Modifica cheltuiala existenta')
    print('4. Afiseaza o cheltuiala la alegere')
    print('5. Sterge toate cheltuielile unui apartament')
    print('6. Ordoneaza descrescator cheltuielile dupa suma')
    print('7. Aduna o valoare la toate cheltuielile dintr-o dată calendaristica specificata')
    print('8. Determina cea mai mare cheltuiala pentru fiecare tip de cheltuiala')
    print('9. Afiseaza sumele lunare pt fiecare apartament')
    print('u. Undo')
    print('a. Afiseaza toate cheltuielile')
    print('x. Iesire')


def adaugare(lst_cheltuieli):
    try:
        print(' ')
        nr_apartament = int(input('Alege nr apartament: '))
        id = int(input('Alege un ID: '))
        suma = float(input('Scrie suma cheltuita: '))
        data = str(input('Scrie data cheltuielii: '))
        tip_cheltuiala = str(input('Scrie tipul cheltuielii: '))
        return create(lst_cheltuieli, nr_apartament, id, suma, data, tip_cheltuiala)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def stergere_o_cheltuiala(lst_cheltuieli):
    try:
        print(' ')
        id_cheltuiala = int(input('Alege ID-ul cheltuielii pe care doresti sa o stergi: '))
        return delete(lst_cheltuieli, id_cheltuiala)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def modificare(lst_cheltuieli):
    try:
        print(' ')
        id = int(input('Alege ID-ul cheltuielii pe care vrei sa o modifici: '))
        nr_apartament = int(input('Alege noul nr al apartamentului: '))
        suma = float(input('Scrie noua suma cheltuita: '))
        data = str(input('Scrie noua data a cheltuielii: '))
        tip_cheltuiala = str(input('Scrie noul tip al cheltuielii: '))
        return update(lst_cheltuieli, creeaza_cheltuiala(nr_apartament, id, suma, data, tip_cheltuiala))
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def afisare_tot(lst_cheltuieli):
    print(' ')
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def afisare_unica(lst_cheltuieli):
    try:
        print(' ')
        id = int(input('Alege ID-ul cheltuielii pe care vrei sa o afisezi: '))
        result = read(lst_cheltuieli, id)
        if result is None:
            raise ValueError(f'Nu exista o cheltuiala cu ID-ul {id} pe care sa o afisam')
        print(get_str(result))
    except ValueError as ve:
        print('Eroare: ', ve)


def stergere_toate_cheltuielile_unui_ap(lst_cheltuieli):
    try:
        print(' ')
        nr_apartament = int(input('Alege numarul apartamentului caruia vrei sa ii stergi toate cheltuielile: '))
        return stergere_toate_chelt(lst_cheltuieli, nr_apartament)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def sortare_descrescator(lst_cheltuieli):
    return sortare_desc_dupa_suma(lst_cheltuieli)


def adaugare_valoare_pt_chelt_din_data(lst_cheltuieli):
    try:
        print(' ')
        data = str(input('Alege data dorita (de tipul: DD.MM.YY): '))
        valoare = float(input('Alege valoarea pe care vrei sa o aduni: '))
        return adunare_valoare(lst_cheltuieli, valoare, data)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def cea_mai_mare_chelt_pt_fiecare_tip(lst_cheltuieli):
    print(' ')
    afiseaza_max_chelt(max_suma_chelt_pt_fiecare_tip_chelt(lst_cheltuieli))


def afiseaza_sume_lunare(lst_cheltuieli):
    lst_ap = lista_apartamente(lst_cheltuieli)
    lst_sume_lunare = lista_sume_lunare(lst_cheltuieli, lst_ap)

    for idx in range(0, len(lst_ap)):
        print(' ')
        print(f'Sumele lunare pentru apartamentul {lst_ap[idx]} sunt:')
        print(f'Ianuarie:   {lst_sume_lunare[idx][0]}')
        print(f'Februarie:  {lst_sume_lunare[idx][1]}')
        print(f'Martie:     {lst_sume_lunare[idx][2]}')
        print(f'Aprilie:    {lst_sume_lunare[idx][3]}')
        print(f'Mai:        {lst_sume_lunare[idx][4]}')
        print(f'Iunie:      {lst_sume_lunare[idx][5]}')
        print(f'Iulie:      {lst_sume_lunare[idx][6]}')
        print(f'August:     {lst_sume_lunare[idx][7]}')
        print(f'Septembrie: {lst_sume_lunare[idx][8]}')
        print(f'Octombrie:  {lst_sume_lunare[idx][9]}')
        print(f'Noiembrie:  {lst_sume_lunare[idx][10]}')
        print(f'Decembrie:  {lst_sume_lunare[idx][11]}')


def handle_new_list(list_versions, current_version, lst_cheltuieli):
    """
    Adauga o noua lista in lista de versiuni
    :param list_versions: lista de versiuni
    :param current_version: versiunea curenta
    :param lst_cheltuieli: lista de cheltuieli
    :return: noua lista de versiuni, si noua versiune curenta
    """
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(lst_cheltuieli)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    """
    Readuce lista ''din baza de date'' la un stadiu anterior
    :param list_versions: lista de versiuni
    :param current_version: versiuena curenta
    :return: lista de versiuni din un stadiu anterior, versiunea curenta dupa aducerea la acel stadiu
    """
    if current_version < 1:
        print('Nu se mai poate efectua undo.')
        return list_versions[current_version], current_version

    current_version -= 1
    return list_versions[current_version], current_version


def interfata(lst_cheltuieli):

    list_versions = [lst_cheltuieli]
    current_version = 0

    while True:
        show_menu()
        optiune = input('Alege o optiune: ')

        if optiune == '1':
            lst_cheltuieli = adaugare(lst_cheltuieli)
            list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli)

        elif optiune == '2':
            lst_cheltuieli = stergere_o_cheltuiala(lst_cheltuieli)
            list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli)

        elif optiune == '3':
            lst_cheltuieli = modificare(lst_cheltuieli)
            list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli)

        elif optiune == '4':
            afisare_unica(lst_cheltuieli)

        elif optiune == 'a':
            afisare_tot(lst_cheltuieli)

        elif optiune == '5':
            lst_cheltuieli = stergere_toate_cheltuielile_unui_ap(lst_cheltuieli)
            list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli)

        elif optiune == '6':
            lst_cheltuieli = sortare_descrescator(lst_cheltuieli)
            list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli)

        elif optiune == '7':
            lst_cheltuieli = adaugare_valoare_pt_chelt_din_data(lst_cheltuieli)
            list_versions, current_version = handle_new_list(list_versions, current_version, lst_cheltuieli)

        elif optiune == '8':
            cea_mai_mare_chelt_pt_fiecare_tip(lst_cheltuieli)
            
        elif optiune == '9':
            afiseaza_sume_lunare(lst_cheltuieli)

        elif optiune == 'u':
            lst_cheltuieli, current_version = handle_undo(list_versions, current_version)

        elif optiune == 'x':
            break

        else:
            print('Optiunea aleasa este INVALIDA')

        # input('\nApasati orice tasta pt a continua')
    return lst_cheltuieli
