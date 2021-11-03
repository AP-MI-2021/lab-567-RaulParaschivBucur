"""
add,2,sambata,13;

showall;

add,2,sambata,13;showall,add,4,azi,23;remove,4;showall;
"""
from Domain.Cheltuiala2 import creeaza_cheltuiala, get_str
from Logic.Add_value_for_date import adunare_valoare
from Logic.CRUD import create, delete, update, read
from Logic.Del_all import stergere_toate_chelt
from Logic.Max_chelt_each_type import afiseaza_max_chelt, max_suma_chelt_pt_fiecare_tip_chelt
from Logic.Show_monthly_sum import lista_apartamente, lista_sume_lunare
from Logic.Sort_desc import sortare_desc_dupa_suma
from UserInterface.Interfata import afisare_tot


def show_help():
    print('Legenda:')
    print('add, id, nr_ap, suma, data, tipul -> adauga cheltuiala')
    print('showall -> afiseaza toate cheltuielile')
    print('update -> modifica cheltuiala, scrie apoi un numar pt a alege ID-ul cheltuielii pe care vrei sa o modifici'
          'si noile nr_apartament, suma, data, tipul')
    print('remove, id -> sterge o cheltuiala,  cu ID-ul dat')
    print('; -> sfarsitul unei comenzi')
    print('quit ,obligatoriu la final -> iesire (dupa quit nu se pune ;)')
    print('del_all, nr_ap -> sterge toate cheltuielile apartamentului dorit')
    print('sort_desc -> sorteaza descrescator dupa suma cheltuita')
    print('read, id -> afiseaza cheltuiala cu id-ul dat')
    print('add_value_for_date, data , valoare -> adauga o valoare la cheltuielile din data aleasa')
    print('max_chelt -> afiseaza cheltuiala maxima pt fiecare tip de cheltuiala')
    print('show_monthly_sum -> afiseaza sumele lunare pt fiecare apartament')


def adaugare(lst_cheltuieli, id, nr_apartament, suma, data, tip_cheltuiala):
    try:
        return create(lst_cheltuieli, nr_apartament, id, suma, data, tip_cheltuiala)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def stergere_o_cheltuiala(lst_cheltuieli, id_cheltuiala):
    try:
        return delete(lst_cheltuieli, id_cheltuiala)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def modificare(lst_cheltuieli, id, nr_apartament, suma, data, tip_cheltuiala):
    try:
        return update(lst_cheltuieli, creeaza_cheltuiala(nr_apartament, id, suma, data, tip_cheltuiala))
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def stergere_toate_cheltuielile_unui_ap(lst_cheltuieli, nr_apartament):
    try:
        return stergere_toate_chelt(lst_cheltuieli, nr_apartament)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lst_cheltuieli


def sortare_descrescator(lst_cheltuieli):
    return sortare_desc_dupa_suma(lst_cheltuieli)


def afisare_unica(lst_cheltuieli, id):
    try:
        print(' ')
        result = read(lst_cheltuieli, id)
        if result is None:
            raise ValueError(f'Nu exista o cheltuiala cu ID-ul {id} pe care sa o afisam')
        print(get_str(result))
    except ValueError as ve:
        print('Eroare: ', ve)


def adaugare_valoare_pt_chelt_din_data(lst_cheltuieli, data, valoare):
    try:
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


def ui_2(lst_cheltuieli):
    print(' ')
    show_help()
    print(' ')
    comenzi = input('Scrie lista de comenzi separate prin virgula si ; pt finalul comenzii: ')
    lst_comenzi = comenzi.split(';')
    done = False
    while not done:
        for comanda in lst_comenzi:
            comanda_split = comanda.split(',')

            if comanda_split[0] == 'showall':
                afisare_tot(lst_cheltuieli)

            elif comanda_split[0] == 'add':
                lst_cheltuieli = adaugare(lst_cheltuieli, int(comanda_split[1]), int(comanda_split[2]),
                                          float(comanda_split[3]), str(comanda_split[4]), str(comanda_split[5]))

            elif comanda_split[0] == 'remove':
                lst_cheltuieli = stergere_o_cheltuiala(lst_cheltuieli, int(comanda_split[1]))

            elif comanda_split[0] == 'update':
                lst_cheltuieli = modificare(lst_cheltuieli, int(comanda_split[1]), int(comanda_split[2]),
                                            float(comanda_split[3]), str(comanda_split[4]), str(comanda_split[5]))

            elif comanda_split[0] == 'quit':
                done = True

            elif comanda_split[0] == 'del_all':
                lst_cheltuieli = stergere_toate_cheltuielile_unui_ap(lst_cheltuieli, int(comanda_split[1]))

            elif comanda_split[0] == 'sort_desc':
                lst_cheltuieli = sortare_descrescator(lst_cheltuieli)

            elif comanda_split[0] == 'read':
                afisare_unica(lst_cheltuieli, int(comanda_split[1]))

            elif comanda_split[0] == 'add_value_for_date':
                adaugare_valoare_pt_chelt_din_data(lst_cheltuieli, str(comanda_split[1]), int(comanda_split[2]))

            elif comanda_split[0] == 'max_chelt':
                cea_mai_mare_chelt_pt_fiecare_tip(lst_cheltuieli)

            elif comanda_split[0] == 'show_monthly_sum':
                afiseaza_sume_lunare(lst_cheltuieli)

