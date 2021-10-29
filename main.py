from Tests.test_CRUD import test_CRUD, get_dat3
from Tests.test_rest_tasks import test_rest_tasks
from UserInterface.Interfata import interfata

"""
Scrieți un program pentru gestionarea unei asociații de proprietari. Vor fi suportate operațiile:
1. Adăugare / ștergere / modificare cheltuială: se efectuează pe bază de număr de apartament.
 O cheltuială conține număr apartament, suma, data (DD.MM.YYYY) și tipul: întreținere, canal, alte cheltuieli.
~2. Ștergerea tuturor cheltuielilor pentru un apartament dat.
~3. Adunarea unei valori la toate cheltuielile dintr-o dată calendaristica citită.
4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
~5. Ordonarea cheltuielilor descrescător după sumă.  ----> cu: sorted(lista, key=<<dupa ce se sorteaza>> {, Reverse=True daca vrem descrescator})
6. Afișarea sumelor lunare pentru fiecare apartament.
7. Undo.
"""
"""
Tips: -un fisier pt fiecare functionalitate  
"""
"""
Precizari: Fiecare cheltuiala are un ID unic pt a putea fi identificata             
"""


def main():
    lst_cheltuieli = get_dat3()
    interfata(lst_cheltuieli)

# FA TESTE SI PT EXCEPTII
if __name__ == '__main__':
    test_CRUD()
    test_rest_tasks()
    main()
