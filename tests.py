import unittest
import date


class DateTestCase(unittest.TestCase):
    def test_ajoutDeJoursSansChangerDeMois(self):
        date0 = date.Date()  # 23 décembre 2020
        
        date1 = date0.plus(jours=5)

        assert date1.annee == date0.annee
        assert date1.mois == date0.mois
        assert date1.jour == 28
    
    def test_ajoutDeJoursSansChangerDAnnees(self):
        date0 = date.Date()
        date0.mois = 8  # 23 septembre 2020
        
        date1 = date0.plus(jours=42)

        assert date1.annee == date0.annee
        assert date1.mois == 10
        assert date1.jour == 4

    def test_ajoutDeJoursQuiChangentDAnnee(self):
        date0 = date.Date()
        
        date1 = date0.plus(jours=9)

        assert date1.annee == date0.annee + 1
        assert date1.mois == 0
        assert date1.jour == 1
    
    def test_ajoutDHeuresSansChangerDeJour(self):
        date0 = date.Date()  # 23 décembre 2020 19:30:00

        date1 = date0.plus(heures=2)

        assert date1.annee == date0.annee
        assert date1.mois == date0.mois
        assert date1.jour == date0.jour
        assert date1.heure == 21
        assert date1.minute == date0.minute

    def test_ajoutDHeuresQuiChangentDeJour(self):
        date0 = date.Date()  # 23 décembre 2020 19:30:00

        date1 = date0.plus(heures=5)

        assert date1.annee == date0.annee
        assert date1.mois == date0.mois
        assert date1.jour == 24
        assert date1.heure == 0
        assert date1.minute == date0.minute

    def test_ajoutDHeuresQuiChangentDeMois(self):
        date0 = date.Date()
        date0.mois = 8
        date0.jour = 28  # 28 septembre 2020 19:30:00

        date1 = date0.plus(heures=72)

        assert date1.annee == date0.annee
        assert date1.mois == 9
        assert date1.jour == 1
        assert date1.heure == date0.heure
        assert date1.minute == date0.minute

    def test_ajoutMinutes(self):
        date0 = date.Date()  # 23 décembre 2020 19:30:00

        date1 = date0.plus(minutes=270)  # 4h30

        assert date1.annee == 2020
        assert date1.mois == 11
        assert date1.jour == 24
        assert date1.heure == 0
        assert date1.minute == 0

    def test_ajoutSecondes(self):
        date0 = date.Date()  # 23 décembre 2020 19:30:00

        date1 = date0.plus(secondes=15)

        assert date1.annee == date0.annee
        assert date1.mois == date0.mois
        assert date1.jour == date0.jour
        assert date1.heure == date0.heure
        assert date1.minute == date0.minute
        assert date1.seconde == 15
    
    def test_ajoutDureeCombinee(self):
        date0 = date.Date()  # 23 décembre 2020 19:30:00

        date1 = date0.plus(
            jours=21,
            heures=2,
            minutes=20,
            secondes=15
        )

        assert date1.annee == 2021
        assert date1.mois == 0
        assert date1.jour == 13
        assert date1.heure == 21
        assert date1.minute == 50
        assert date1.seconde == 15

if __name__ == '__main__':
    unittest.main()
