# ======================================================================================================================
# === IMPORTATIONS
# ======================================================================================================================


import random
import math
# ======================================================================================================================
# === CLASS
# ======================================================================================================================


class Taquin:

    """
    Programme du jeu du Taquin
    """

    def __init__(self):
        self.ensemble_jeu = []
        self.fin_jeu = False
        self.lignes = []
        self.coups = []
        self.coup_courant = 0
        self.positions = {}
        self.compteur = 0

    def launcher(self):
        """
        Méthode qui génère aléatoirement le set de départ
        """
        numbers = [i for i in range(1, 16)]
        numbers.extend(' ')  # ajouter la case vide
        random.shuffle(numbers)

        self.ensemble_jeu = numbers
        self.lignes = [self.ensemble_jeu[i:i + 4] for i in range(0, len(self.ensemble_jeu), 4)]

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
        case_vide = [value for key, value in positions.items() if key == ' ']

        def distance(case):
            return math.sqrt((case[0] - case_vide[0][0]) ** 2 + (case[1] - case_vide[0][1]) ** 2)

        distances = {key: distance(value) for key, value in positions.items()}

        return distances

    def cases_disponibles(self):
        """
        Méthode qui renvoie les coups jouables
        :return coups_possibles: list, liste des coups jouables
        """
        distances = self.distance_espace()
        # distance de 1 avec la case vide : la case peut être jouée
        coups_possibles = [key for key, value in distances.items() if value == 1.0]
        self.coups = coups_possibles

        return coups_possibles

    def permutation(self):
        """
        Méthode qui permute l'élément vide et le coup joué
        """
        pos_vide, pos_courant = (), ()
        for i in range(len(self.lignes)):
            for j in range(len(self.lignes[i])):
                if self.lignes[i][j] == " ":  # recherche de la case vide
                    pos_vide = i, j
                elif self.lignes[i][j] == self.coup_courant:  # recherche de la case valeur
                    pos_courant = i, j

        # assignation des coordonnées de la case valeur et de la case vide
        val_x, val_y, vide_x, vide_y = pos_courant[0], pos_courant[1], pos_vide[0], pos_vide[1]

        # permutation des cases
        self.lignes[val_x][val_y], self.lignes[vide_x][vide_y] = self.lignes[vide_x][vide_y], self.lignes[val_x][val_y]

    def mise_a_jour_jeu(self):
        self.ensemble_jeu = [j for i in self.lignes for j in i]
        self.compteur += 1

    # ******************************************* interaction joueur ***************************************************

    def afficher_plateau(self):
        """
        Méthode qui affiche le plateau du jeu
        """
        jeu = self.ensemble_jeu
        rang_elt = 0
        motif = '+-----+-----+-----+-----+'
        for k in range(4):
            print(motif)
            for i in range(4):
                espace = (3 - len(str(jeu[rang_elt]))) * ' '
                print('|' + espace + str(jeu[rang_elt]), end='')
                if espace == " ":
                    espace_sup = espace + ' '
                else:
                    espace_sup = espace
                print(espace_sup, end='')
                rang_elt += 1
            print('|')
        print(motif)

    def jeu_coups(self):
        """
        Méthode qui demande au joueur quelle case il souhaite jouer
        """
        print("\nVoici les coups que vous pouvez jouer:\n")

        for elt in self.coups:  # affichage des coups disponibles
            print(elt)

        while True and not self.fin_jeu:
            coup = input("\nQuelle nombre souhaitez-vous jouer ? (stop pour arrêter le jeu)")
            if coup.isdigit():
                if int(coup) in self.cases_disponibles():
                    self.coup_courant = int(coup)
                    break
            elif coup == "stop":
                self.fin_jeu = True

    def jeu(self):
        """
        Méthode qui gère le déroulement du jeu
        """
        jeu_depart = [i for i in range(1, 16)]
        jeu_depart.extend(" ")
        while self.ensemble_jeu != jeu_depart and not self.fin_jeu:
            self.afficher_plateau()
            self.cases_disponibles()
            self.jeu_coups()
            if not self.fin_jeu:
                self.permutation()
                self.mise_a_jour_jeu()

        if not self.fin_jeu:
            self.afficher_plateau()
            print("\nBravo ! Vous avez gagné !!!")
            print('Vous avez terminé le jeu en', self.compteur, 'coups.')
        else:
            print('Vous avez arrêté la partie. A bientôt !')


# ======================================================================================================================
# === PROGRAMME PRINCIPAL
# ======================================================================================================================


jeu_taquin = Taquin()
jeu_taquin.launcher()
jeu_taquin.jeu()
