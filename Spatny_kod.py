import sys
import os  # CHYBA 1: Knihovny importuji, ale nikde ji nepoužiji
import math


def spocitej(a, b):
    vysledek = a + b
    tajne_cislo = 42  # CHYBA 2: Proměnná byla vytvořená, ale nepoužil jsem ji
    return vysledek


print(spocitej(5, 10))