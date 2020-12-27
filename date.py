class Date:
    DATE_REFERENCE = "2020-12-23:19:30:00"
    NOMJOUR_REFERENCE = "mercredi"
    NBJOURS_MOIS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, date=None):
        self.annee = date.annee if date is not None else 2020
        self.mois = date.mois if date is not None else 11
        self.jour = date.jour if date is not None else 23
        self.heure = date.heure if date is not None else 19
        self.minute = date.minute if date is not None else 30
        self.seconde = date.seconde if date is not None else 00

    def plus(self, jours):
        """Ajoute une durée à la date courante et retourne une nouvelle date résultante"""
        date = Date(self)
        joursRestantsMois = 1
        while jours > 0:
            if date.mois == 1 and date.estBissextile():
                joursRestantsMois = 29 - date.jour
            else:
                joursRestantsMois = Date.NBJOURS_MOIS[date.mois] - date.jour
            if joursRestantsMois < jours:
                # si on doit ajouter plus de jours que restants dans le mois,
                # on passe au mois suivant
                date.mois = (date.mois + 1) % 12
                date.jour = 1
                if date.mois == 0:
                    date.annee += 1
            else:
                # sinon on ajoute juste les jours
                date.jour += jours
            jours -= joursRestantsMois + 1
        return date
    
    def estBissextile(self):
        """Retourne si cette date est dans une année bissextile"""
        return abs(self.annee - 2020) % 4 > 0  # puisque 2020 est bissextile
