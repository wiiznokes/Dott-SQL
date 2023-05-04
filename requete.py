
from utils import utils, db, date

from datetime import datetime


adresse_magasin = "12 Bis Rue de Kérogan, Grenoble"

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

    print(f"Vous avez bien été ajouté à la base de donnée. Votre numéro client est {numero}")
    input()



def creer_location(conn):
    utils.clear()
    print("******************************************************************************")
    print("                               AJOUTER LOCATION                                 ")
    print("******************************************************************************")

    print("Saisissez votre numero client")
    while True:
        choix = input()

        if (choix == 'q'):
            return

        if (choix.isdigit()):
            choix = int(choix)
            request = f'''
            SELECT MAX(numero_client)
            FROM Clients
            '''
            numero_client_max = int(db.faire_request_avec_result(conn, request)[0][0])

            if (choix > 0 and choix <= numero_client_max):
                # numero client valid, check si un location est déjà en cours
                request = f'''
                SELECT numero_location
                FROM Locations
                WHERE numero_client = {choix} and adresse_arr_location IS NULL;
                '''
                locations = db.faire_request_avec_result(conn, request)

                if (len(locations) != 0):
                    input("Une location est déjà en cours. Veuillez la terminer pour en ouvrir une autre.")
                    return
                else:
                    break
            else:
                print("Le numero client saisi n'exite pas. Veuillez en redonner un autre")
            
        

    numero_client = choix


    request = f'''
    SELECT horaire_employe, numero_employe, prenom_employe
    FROM Employes
    '''
    
    employes = db.faire_request_avec_result(conn, request)


    employes_dispo = []

    for e in employes:
        if(date.date_est_dans_horaire(horaire=date.Horaire(e[0]), date_actuelle=datetime.now())):
            employes_dispo.append(e)

    if (len(employes_dispo) == 0):
        input("Aucun employé disponible pour l'instant, revenez plus tard")
        return
    

    print("Saisissez le numero de l'employé qui vous vendra la location. (Liste d'employé en fonction de leur horaire)")
    for index, e in enumerate(employes_dispo):
        l = f'''{index} - {e[2]}'''
        print(l)
    print("q - Quitter")

    choix = ""
    while True:
        choix = input()

        if (choix == 'q'):
            return
        
        if (choix.isdigit()):
            choix = int(choix)
            if (choix >= 0 and choix < len(employes_dispo)):
                break
            
        print("Mauvaise entree, veuillez redonner un reponse.")


    employe = employes_dispo[choix]
    numero_employe = employe[1]


    request = f'''
    SELECT nom_modele, prix_modele, vitesse_modele, couleur_modele
    FROM Modeles
    '''
    
    modeles = db.faire_request_avec_result(conn, request)


    print("Saisissez le modèle voulu.")
    for index, e in enumerate(modeles):
        l = f'''{index} - {e[0]} ({e[1]} €, {e[2]} km/h, {e[3]})'''
        print(l)
    
    while True:
        choix = input()

        if (choix == 'q'):
            return

        if (choix.isdigit()):
            choix = int(choix)
            if (choix >= 0 and choix < len(modeles)):
                break
            
        print("Mauvaise entree, veuillez redonner un reponse.")

    nom_modele = modeles[choix][0]


    # requete pour avoir les trott dispo, qui ont de la batterie, qui ont
    # un etat moyen ou superieur et qui
    # correspondent a un certain modele

    request = f'''
    WITH TrottSansBatterie AS (
        SELECT numero_trottinette
        FROM Trottinettes
        JOIN Batteries USING (numero_batterie)
        WHERE charge_batterie = 'petit'
    ), TrottEtatMauvais AS (
        SELECT numero_trottinette
        FROM Trottinettes
        WHERE etat_trottinette = 'mauvais'
    ), TrottOccupee AS (
        SELECT numero_trottinette
        FROM LocationsTrottinettes
        JOIN Locations USING (numero_location)
        WHERE date_arr_location IS NULL
    ), TrottModele AS (
        SELECT numero_trottinette
        FROM Trottinettes
        WHERE nom_modele = '{nom_modele}'
    ), TrottIndisponible AS (
        SELECT numero_trottinette
        FROM TrottSansBatterie
        UNION
        SELECT numero_trottinette
        FROM TrottEtatMauvais
        UNION
        SELECT numero_trottinette
        FROM TrottOccupee
    )
    SELECT numero_trottinette
    FROM TrottModele
    EXCEPT
    SELECT numero_trottinette
    FROM TrottIndisponible;
    '''
    

    trottinettes = db.faire_request_avec_result(conn, request)

    if (len(trottinettes) == 0):
        input("Aucunne trottinette disponible avec ce modèle. Veuillez recommencer le process (pas de goto en python :( )")
        return

    numero_trottinette = trottinettes[0][0]


    request = f'''
    SELECT MAX(numero_location)
    FROM Locations
    '''


    numero_location = int(db.faire_request_avec_result(conn, request)[0][0]) + 1

 
    date_dep_location = datetime.now()

    insert = f'''
    INSERT INTO Locations 
    VALUES ({numero_location}, '{date_dep_location}', '{adresse_magasin}', NULL, NULL, {numero_client}, {numero_employe});
    '''
    db.faire_request(conn, insert)
    insert = f'''
    INSERT INTO LocationsTrottinettes 
    VALUES ({numero_location}, {numero_trottinette});
    '''
    db.faire_request(conn, insert)
    
    request = f'''
    SELECT numero_trottinette, etat_trottinette, nom_modele, charge_batterie
    FROM Trottinettes
    JOIN Batteries USING (numero_batterie)
    WHERE numero_trottinette = {numero_trottinette}
    '''

    info = db.faire_request_avec_result(conn, request)[0]
    print(f"Vous avez bien réservé la trottinette numero {info[0]}.")
    print(f"Etat: {info[1]}, Modele: {info[2]}, Batterie: {info[3]}.")

    input()



