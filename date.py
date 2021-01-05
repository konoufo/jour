class Date:
    DATE_REFERENCE = "2020-12-23:19:30:00"
    SEMAINE = ('mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', 'lundi', 'mardi')
    NBJOURS_MOIS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, date=None):
        self.annee = date.annee if date is not None else 2020
        self.mois = date.mois if date is not None else 11  # 0=Janvier,...,11=Décembre
        self.jour = date.jour if date is not None else 23  # 0..31
        self.heure = date.heure if date is not None else 19  # 0..23
        self.minute = date.minute if date is not None else 30  # 0..59
        self.seconde = date.seconde if date is not None else 00  # 0..59
        self.nomJour = date.nomJour if date is not None else "mercredi"

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
        date._evalueNomJour()
        return date
    
    def estBissextile(self):
        """Retourne si cette date est dans une année bissextile"""
        return Date.estAnneeBissextile(self.annee)
    
    @staticmethod
    def estAnneeBissextile(annee):
        return annee % 4 == 0

    def _evalueNomJour(self):
        orig = Date.creeDateAvecStr(Date.DATE_REFERENCE)
        jours = (self.annee - orig.annee) * 365
        if self.annee > orig.annee:
            jours += (self.annee - orig.annee - 1) // 4  # supplément années bissextiles
            if Date.estAnneeBissextile(self.annee) and self.mois > 1:
                jours += 1
        else:
            jours -= abs(self.annee - orig.annee + 1) // 4
            if Date.estAnneeBissextile(self.annee) and self.mois <= 1:
                jours -= 1
        if self.mois > orig.mois:
            jours += sum(Date.NBJOURS_MOIS[orig.mois:self.mois]) - orig.jour + self.jour
        else:
            jours -= sum(Date.NBJOURS_MOIS[self.mois:orig.mois]) + orig.jour - self.jour
            print('JOURS:', jours)
        self.nomJour = Date.SEMAINE[jours % 7]
        return self.nomJour

    def __str__(self):
        return '{0.annee}-{1}-{0.jour}:{0.heure}:{0.minute}:{0.seconde}'.format(self, self.mois + 1)

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

    @staticmethod
    def creeDateAvecStr(strDate):
        """Crée et retourne un objet Date si le format est respecté"""
        annee, mois, jour, heure, minute, seconde = None, None, None, None, None, None
        parties = strDate.split(':')
        partieDate = parties[0]
        try:
            annee = int(partieDate[:4])
            mois = int(partieDate[5:7]) - 1
            jour = int(partieDate[8:10])
        except (ValueError, IndexError):
            raise ValueError('Le format de date n\'est pas respecté.')
        date = Date()
        date.annee, date.mois, date.jour = annee, mois, jour
        try:
            heure = int(parties[1])
            minute = int(parties[2])
            seconde = int(parties[3])
        except (ValueError, IndexError):
            pass
        else:
            date.heure, date.minute, date.seconde = heure, minute, seconde
        return date
