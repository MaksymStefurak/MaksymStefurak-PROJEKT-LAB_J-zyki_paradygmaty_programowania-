#zad1

def podzialPaczek(wagi, max_waga):
    for waga in wagi:

        if waga > max_waga:
            raise ValueError(f"Waga paczki {waga} przekracza dozwolone maksymalne wage kursu {max_waga}")
    sort_wagi = sorted(wagi, reverse = True)
    kursy = []

    for waga in sort_wagi:
        added = False

        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                added = True
                break

        if not added:
            kursy.append([waga])
    return len(kursy), kursy


wagi = [12,7,20,5,9,10,7]

max_wag = 32

licz_kurs, kursy = podzialPaczek(wagi, max_wag)

for i, kurs in enumerate(kursy, 1):
    print(f" Kurs {i} : {kurs} -> suma wagi : {sum(kurs)} kg")

#Zad2
from collections import deque


def algbfs(graf, poczatek, koniec):
    queue = deque(poczatek)

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == koniec:
            return path, len(path)
        else:
            for neighbor in graf.get(node, []):
                queue.append(list(path) + [neighbor])

graf = {

    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']

}


print(algbfs(graf, 'A', 'G'))
#Zad3
taski = [
    {'Czas wykonania': 2, 'nagroda': 11},
    {'Czas wykonania': 5, 'nagroda': 8},
    {'Czas wykonania': 3, 'nagroda': 4},
    {'Czas wykonania': 4, 'nagroda': 9},
]


def Proceduralnie(taski):

    taski.sort(key=lambda x: x['Czas wykonania'])

    czas_oczekiwania = 0
    aktualny_czas = 0

    kolejnosc = []

    for task in taski:

        kolejnosc.append(task)
        czas_oczekiwania += aktualny_czas
        aktualny_czas += task['Czas wykonania']

    return kolejnosc, czas_oczekiwania


kolejnosc, czas_oczekiwania = Proceduralnie(taski)




print("Kolejność zadań:", kolejnosc)
print("Czas oczekiwania:", czas_oczekiwania)
#Zad4
def plecak(wagi, wartosci, pojemnosc):

    przedmioty = len(wagi)

    arrpojemnosc = [0] * (pojemnosc + 1)


    for item in range(przedmioty):

        for j in range(pojemnosc, wagi[item] - 1, -1):
            arrpojemnosc[j] = max(arrpojemnosc[j], arrpojemnosc[j - wagi[item]] + wartosci[item])


    wybrane_przedmioty = []
    item = pojemnosc
    for j in range(przedmioty - 1, -1, -1):

        if item - wagi[j] >= 0 and arrpojemnosc[item] != arrpojemnosc[item - wagi[j]]:
            wybrane_przedmioty.append(j)
            item -= wagi[j]

    wybrane_przedmioty.reverse()

    return arrpojemnosc[pojemnosc], wybrane_przedmioty



wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
pojemnosc = 5

maksymalna_wartosc, wybrane_przedmioty = plecak(wagi, wartosci, pojemnosc)



print(f'Maksymalna wartość: {maksymalna_wartosc}')

print(f'Wybrane przedmioty: {wybrane_przedmioty}')
#Zad5
taski = [
    (2, 6, 7),
    (1, 4, 10),
    (4, 8, 5),
    (5, 9, 12),
    (3, 7, 3),
    (6, 10, 6),
    (0, 5, 8)
]

def procedur(taski):

    taski.sort(key=lambda x: x[1])


    wybrane_taski = []
    maksymalna_nagroda = 0
    zakonczenie = 0

    for task in taski:

        poczatek, koniec, nagroda = task
        if poczatek >= zakonczenie:

            wybrane_taski.append(task)
            maksymalna_nagroda += nagroda
            zakonczenie = koniec

    return maksymalna_nagroda, wybrane_taski

maksymalna_nagroda, wybrane_taski = procedur(taski)
print("Maksymalna Nagroda:", maksymalna_nagroda)
print("Wybrane taski:", wybrane_taski)