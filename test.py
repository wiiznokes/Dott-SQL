from utils.date import Horaire

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







if __name__ == '__main__':

    hor_str = "10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,16h00 : |13h30,16h00 : |: |"
    hor = Horaire(hor_str)

    now = datetime.now()

    print(now)

    res = is_date_in_schedule(hor, now)

    print(res)