def finir_location(conn):
    print("hello")


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



def employe_qui_ont_loue_trott(conn):

    utils.clear()

    request = f'''
    SELECT  DISTINCT nom_employe, prenom_employe
    FROM Employes JOIN Locations USING(numero_employe);

    '''

    db.faire_request(conn, request)
    
    input()    




#def avoir_employe_dispo(date):
def employe_qui_non_ont_pas_loue_trott(conn):
    utils.clear()

    request = f'''
    SELECT nom_employe, prenom_employe
    FROM  Employes
    EXCEPT
    SELECT nom_employe, prenom_employe
    FROM Employes JOIN Locations USING(numero_employe);

    '''

    db.faire_request(conn, request)
    
    input()    

def nombre_employe_total(conn):
    utils.clear()

    request = f'''
    SELECT Count(numero_employe)
    FROM  Employes;

    '''

    db.faire_request(conn, request)
    
    input()    

def numero_trottinette_couleur_bleu(conn):
    utils.clear()

    request = f'''
    SELECT numero_trottinette,date_fabrication_trottinette,etat_trottinette,nom_modele,couleur_modele
    FROM  Trottinettes JOIN Modeles USING(nom_modele)
    WHERE couleur_modele='bleu';

    '''

    db.faire_request(conn, request)
    
    input()    

def nom_prenom_date_location_premier_client(conn):
    utils.clear()

    request = f'''
    SELECT DISTINCT nom_client, prenom_client, date_dep_location
    FROM Clients JOIN Locations USING(numero_client)
    WHERE numero_location=1;


    '''

    db.faire_request(conn, request)
    
    input()    

def nom_prenom_du_client_effectue_exactement_deux_reservation(conn):
    utils.clear()

    request = f'''
    SELECT nom_client, prenom_client
    FROM Clients JOIN Locations USING(numero_client)
    GROUP BY nom_client,prenom_client
    HAVING COUNT (numero_location) =2;


    '''

    db.faire_request(conn, request)
    
    input()    

