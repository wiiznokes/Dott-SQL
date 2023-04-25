


def select_tous_les_bateaux(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bateaux")
    rows = cur.fetchall()
    for row in rows:
        print(row)




def get_info_client(conn):
    input = input("quel est votre nom ?")

    print(f"Voici votre nom {input}")