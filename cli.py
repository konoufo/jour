import argparse

from date import Date


parser = argparse.ArgumentParser(description='Calendrier')
parser.add_argument("-d", dest="start", help='Date de départ (AAAA-mm-jj:HH:MM:SS)')
parser.add_argument('-J', dest="jours", help='Jours à ajouter')
parser.add_argument('-H', dest="heures", help='Heures à ajouter')
parser.add_argument('-M', dest="minutes", help='Minutes à ajouter')
parser.add_argument('-S', dest="secondes", help='Secondes à ajouter')
parser.set_defaults(start=Date.DATE_REFERENCE, jours=0, heures=0, minutes=0, secondes=0)

if __name__ == '__main__':
    args = parser.parse_args()
    dateDepart = Date.creeDateAvecStr(args.start)
    dateArrivee = dateDepart.plus(jours=args.jours,
                    heures=args.heures,
                    minutes=args.minutes,
                    secondes=args.secondes)
     
    print('{0.nomJour} {0}'.format(dateArrivee))
