from abc import ABC, abstractmethod
from math import *
# Q1
def analyzer_position(positions):
    distances = [sqrt(x ** 2 + y ** 2) for x, y in positions]
    moyenne = sum(distances) / len(positions)

    index_plus_eloigner = distances.index(max(distances))
    plus_eloigner = positions[index_plus_eloigner]
    tri_x = sorted(positions, key=lambda p: p[0], reverse=True)
    unique = {(x, y) for x, y in positions if x > y }
    return moyenne, plus_eloigner, tri_x, unique
positions = [(1, 0), (2, 2), (0, 1), (2, 2)]
print(analyzer_position(positions))

#Q2
def analyzer_deplacement(mouvements):
    groupe = {}
    for dx, dy in mouvements:
        distance = sqrt(dx ** 2 + dy ** 2)

        if distance not in groupe:
            groupe[distance] = set()
        groupe[distance].add((dx, dy))

    return groupe
deplacement = [(1, 0), (0, 1), (1, 1), (1, 0)]
result = analyzer_deplacement(deplacement)
print(result)

# Q3

class Entite(ABC):
    def __init__(self, nom, annee_arrivee):
        self.nom = nom
        self.annee_arrivee = annee_arrivee

    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f"{self.nom} {self.annee_arrivee}"

#class Animal(Entite):





