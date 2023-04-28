from typing import Optional

from utils.utils import chaine_is_valid

class Date:

    def __init__(self, chaine: str):
        (heure, minute) = chaine.split('h')
        self.heure = heure
        self.minute = minute


class DateCouple:
    def __init__(self, chaine: str):
        (deb, fin) = chaine.split(',')
        self.deb: Date = Date(deb)
        self.fin: Date = Date(fin)





class Day:
    def __init__(self, chaine: str):
        self.matin: Optional[DateCouple] = None
        self.soir: Optional[DateCouple] = None

        (matin, soir) = chaine.split('|')

        if chaine_is_valid(matin):
            self.matin = DateCouple(matin)

        if chaine_is_valid(soir):
            self.soir = DateCouple(soir)



# input exemple: 
# "10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,17h30 : |13h30,17h30 : |: |"

# usage: 
# a = Horaire(chaine)
# if a.lundi.soir:  verification car soir peut être null
#    print(a.lundi.soir.deb.heure)

class Horaire:
    def __init__(self, chaine: str):
        
        days = chaine.split(':')

        
        self.lundi: Day = Day(days[0])
        self.mardi: Day = Day(days[1])
        self.mercredi: Day = Day(days[2])
        self.jeudi: Day = Day(days[3])
        self.vendredi: Day = Day(days[4])
        self.samedi: Day = Day(days[5])
        self.dimanche: Day = Day(days[6])



from datetime import datetime

def date_est_dans_horaire(horaire: Horaire, date_actuelle: datetime) -> bool:
    jour_semaine = date_actuelle.weekday()

    if jour_semaine == 0:
        jour = horaire.lundi
    elif jour_semaine == 1:
        jour = horaire.mardi
    elif jour_semaine == 2:
        jour = horaire.mercredi
    elif jour_semaine == 3:
        jour = horaire.jeudi
    elif jour_semaine == 4:
        jour = horaire.vendredi
    elif jour_semaine == 5:
        jour = horaire.samedi
    else:
        jour = horaire.dimanche

    if (jour.matin):
        deb = datetime(date_actuelle.year, date_actuelle.month, date_actuelle.day, int(jour.matin.deb.heure), int(jour.matin.deb.minute))
        fin = datetime(date_actuelle.year, date_actuelle.month, date_actuelle.day, int(jour.matin.fin.heure), int(jour.matin.fin.minute))
        if deb <= date_actuelle and date_actuelle <= fin:
            return True

    if (jour.soir):
        deb = datetime(date_actuelle.year, date_actuelle.month, date_actuelle.day, int(jour.soir.deb.heure), int(jour.soir.deb.minute))
        fin = datetime(date_actuelle.year, date_actuelle.month, date_actuelle.day, int(jour.soir.fin.heure), int(jour.soir.fin.minute))
        if deb <= date_actuelle and date_actuelle <= fin:
            return True

  

    return False
