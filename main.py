from utils import db

import requete


db_file = "data/location_trottinette.db"



conn = db.creer_connexion(db_file)
db.mise_a_jour_bd(conn, "data/db_creation.sql")
#db.mise_a_jour_bd(conn, "data/db_first_insert.sql")




input = ""
while input != "q":


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
    
    input = input("Que souhaitez vous faire ?")
    

    if (input == 1):
        requete.get_info_client(conn)
    elif (input == 2):
        pass
    elif (input == 3):
        pass
    elif (input == 4):
        pass
    elif (input == 'q'):
        break