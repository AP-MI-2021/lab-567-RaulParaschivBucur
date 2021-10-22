def show_menu():
    print('1. Adaugare cheltuiala')
    print('2. Stergere cheltuiala')
    print('3. Modifica cheltuiala existenta')
    print('4. Afiseaza toate cheltuielile')
    print('x. Iesire')


def adaugare(lst_cheltuieli):
    pass


def stergere(lst_cheltuieli):
    pass


def modificare(lst_cheltuieli):
    pass


def afisare(lst_cheltuieli):
    pass


def interfata(lst_cheltuieli):
    while True:
        show_menu()
        optiune = input('Alege o optiune: ')
        if optiune == 1:
            adaugare(lst_cheltuieli)

        elif optiune == 2:
            stergere(lst_cheltuieli)

        elif optiune == 3:
            modificare(lst_cheltuieli)

        elif optiune == 4:
            afisare(lst_cheltuieli)

        elif optiune == 'x':
            break