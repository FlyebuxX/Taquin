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
        self.coups = []
        self.coup_courant = 0
        self.positions = {}

    def launcher(self):
        """
        Méthode qui génère aléatoirement le jeu
        """
        numbers = [i for i in range(1, 16)]
        numbers.extend(" ")  # ajouter la case vide
        random.shuffle(numbers)

        self.game = numbers
        self.lignes = [self.game[i:i + 4] for i in range(0, len(self.game), 4)]

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
        self.positions = positions
        case_vide = [value for key, value in positions.items() if key == " "]

        def distance(case):
            return math.sqrt((case[0] - case_vide[0][0]) ** 2 + (case[1] - case_vide[0][1]) ** 2)

        return {key: distance(value) for key, value in positions.items()}

    def cases_disponibles(self):
        """
        Méthode qui renvoie les coups possibles
        :return: list
        """
        distances = self.distance_espace()
        coups_possibles = [key for key, value in distances.items() if value == 1.0]
        self.coups = coups_possibles

        return coups_possibles

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

    def jeu_coups(self):
        print("_nVoici les coups que vous pouvez jouer:\n")
        for elt in self.coups:
            print(elt)

        while True:
            coup = input("\nQuelle nombre souhaitez-vous jouer ?")
            if coup.isdigit():
                if int(coup) in self.cases_disponibles():
                    self.coup_courant = int(coup)
                    break

    def permutation(self):
        """
        Méthode qui permute l'élément vide et le coup joué
        """
        # recherche de la positon de l'espace
        pos_vide = ()
        pos_courant = ()
        for i in range(len(self.lignes)):
            for j in range(len(self.lignes[i])):
                if self.lignes[i][j] == " ":
                    pos_vide = i, j
                elif self.lignes[i][j] == self.coup_courant:
                    pos_courant = i, j

        ax = pos_vide[0]
        ay = pos_vide[1]
        bx = pos_courant[0]
        by = pos_courant[1]

        self.lignes[ax][ay], self.lignes[bx][by] = self.lignes[bx][by], self.lignes[ax][ay]

    def maj_game(self):
        self.game = [j for i in self.lignes for j in i]

    def jeu(self):
        r = [i for i in range(1, 16)]
        r.extend(" ")
        while self.game != r:
            self.afficher_plateau()
            self.cases_disponibles()
            self.cases_disponibles()
            self.jeu_coups()
            self.permutation()
            self.maj_game()
        self.afficher_plateau()
        print('\nBravo ! Vous avez gagné !!!')


# ======================================================================================================================
# === PROGRAMME PRINCIPAL
# ======================================================================================================================


g = Game()
g.launcher()
g.jeu()
