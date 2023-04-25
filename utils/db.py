import sqlite3


def creer_connexion(db_file):
    try:
        conn = sqlite3.connect(db_file)
        # On active les foreign keys
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except sqlite3.Error as e:
        print(e)
        return None


def mise_a_jour_bd(conn: sqlite3.Connection, file: str):
    sqlQueries = []
    with open(file, 'r') as f:
        createSql = f.read()
        sqlQueries = createSql.split(";")

    cursor = conn.cursor()
    for query in sqlQueries:
        #print(query)
        cursor.execute(query)

    conn.commit()




def faire_request(conn: sqlite3.Connection, query: str):
    #print(query)
    
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)