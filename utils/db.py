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
    # Lecture du fichier et placement des requ^etes dans un tableau
    sqlQueries = []
    with open(file, 'r') as f:
        createSql = f.read()
        sqlQueries = createSql.split(";")

    # Ex ́ecution de toutes les requ^etes du tableau
    cursor = conn.cursor()
    for query in sqlQueries:
        cursor.execute(query)
    # Validation des modifications
    conn.commit()

