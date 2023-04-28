
from utils import utils, db, date

from datetime import datetime

def get_info_client(conn):
    utils.clear()

    numero_client = utils.to_sql_string(input("Quel est votre numero client ?"))

  
    request = f'''
    SELECT nom_client, prenom_client, date_naissance_client, adresse_client
    FROM Clients
    WHERE numero_client={numero_client}
    '''

    db.faire_request(conn, request)

    input()



def avoir_list_client_au_moins_une_loc(conn):
    utils.clear()

  
    request = f'''
    SELECT DISTINCT nom_client
    FROM Clients
    JOIN Locations USING (numero_client)
    '''

    db.faire_request(conn, request)

    input()


def nouveau_client(conn):
    utils.clear()

    request = f'''
    SELECT MAX(numero_client)
    FROM Clients
    '''


    numero = int(db.faire_request_avec_result(conn, request)[0][0]) + 1

 
    
    nom = utils.to_sql_string(input("Quel est votre nom ?"))

    prenom = utils.to_sql_string(input("Quel est votre prenom ?"))

    date = utils.to_sql_string(input("Quel est votre date de naissance ? Exemple: aaaa-mm-jj"))

    adresse = utils.to_sql_string(input("Quel est votre adresse ?"))
    

    request = f'''
    INSERT INTO Clients 
    VALUES ({numero}, {nom}, {prenom}, {date}, {adresse});
    '''
  

    db.faire_update(conn, request)

    print("Vous avez bien été ajouté à la base de donnée.")
    input()



def creer_location(conn):
    utils.clear()

    request = f'''
    SELECT prenom_employe, horaire_employe
    FROM Employes
    '''
    
    employes = db.faire_request_avec_result(conn, request)


    employes_dispo = []

    for e in employes:
        if(date.date_est_dans_horaire(horaire=date.Horaire(e[1]), date_actuelle=datetime.now())):
            employes_dispo.append(e[0])

    print(employes)
    print(employes_dispo)

    input()


def client_qui_ont_loue_une_trott_modele_xiaomi(conn):

    utils.clear()

    request = f'''
    WITH NPClientAvecLocat AS(
    SELECT nom_client, prenom_client, numero_location
    FROM Clients JOIN Locations USING(numero_client)
    ),
    ModeleTrottinette AS(
    SELECT numero_trottinette, nom_modele
    FROM  Trottinettes
    WHERE nom_modele='xiaomi')
    SELECT nom_client, prenom_client, nom_modele
    FROM NPClientAvecLocat JOIN LocationsTrottinettes
    USING(numero_location ) JOIN ModeleTrottinette USING (numero_trottinette);
    '''

    db.faire_request(conn, request)
    
    input()

#def avoir_employe_dispo(date):
    