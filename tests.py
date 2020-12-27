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


if __name__ == '__main__':
    unittest.main()
