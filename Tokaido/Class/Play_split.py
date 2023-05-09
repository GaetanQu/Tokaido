import Class.Joueur


def Play_split (liste_joueurs):
    def au_tour_de (liste_joueurs):
        dernier=liste_joueurs[0]
        for joueur in liste_joueurs:
            if joueur.case<dernier.case:
                dernier=joueur
        return dernier

    def jouer_tour (liste_joueurs):
        joueur = au_tour_de(liste_joueurs)