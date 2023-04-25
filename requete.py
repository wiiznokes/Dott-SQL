
from utils import utils, db



def get_info_client(conn):
    utils.clear()

    numero_client = utils.to_sql_string(input("Quel est votre numero client ?"))

  
    request = f'''
    SELECT nom_client, prenom_client, date_naissance_client, adresse_client
    FROM Clients
    WHERE numero_client={numero_client}
    '''

    db.faire_request(conn, request)

    input()

