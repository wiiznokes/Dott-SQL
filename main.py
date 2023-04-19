from utils import db


def main():
    db_file = "data/location_trottinette.db"
    
    conn = db.creer_connexion(db_file)
  
    print("creattion des tables")
    db.mise_a_jour_bd(conn, "data/db_creation.sql")
    db.mise_a_jour_bd(conn, "data/db_first_insert.sql")
    
    print("2. Liste de tous les bateaux")
    select_tous_les_bateaux(conn)





def select_tous_les_bateaux(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bateaux")
    rows = cur.fetchall()
    for row in rows:
        print(row)