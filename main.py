
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
    elif (choix == '6'):
        requete.client_qui_ont_loue_une_trott_modele_xiaomi(conn)
    elif (choix == 'q'):
        break



db.mise_a_jour_bd(conn, "data/db_drop.sql")


print("Au revoir !")