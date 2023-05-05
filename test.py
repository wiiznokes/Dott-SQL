from utils import db, utils

import requete


db_file = "data/location_trottinette.db"

utils.remove_file(db_file)


conn = db.creer_connexion(db_file)
db.mise_a_jour_bd(conn, "data/db_creation.sql")
db.mise_a_jour_bd(conn, "data/db_first_insert.sql")
db.mise_a_jour_bd(conn, "data/db_insert_incorrect.sql")

