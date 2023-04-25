from utils import db, affichage


import requete


db_file = "data/location_trottinette.db"

conn = db.creer_connexion(db_file)
#db.mise_a_jour_bd(conn, "data/db_creation.sql")
#db.mise_a_jour_bd(conn, "data/db_first_insert.sql")




choix = ""
while choix != "q":

    affichage.clear()
    
    print("******************************************************************************")
    print("                               MENU PRINCIPAL                                  ")
    print("******************************************************************************")
    print("1 - Info client")
    print("2 - Afficher une requête")
    print("3 - Faire une insertion")
    print("4 - Faire un delete")
    print("q - Quitter")
    print("******************************************************************************")
    print("\n")
    
    choix = input("Que souhaitez vous faire ?")
    


    if (choix == '1'):
        requete.get_info_client(conn)
    elif (choix == '2'):
        pass
    elif (choix == '3'):
        pass
    elif (choix == '4'):
        pass
    elif (choix == 'q'):
        break



