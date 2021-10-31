
"""
format data calendaristica : DD.MM.YYYY

Cum se afiseaza:
Apartament 1:
Ianuarie:
Februarie:
.
.
.
Decembrie:

Apartament 2:
Ian:
.
.
.
Dec:

"""
from Domain.Cheltuiala2 import get_data, get_nr_apartament, get_suma, creeaza_cheltuiala


def get_month(cheltuiala):
    """
    Returneaza luna dintr-o data calendaristica de forma DD.MM.YYYY
    """
    data = get_data(cheltuiala)
    data_split = data.split('.')
    return data_split[1]


def lista_apartamente(lst_cheltuieli):
    """
    Creeaza o lista cu toate apartamentele din "baza de date"
    """
    result_lst = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) not in result_lst:
            result_lst.append(get_nr_apartament(cheltuiala))

    return result_lst


"""
    lista_apartamente = [1, 2, 3, 7, 8, 10]
    lista_sume_lunare = [[ian1, feb1, ..., dec1], [ian2, feb2, ..., dec2], ... , [ian10, feb10, ..., dec10]
    
    len(lista_apartamente) == len(lista_sume_lunare)
"""


def lista_sume_lunare(lst_cheltuieli, lst_ap):
    """
    Creeaza o lista de liste care contin sumele lunare pt fiecare apartament

    lista_sume_lunare = [[ian1, feb1, ..., dec1], [ian2, feb2, ..., dec2], ... , [ian10, feb10, ..., dec10]
    """
    lst_sume_lunare = []
    for ap in lst_ap:
        lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for cheltuiala in lst_cheltuieli:
            if get_nr_apartament(cheltuiala) == ap:
                if get_month(cheltuiala) == '1':
                    lst[0] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '2':
                    lst[1] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '3':
                    lst[2] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '4':
                    lst[3] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '5':
                    lst[4] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '6':
                    lst[5] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '7':
                    lst[6] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '8':
                    lst[7] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '9':
                    lst[8] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '10':
                    lst[9] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '11':
                    lst[10] += get_suma(cheltuiala)

                elif get_month(cheltuiala) == '12':
                    lst[11] += get_suma(cheltuiala)
        lst_sume_lunare.append(lst)

    return lst_sume_lunare
