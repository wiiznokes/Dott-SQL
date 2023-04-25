from utils import db

<<<<<<< HEAD
<<<<<<< HEAD
import requete


db_file = "data/location_trottinette.db"
=======
def select_tous_les_Clients(conn):
=======
def select_tous_les_bateaux(conn):
>>>>>>> parent of c48c009 (SSSSSSS)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bateaux")
    rows = cur.fetchall()
    for row in rows:
        print(row)
>>>>>>> c48c009fbce692bc88cf44ec476c1461d2223aad



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
    

<<<<<<< HEAD
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
=======
    while True:
        print("/n")
        print("""
        print("MENU PRINCIPAL")  
        1- Afficher une table
        2- Afficher une requete
        3- Faire insertion
        4- Faire Delete
        5- Quitter""")
print("*********************************************************************************************")
        print("\n")
        choix = input("saisir un choix")
        if choix =='5':
              print("Aurevoir")
              break
        if choix =='1':
            






if __name__ == "__main__":
    main()
>>>>>>> c48c009fbce692bc88cf44ec476c1461d2223aad
