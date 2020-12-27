class Date:
    DATE_REFERENCE = "2020-12-23:19:30:00"
    NOMJOUR_REFERENCE = "mercredi"
    NBJOURS_MOIS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, date=None):
        self.annee = date.annee if date is not None else 2020
        self.mois = date.mois if date is not None else 11  # 0=Janvier,...,11=Décembre
        self.jour = date.jour if date is not None else 23  # 0..31
        self.heure = date.heure if date is not None else 19  # 0..23
        self.minute = date.minute if date is not None else 30  # 0..59
        self.seconde = date.seconde if date is not None else 00  # 0..59

    def plus(self, jours=0, heures=0, minutes=0, secondes=0):
        """Ajoute une durée à la date courante et retourne une nouvelle date résultante"""
        date = Date(self)
        jours, heures, minutes, secondes = int(jours), int(heures), int(minutes), int(secondes)
        if jours == 0 and heures == 0 and minutes == 0 and secondes == 0:
            return date
        jours, heures, minutes, secondes = Date.simplifieDuree(jours, heures, minutes, secondes)
        return date.plusSecondes(secondes).plusMinutes(minutes).plusHeures(heures).plusJours(jours)
    
    def plusSecondes(self, secondes):
        date = Date(self)
        secRestantsMinute = 1
        while secondes > 0:
            secRestantsMinute = 59 - date.seconde
            if secRestantsMinute < secondes:
                date.minute = (date.minute + 1) % 60
                date.seconde = 0
                if date.minute == 0:
                    date.heure = (date.heure + 1) % 24
                    if date.heure == 0:
                        date = date.plusJours(1)
            else:
                date.seconde += secondes
            secondes -= secRestantsMinute + 1
        return date

    def plusMinutes(self, minutes):
        date = Date(self)
        minsRestantsHeures = 1
        while minutes > 0:
            minsRestantsHeures = 59 - date.minute
            if minsRestantsHeures < minutes:
                date.heure = (date.heure + 1) % 24
                date.minute = 0
                if date.heure == 0:
                    date = date.plusJours(1)
            else:
                date.minute += minutes
            minutes -= minsRestantsHeures + 1
        return date

    def plusHeures(self, heures):
        date = Date(self)
        heuresRestantsJours = 1
        while heures > 0:
            heuresRestantsJours = 23 - date.heure
            if heuresRestantsJours < heures:
                date.heure = 0
                date = date.plusJours(1)
            else:
                date.heure += heures
            heures -= heuresRestantsJours + 1
        return date

    def plusJours(self, jours):
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
                    # si on passe à Janvier, alors on incrémente l'année
                    date.annee += 1
            else:
                # sinon on ajoute juste les jours
                date.jour += jours
            jours -= joursRestantsMois + 1
        return date
    
    @staticmethod
    def simplifieDuree(jours=0, heures=0, minutes=0, secondes=0):
        """Retourne une durée simplifiée dans les bornes de chaque unité de temps"""
        minutes += secondes // 60
        secondes = secondes % 60
        heures += minutes // 60
        minutes = minutes % 60
        jours += heures // 24
        heures = heures % 24
        return jours, heures, minutes, secondes

    def estBissextile(self):
        """Retourne si cette date est dans une année bissextile"""
        return abs(self.annee - 2020) % 4 > 0  # puisque 2020 est bissextile
