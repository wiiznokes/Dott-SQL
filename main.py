from utils import db

def select_tous_les_bateaux(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bateaux")
    rows = cur.fetchall()
    for row in rows:
        print(row)



def main():
    db_file = "data/location_trottinette.db"
    
    conn = db.creer_connexion(db_file)
  
    print("creation des tables")
    db.mise_a_jour_bd(conn, "data/db_creation.sql")
    
    #db.mise_a_jour_bd(conn, "data/db_first_insert.sql")
    
    #select_tous_les_bateaux(conn)

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