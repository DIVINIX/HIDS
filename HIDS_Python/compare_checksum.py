import pymysql
import time
import datetime

CONSTANT_NUMBER_SITE = 1


# Methode pour ouvrir la connexion avec la BDD
def open_connection():
    # Connexion a la base de donnee
    conn = pymysql.connect(host='dreamzite.com', user='User_EPSI', passwd="zPaYRYeQKqUXibuV", db='Projet_HIDS')
    return conn


# Methode pour creer le cursor pour interagir avec la BDD
def create_cursor(conn):
    cursor = conn.cursor()
    return cursor


# Methode pour fermer la connexion avec la BDD
def close_connection(cursor):
    cursor.close()


# Methode pour ajouter un resultat dans la BDD, notament en cas d'erreur
def add_result(conn, cursor, result, description, num_site):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    datas = {"result": result, "description": description, "num_site": num_site, "created_at": timestamp}
    cursor.execute("""
    INSERT INTO checkings (result, description, website_id, created_at)
    VALUES (%(result)s, %(description)s, %(num_site)s,%(created_at)s)
    """, datas)
    conn.commit()


# Methode pour recuperer les checksums source
def get_checksums_source(cursor):
    checksums_source = []
    cursor.execute("""
    SELECT 	Checksum
    FROM checksum_source
    WHERE website_id = %s""", CONSTANT_NUMBER_SITE)
    rows = cursor.fetchall()
    for row in rows:
        checksums_source.append('{0}'.format(row[0]))
    return checksums_source


# Methode pour recuperer les nom de fichier des checksums source
def get_checksums_source_name_file(cursor):
    checksums_source_name_file = []
    cursor.execute("""
    SELECT 	Name_File
    FROM checksum_source
    WHERE website_id = %s""", CONSTANT_NUMBER_SITE)
    rows = cursor.fetchall()
    for row in rows:
        checksums_source_name_file.append('{0}'.format(row[0]))
    return checksums_source_name_file


# Methode pour recuperer les checksums traitement
def get_checksums_treatment(cursor):
    checksums_treatment = []
    cursor.execute("""
    SELECT 	Checksum
    FROM checksum_treatment
    WHERE website_id = %s""", CONSTANT_NUMBER_SITE)
    rows = cursor.fetchall()
    for row in rows:
        checksums_treatment.append('{0}'.format(row[0]))
    return checksums_treatment


# Methode pour recuperer les nom de fichier des checksums traitement
def get_checksums_treatment_name_file(cursor):
    checksums_treatment_name_file = []
    cursor.execute("""
    SELECT 	Name_File
    FROM checksum_treatment
    WHERE website_id = %s""", CONSTANT_NUMBER_SITE)
    rows = cursor.fetchall()
    for row in rows:
        checksums_treatment_name_file.append('{0}'.format(row[0]))
    return checksums_treatment_name_file


# Permet l'ouverture de la connexion a la BDD
conn = open_connection()

# Permet la creation d'un cursor
cursor = create_cursor(conn)

# Variable permettant de stocker des donnees sur le traitement
details = []

# Booleen pour le traitement
treatment = True

# Permet de recuperer tous les checksums source
checksums_source = get_checksums_source(cursor)

# Methode pour recuperer les nom de fichier des checksums source
checksums_source_name_file = get_checksums_source_name_file(cursor)

# Methode pour recuperer les checksums traitement
checksums_treatment = get_checksums_treatment(cursor)

# Methode pour recuperer les nom de fichier des checksums traitement
checksums_treatment_name_file = get_checksums_treatment_name_file(cursor)

i = 0
j = 0

while i < len(checksums_source) - 1 or i < len(checksums_treatment) - 1:
    if checksums_source[i] != checksums_treatment[j]:
        if checksums_source_name_file[i] == checksums_treatment_name_file[j]:
            details.append("Certains fichiers ont ete modifie : ")
            detail = details[0] + checksums_source_name_file[i] + " | "
            details[0] = detail
            treatment = False
        elif checksums_source_name_file[i] == checksums_treatment_name_file[j + 1]:
            details.append("Fichier ajoute : ")
            detail = details[0] + checksums_treatment_name_file[j] + " | "
            details[0] = detail
            treatment = False
            j = j + 1
        elif checksums_source_name_file[i + 1] == checksums_treatment_name_file[j]:
            details.append("Fichier supprime : ")
            detail = details[0] + checksums_source_name_file[i] + " | "
            details[0] = detail
            treatment = False
            j = j - 1
        """elif checksums_source_name_file[i] != checksums_treatment_name_file[j]:
            details.append("Fichier remplace : ")
            detail = details[0] + checksums_source_name_file[i] + " | "
            details[0] = detail
            treatment = False"""
    i = i + 1
    j = j + 1

if treatment:
    details.append("Aucun probleme")
    add_result(conn, cursor, True, details[0], CONSTANT_NUMBER_SITE)
else:
    add_result(conn, cursor, False, details[0], CONSTANT_NUMBER_SITE)

close_connection(cursor)
