
from utils import db, utils

import requete


db_file = "data/location_trottinette.db"

utils.remove_file(db_file)


conn = db.creer_connexion(db_file)
db.mise_a_jour_bd(conn, "data/db_creation.sql")
db.mise_a_jour_bd(conn, "data/db_first_insert.sql")






choix = ""
while choix != "q":

    utils.clear()
    
    print("******************************************************************************")
    print("                               MENU PRINCIPAL                                 ")
    print("******************************************************************************")
    print("1 - Info client")
    print("2 - Liste des clients qui ont fait au moins une location")
    print("3 - Nouveau client")
    print("4 - Creer location")
    print("5 - Finir location")
    print("6 - Nom et prénom des clients qui ont loué une trottinette xiaomi")
    print("7 - Nom et prénom des employes qui ont louer des trottinette")      
    print("8 - Nom et prénom des employes qui n'ont pas louer des trottinette")   
    print("9 - Nombre des employes")   
    print("10 -Numero de trottinette avec le couleur bleu")  
    print("11 -Nom, prenom et la date du clients qui a fait la premier location") 
    print("12 -Nom et prenom du client qui a effectue exactement deux location")

    print("q - Quitter")
    print("******************************************************************************")
    print("\n")
    
    choix = input("Que souhaitez vous faire ?")
    


    if (choix == '1'):
        requete.get_info_client(conn)
    elif (choix == '2'):
        requete.avoir_list_client_au_moins_une_loc(conn)
    elif (choix == '3'):
        requete.nouveau_client(conn)
    elif (choix == '4'):
        requete.creer_location(conn)
    elif (choix == '5'):
        requete.finir_location(conn)
    elif (choix == '6'):
        requete.client_qui_ont_loue_une_trott_modele_xiaomi(conn)
    elif (choix == '7'):
        requete.employe_qui_ont_loue_trott(conn)   
    elif (choix == '8'):
        requete.employe_qui_non_ont_pas_loue_trott(conn)
    elif (choix == '9'):
        requete.nombre_employe_total(conn)
    elif (choix == '10'):
        requete.numero_trottinette_couleur_bleu(conn)   
    elif (choix == '11'):
        requete.nom_prenom_date_location_premier_client(conn)    
    elif (choix == '12'):
        requete.nom_prenom_du_client_effectue_exactement_deux_reservation(conn)
        
    elif (choix == 'q'):
        break



db.mise_a_jour_bd(conn, "data/db_drop.sql")


print("Au revoir !")