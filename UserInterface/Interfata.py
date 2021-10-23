from Domain.Cheltuiala import get_str, creeaza_cheltuiala
from Logic.CRUD import create, read, update, delete


def show_menu():
    print(' ')
    print('1. Adaugare cheltuiala')
    print('2. Stergere cheltuiala')
    print('3. Modifica cheltuiala existenta')
    print('4. Afiseaza toate cheltuielile')
    print('x. Iesire')


def adaugare(lst_cheltuieli):
    nr_apartament = int(input('Alege nr apartament: '))
    suma = float(input('Scrie suma cheltuita: '))
    data = str(input('Scrie data cheltuielii: '))
    tip_cheltuiala = str(input('Scrie tipul cheltuielii: '))
    return create(lst_cheltuieli, nr_apartament, suma, data, tip_cheltuiala)


def stergere(lst_cheltuieli):
    nr_apartament = int(input('Alege nr apartamentului pe care doresti '))
    return delete(lst_cheltuieli, nr_apartament)


def modificare(lst_cheltuieli):
    nr_apartament = int(input('Alege nr apartamentului pe care doresti sa il modifici: '))
    suma = float(input('Scrie noua suma cheltuita: '))
    data = str(input('Scrie noua data a cheltuielii: '))
    tip_cheltuiala = str(input('Scrie noul tip al cheltuielii: '))
    return update(lst_cheltuieli, creeaza_cheltuiala(nr_apartament, suma, data, tip_cheltuiala))


def afisare(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def interfata(lst_cheltuieli):
    while True:
        show_menu()
        optiune = input('Alege o optiune: ')

        if optiune == '1':
            lst_cheltuieli = adaugare(lst_cheltuieli)

        elif optiune == '2':
            lst_cheltuieli = stergere(lst_cheltuieli)

        elif optiune == '3':
            lst_cheltuieli = modificare(lst_cheltuieli)

        elif optiune == '4':
            afisare(lst_cheltuieli)

        elif optiune == 'x':
            break

        else:
            print('Optiunea aleasa este INVALIDA')

    return lst_cheltuieli
