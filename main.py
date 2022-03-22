import random
import copy
import time

v = [random.sample(range(1, 10 ** 3), 10 ** 2),  # Putine si mici.
     random.sample(range(1, 10 ** 4), 10 ** 3),
     random.sample(range(1, 10 ** 6), 10 ** 4),
     random.sample(range(1, 10 ** 7), 10 ** 5),
     random.sample(range(1, 10 ** 8), 10 ** 6),
     random.sample(range(1, 10 ** 9), 10 ** 7)]  # Multe si mari.

v_copy = copy.deepcopy(v)


# ------------------------------------------------------------------------------------------------------------------
# Functie care testeaza daca vectorul este intr-adevar sortat ------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def test_sort(v):
    n = len(v)
    for i in range(1, n):
        if v[i] < v[i - 1]:
            return False
    return True


# ------------------------------------------------------------------------------------------------------------------
# Merge Sort -------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def interclasare(lst, ldr):
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] < ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def merge_sort(v):
    if len(v) <= 1:
        return v
    else:
        mij = len(v) // 2
        lst = merge_sort(v[:mij])
        ldr = merge_sort(v[mij:])
        return interclasare(lst, ldr)


# ------------------------------------------------------------------------------------------------------------------
# Insertion Sort ---------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def insertion_sort(v):
    for i in range(1, len(v)):
        k = v[i]
        j = i - 1
        while j >= 0 and k < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = k
    return v


# ------------------------------------------------------------------------------------------------------------------
# Shell Sort ---------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def shell_sort1(v):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]  # Ciura sequence
    for gap in gaps:
        for i in range(gap, len(v)):
            temp = v[i]
            j = i
            while j >= gap and v[j - gap] > temp:
                v[j] = v[j - gap]
                j -= gap

            v[j] = temp

    return v


def shell_sort2(v):
    gap = 1
    gaps = []

    # Gasim cel mai mare gap utilizand formula lui Knuth
    # Obtin memory error (nu am inteles exact de ce)
    while gap < len(v):
        gap = (gap ** 3 - 1) // 2
        gaps.append(gap)

    for i in reversed(gaps):
        for i in range(gap, len(v)):
            temp = v[i]
            j = i
            while j >= gap and v[j - gap] > temp:
                v[j] = v[j - gap]
                j -= gap

            v[j] = temp

    return v


# ------------------------------------------------------------------------------------------------------------------
# Radix Sort -------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def radix_sort(v):
    for k in range(0, 32, 8):
        buck = [[] for p in range(256)]
        for x in v:
            buck[(x >> k) & 255].append(x)
        index = 0
        for i in range(0, 256):
            for j in range(0, len(buck[i])):
                v[index] = buck[i][j]
                index += 1
    return v


# ------------------------------------------------------------------------------------------------------------------
# Quick Sort -------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def pivot_mediana_din_3(x, y, z):
    if x >= y and x <= z or x >= z and x <= y:
        return x
    if y >= x and y <= z or y >= z and y <= x:
        return y
    return z


def quick_sort(v):
    if len(v) <= 1:
        return v
    else:
        if len(v) >= 3:
            pivot = pivot_mediana_din_3(v[0], v[len(v) // 2], v[len(v) - 1])
        else:
            pivot = v[0] if v[0] >= v[1] else v[1]
        L = [x for x in v if x < pivot]
        E = [x for x in v if x == pivot]
        G = [x for x in v if x > pivot]
        return quick_sort(L) + E + quick_sort(G)


# ------------------------------------------------------------------------------------------------------------------
# Testarea ---------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

for l in v_copy:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} numere folosind Merge Sort dureaza prea mult timp!")
    else:
        start_time = time.time()
        sorted_vector = merge_sort(l)
        stop_time = time.time()
        sort_time = round((stop_time - start_time), 4)
        if test_sort(sorted_vector) == False:
            print("Vectorul nu este sortat!")
        else:
            print(f"Sortarea a {len(l)} numere folosind Merge Sort s-a realizat in {sort_time} secunde")

print()

for l in v_copy:
    if len(l) > 10 ** 4:
        print(f"Sortarea a {len(l)} numere folosind Insertion Sort dureaza prea mult timp!")
    else:
        start_time = time.time()
        sorted_vector = insertion_sort(l)
        stop_time = time.time()
        sort_time = round((stop_time - start_time), 4)
        if test_sort(sorted_vector) == False:
            print("Vectorul nu este sortat!")
        else:
            print(f"Sortarea a {len(l)} numere folosind Insertion Sort s-a realizat in {sort_time} secunde")

print()

for l in v_copy:
    if len(l) > 10 ** 5:
        print(f"Sortarea a {len(l)} numere folosind Shell Sort folosind Ciura's sequence dureaza prea mult timp!")
    else:
        start_time = time.time()
        sorted_vector = shell_sort1(l)
        stop_time = time.time()
        sort_time = round((stop_time - start_time), 4)
        if test_sort(sorted_vector) == False:
            print("Vectorul nu este sortat!")
        else:
            print(f"Sortarea a {len(l)} numere folosind Shell Sort s-a realizat in {sort_time} secunde")

print()

for l in v_copy:
    if len(l) > 10 ** 7:
        print(f"Sortarea a {len(l)} numere folosind Radix Sort baza 256 dureaza prea mult timp!")
    else:
        start_time = time.time()
        sorted_vector = radix_sort(l)
        stop_time = time.time()
        sort_time = round((stop_time - start_time), 4)
        if test_sort(sorted_vector) == False:
            print("Vectorul nu este sortat!")
        else:
            print(f"Sortarea a {len(l)} numere folosind Radix Sort baza 256 s-a realizat in {sort_time} secunde")

print()

for l in v_copy:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} numere folosind Quick Sort - Pivot mediana dureaza prea mult timp!")
    else:
        start_time = time.time()
        sorted_vector = quick_sort(l)
        stop_time = time.time()
        sort_time = round((stop_time - start_time), 4)
        if test_sort(sorted_vector) == False:
            print("Vectorul nu este sortat!")
        else:
            print(f"Sortarea a {len(l)} numere folosind Quick Sort - Pivot mediana din 3 s-a realizat in {sort_time} secunde")

print()
