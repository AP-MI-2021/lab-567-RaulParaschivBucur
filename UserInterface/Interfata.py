from Domain.Cheltuiala2 import get_str, creeaza_cheltuiala
from Logic.CRUD import create, read, update, delete
from Logic.Del_all import stergere_toate_chelt
from Logic.Sort_desc import sortare_desc_dupa_suma


def show_menu():
    print(' ')
    print('1. Adaugare cheltuiala')
    print('2. Stergere cheltuiala')
    print('3. Modifica cheltuiala existenta')
    print('4. Afiseaza o cheltuiala aleasa')
    print('5. Sterge toate cheltuielile unui apartament')
    print('6. Ordoneaza descrescator cheltuielile dupa suma')
    print('a. Afiseaza toate cheltuielile')
    print('x. Iesire')


def adaugare(lst_cheltuieli):
    print(' ')
    nr_apartament = int(input('Alege nr apartament: '))
    id = int(input('Alege un ID: '))
    suma = float(input('Scrie suma cheltuita: '))
    data = str(input('Scrie data cheltuielii: '))
    tip_cheltuiala = str(input('Scrie tipul cheltuielii: '))
    return create(lst_cheltuieli, nr_apartament, id, suma, data, tip_cheltuiala)


def stergere_o_cheltuiala(lst_cheltuieli):
    print(' ')
    id_cheltuiala = int(input('Alege ID-ul cheltuielii pe care doresti sa o stergi: '))
    return delete(lst_cheltuieli, id_cheltuiala)


def modificare(lst_cheltuieli):
    print(' ')
    id = int(input('Alege ID-ul cheltuielii pe care vrei sa o modifici: '))
    nr_apartament = int(input('Alege noul nr al apartamentului: '))
    suma = float(input('Scrie noua suma cheltuita: '))
    data = str(input('Scrie noua data a cheltuielii: '))
    tip_cheltuiala = str(input('Scrie noul tip al cheltuielii: '))
    return update(lst_cheltuieli, creeaza_cheltuiala(nr_apartament, id, suma, data, tip_cheltuiala))


def afisare_tot(lst_cheltuieli):
    print(' ')
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def afisare_unica(lst_cheltuieli):
    print(' ')
    id = int(input('Alege ID-ul cheltuielii pe care vrei sa o afisezi: '))
    result = read(lst_cheltuieli, id)
    if result == lst_cheltuieli:
        print('ID-ul ales NU EXISTA')
    else:
        print(get_str(result))


def stergere_toate_cheltuielile_unui_ap(lst_cheltuieli):
    print(' ')
    nr_apartament = int(input('Alege numarul apartamentului caruia vrei sa ii stergi toate cheltuielile: '))
    return stergere_toate_chelt(lst_cheltuieli, nr_apartament)


def sortare_descrescator(lst_cheltuieli):
    return sortare_desc_dupa_suma(lst_cheltuieli)


def interfata(lst_cheltuieli):
    while True:
        show_menu()
        optiune = input('Alege o optiune: ')

        if optiune == '1':
            lst_cheltuieli = adaugare(lst_cheltuieli)

        elif optiune == '2':
            lst_cheltuieli = stergere_o_cheltuiala(lst_cheltuieli)

        elif optiune == '3':
            lst_cheltuieli = modificare(lst_cheltuieli)

        elif optiune == '4':
            afisare_unica(lst_cheltuieli)

        elif optiune == 'a':
            afisare_tot(lst_cheltuieli)

        elif optiune == '5':
            lst_cheltuieli = stergere_toate_cheltuielile_unui_ap(lst_cheltuieli)

        elif optiune == '6':
            lst_cheltuieli = sortare_descrescator(lst_cheltuieli)

        elif optiune == 'x':
            break

        else:
            print('Optiunea aleasa este INVALIDA')

    return lst_cheltuieli
