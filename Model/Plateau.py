from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Construit un plateau vide
    :return: un plateau vide sous forme de double liste/Tableau 2D
    """
    plateau = []
    for i in range(const.NB_LINES):
        ligne =[]
        for j in range(const.NB_COLUMNS):
            ligne.append(None)
        plateau.append(ligne)
    return plateau

def placerPionPlateau(plateau: list, pion: dict, numCol: int) -> int:
    """
    Place un pion sur un plateau dans la colonne indiquée
    :param plateau: Paramètre liste où sera mis le pion
    :param pion: Paramètre dictionnaire désignant le pion mis sur le plateau
    :param numCol: entier représentant la colonne où se situe le pion
    :return: un entier correspondant à la ligne où est mis le pion sur le plateau
    """

    if not type_plateau(plateau):
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau.")
    if not type_pion(pion):
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion.")
    if type(numCol) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier.")
    if numCol > 6 or numCol < 0:
        raise ValueError("placerPionPlateau : La valeur de la colonne (valeur_du_paramètre) n’est pas correcte .")

    pos = False
    i = const.NB_LINES-1
    while not pos and i >= 0:
        if plateau[i][numCol] == None:
            plateau[i][numCol] = pion
            pos = True
            i += 1
        i -= 1
    return i

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de liste de 4 pions aligné horizontalement de la couleur choisie
    :param plateau: Paramètre lu pour connaître la position des pions
    :param couleur: Paramètre de la couleur choisie
    :return: tableau 2D des pions alignés horizontalements
    """
    if not(type_plateau(plateau)):
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4horizontalPlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")

    listeSerie4 = []
    for i in range(const.NB_LINES):
        serie4 = []
        pos = []
        j = 0
        fin = False
        while j < const.NB_COLUMNS and not fin:
            if type_pion(plateau[i][j]):
                if plateau[i][j][const.COULEUR] == couleur:
                    serie4.append(plateau[i][j])
                    pos.append(j)

                if len(serie4) >=2:
                    f = len(serie4)-1
                    if pos[f] > pos[f-1]+1:
                        for h in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.append(serie4)
                fin = True

            j += 1
    return listeSerie4

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
        Retourne une liste de liste de 4 pions aligné verticalment de la couleur choisie
        :param plateau: Paramètre lu pour connaître la position des pions
        :param couleur: Paramètre de la couleur choisie
        :return: tableau 2D des pions alignés verticalement
        """
    if not (type_plateau(plateau)):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4verticalPlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")

    listeSerie4 = []
    for j in range(const.NB_COLUMNS):
        serie4 = []
        pos = []
        i = 0
        fin = False
        while i < const.NB_LINES and not fin:
            if type_pion(plateau[i][j]):
                if plateau[i][j][const.COULEUR] == couleur:
                    serie4.append(plateau[i][j])
                    pos.append(i)

                if len(serie4) >= 2:
                    f = len(serie4) - 1
                    if pos[f] > pos[f - 1] + 1:
                        for h in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.append(serie4)
                fin = True

            i += 1
    return listeSerie4

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Retourne une liste de liste de 4 pions aligné en diagonale directe de la couleur choisie
        :param plateau: Paramètre lu pour connaître la position des pions
        :param couleur: Paramètre de la couleur choisie
        :return: tableau 2D des pions alignés en diagonale directe
    """

    if not (type_plateau(plateau)):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4diagonaleDirectePlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")


    listeSerie4 = []
    i = 0
    rep = 0
    j = 0
    ni = False
    while rep < const.NB_LINES:
        line = i
        col = j
        serie4 = []
        pos = []
        fin = False

        while col < const.NB_COLUMNS and line < const.NB_LINES and not fin:
            if type_pion(plateau[line][col]):
                if plateau[line][col][const.COULEUR] == couleur:
                    serie4.append(plateau[line][col])
                    pos.append((line, col))

                if len(serie4) >= 2:
                    f = len(serie4) - 1
                    if not pos[f][0] == pos[f - 1][0] + 1 or not pos[f][1] == pos[f - 1][1] + 1:
                        for r in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.append(serie4)
                fin = True

            col += 1
            line += 1

        if j >= 3:
            ni = True
        else:
            j += 1

        if ni:
            i += 1
            j = 0

        rep += 1
    return listeSerie4

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
        Retourne une liste de liste de 4 pions aligné en diagonale indirecte de la couleur choisie
            :param plateau: Paramètre lu pour connaître la position des pions
            :param couleur: Paramètre de la couleur choisie
            :return: tableau 2D des pions alignés en diagonale indirecte
        """

    if not (type_plateau(plateau)):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : le second paramètre n’est pas un entier.")
    if couleur > 1 or couleur < 0:
        raise ValueError("detecter4diagonaleIndirectePlateau : La valeur de la couleur (valeur_du_paramètre) n’est pas correcte.")

    listeSerie4 = []
    i = const.NB_LINES-1
    rep = 0
    j = 0
    ni = False
    while rep < const.NB_LINES:
        line = i
        col = j
        serie4 = []
        pos = []
        fin = False

        while col < const.NB_COLUMNS and line < const.NB_LINES and not fin:
            if type_pion(plateau[line][col]):
                if plateau[line][col][const.COULEUR] == couleur:
                    serie4.append(plateau[line][col])
                    pos.append((line, col))

                if len(serie4) >= 2:
                    f = len(serie4) - 1
                    if not pos[f][0] == pos[f - 1][0] - 1 or not pos[f][1] == pos[f - 1][1] + 1:
                        for r in range(f):
                            del pos[0]
                            del serie4[0]

            if len(serie4) >= 4:
                listeSerie4.append(serie4)
                fin = True

            col += 1
            line -= 1

        if j >= 3:
            ni = True
        else:
            j += 1

        if ni:
            i -= 1
            j = 0

        rep += 1
    return listeSerie4

def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction qui retourne les pions gagnants de chaque couleurs
    :param plateau: Liste des positions des pions sur le plateau
    :return: liste des pions de chaque couleurs aligné par 4 en ligne, en colonne et en digonale directe et indirecte
    """
    if not (type_plateau(plateau)):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n'est pas à un plateau.")

    listePionsGagnants = []
    listePionsRouge = []
    listePionsRouge.append((detecter4verticalPlateau(plateau,const.ROUGE),detecter4horizontalPlateau(plateau,const.ROUGE),detecter4diagonaleDirectePlateau(plateau,const.ROUGE),detecter4diagonaleIndirectePlateau(plateau,const.ROUGE)))
    listePionsJaune = []
    listePionsJaune.append((detecter4verticalPlateau(plateau,const.JAUNE),detecter4horizontalPlateau(plateau,const.JAUNE),detecter4diagonaleDirectePlateau(plateau,const.JAUNE),detecter4diagonaleIndirectePlateau(plateau,const.JAUNE)))
    listePionsGagnants.append((listePionsRouge,listePionsJaune))
    return listePionsGagnants

def isRempliPlateau(plateau: list) -> bool:
    """
    Verifie si le plateau est rempli
    :param plateau: Liste des positions des pions sur le plateau
    :return: True si le plateau est rempli, False sinon
    """

    if not (type_plateau(plateau)):
        raise TypeError("isRempliPlateau : Le paramètre n'est pas à un plateau.")

    rempli = True
    i = 0
    while i < const.NB_LINES and rempli:
        j = 0
        while j < const.NB_COLUMNS and rempli:
            if plateau[i][j] == None:
                rempli = False
            j += 1
        i += 1
    return rempli