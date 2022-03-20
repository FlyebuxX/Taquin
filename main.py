# ======================================================================================================================
# === IMPORTS
# ======================================================================================================================


import random
import math
# ======================================================================================================================
# === CLASS
# ======================================================================================================================


class Game:

    """
    Programme du jeu du Taquin
    """

    def __init__(self):
        self.game = []
        self.lignes = []

    def launcher(self):
        """
        Méthode qui génère aléatoirement le jeu
        """
        numbers = [i for i in range(1, 16)] + [" "]
        random.shuffle(numbers)
        self.game = numbers
        self.lignes = [self.game[i:i + 4] for i in range(0, len(self.game), 4)]

    def afficher_plateau(self):
        """
        Méthode qui affiche le jeu
        """
        game = self.game
        rang_elt = 0
        motif = "+-----+-----+-----+-----+"
        for k in range(4):
            print(motif)
            for i in range(4):
                espace = (3 - len(str(game[rang_elt]))) * " "
                if espace == " ":
                    print("|" + espace + str(game[rang_elt]) + espace + " ", end="")
                else:
                    print("|" + espace + str(game[rang_elt]) + espace, end="")
                rang_elt += 1
            print("|")
        print(motif)

    def positions_cases(self):
        """
        Méthode qui récupère les positions des valeurs des cases
        :return positions: list, liste des positions de chaque case
        """
        lignes = self.lignes
        positions = {lignes[i][j]: (i, j) for i in range(len(lignes)) for j in range(len(lignes[i]))}

        return positions

    def distance_espace(self):
        """
        Méthode qui calcule la distance de chaque case à celle de la case dont la valeur est vide
        Algorithme des k-nearest-neighbours
        :return distances: list, liste des distances
        """
        positions = self.positions_cases()
        case_vide = [value for key, value in positions.items() if key == " "]

        distance = lambda case: math.sqrt((case[0] - case_vide[0][0]) ** 2 + (case[1] - case_vide[0][1]) ** 2)

        return {key: distance(value) for key, value in positions.items()}

    def cases_disponibles(self):
        """
        Méthode qui renvoie les coups possibles
        :return: list
        """

        distances = self.distance_espace()

        return [key for key, value in distances.items() if value == 1.0]


g = Game()
g.launcher()
g.afficher_plateau()
g.cases_disponibles()
print(g.cases_disponibles())
