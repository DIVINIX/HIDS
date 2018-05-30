import pymysql
import time
import datetime

CONSTANT_NUMBER_SITE = 1


# Méthode pour ouvrir la connexion avec la BDD
def open_connection():
    # Connexion à la base de donnée
    conn = pymysql.connect(host='dreamzite.com', user='User_EPSI', passwd="zPaYRYeQKqUXibuV", db='Projet_HIDS')
    return conn


# Méthode pour créer le cursor pour intéragir avec la BDD
def create_cursor(conn):
    cursor = conn.cursor()
    return cursor


# Méthode pour fermer la connexion avec la BDD
def close_connection(cursor):
    cursor.close()


# Méthode pour récupérer le chemin du dossier a traiter
def get_path_to_hash(cursor):
    cursor.execute("""
         SELECT configuration
         FROM websites
         WHERE id = %s""", CONSTANT_NUMBER_SITE)
    row = cursor.fetchone()
    if row == None:
        return None
    else:
        configuration = '{0}'.format(row[0])
        return configuration


# Méthode pour récupérer les dossiers à ne pas traiter
def get_folders_no_treatment(cursor):
    cursor.execute("""
    SELECT folder_exception
    FROM websites
    WHERE id = %s""", CONSTANT_NUMBER_SITE)
    row = cursor.fetchone()
    if row == None:
        return None
    else:
        row = '{0}'.format(row[0])
        folder_no_treatment = row.split('|')
        return folder_no_treatment


# Méthode pour ajouter un résultat dans la BDD, notament en cas d'erreur
def add_result(conn, cursor, result, description, num_site):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    datas = {"result": result, "description": description, "num_site": num_site, "created_at": timestamp}
    cursor.execute("""
    INSERT INTO checkings (result, description, website_id, created_at)
    VALUES (%(result)s, %(description)s, %(num_site)s,%(created_at)s)
    """, datas)
    conn.commit()
