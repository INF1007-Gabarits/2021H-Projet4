from random import randint


class Cours(object):
    def __init__(self):
        # TODO: à implémenter

    def ajout_evaluation(self, nom_eval, ponderation):
        # TODO: à implémenter

    def __str__(self):
        # TODO: à implémenter

    def __repr__(self):
        # TODO: à implémenter


class Eleve(object):
    def __init__(self):
        # TODO: à implémenter
    
    def ajout_cours(self, cours):
        # TODO: à implémenter

    def calculer_note(self):
        # TODO: à implémenter

    def __str__(self):
        # TODO: à implémenter
    
    def __repr__(self):
        # TODO: à implémenter


if __name__ == "__main__":
    # Création d'élèves
    eleve1 = Eleve("John Doe", 555555)
    eleve2 = Eleve("Jane Doe", 444444)

    # Creation des cours
    cours1 = Cours('Introduction à la programmation', 'INF1007', 4)
    cours2 = Cours('Calcul 1', 'MTH1101', 3)
    cours3 = Cours('Programmation orientée objet avancée', 'INF1015', 4)
    cours4 = Cours('Calcul 2', 'MTH1102', 3)

    # Ajout des cours à l'élève
    eleve1.ajout_cours(cours1)
    eleve1.ajout_cours(cours2)
    eleve2.ajout_cours(cours3)
    eleve2.ajout_cours(cours4)

    # Affichage de l'élève
    print(eleve1)
    print(eleve2)

    # Ajout d'evaluation et calcul de la moyenne de l'élève 1
    cours1.ajout_evaluation('intra', 35)
    cours1.ajout_evaluation('final', 65)
    cours1.ajout_evaluation('intra', 35)
    cours2.ajout_evaluation('intra', 40)
    cours2.ajout_evaluation('final', 60)
    eleve1.calculer_note()

    # Fonction de conversion
    print(cours1.__repr__())
    print(eleve1.__repr__())
