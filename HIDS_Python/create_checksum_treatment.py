import hashlib
import os.path

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


# Methode pour recuperer le chemin du dossier a traiter
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


# Methode pour recuperer les dossiers a ne pas traiter
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


# Methode pour supprimer les checksums de la base
def void_checksum_treatment_table(conn, cursor, num_site):
    cursor.execute("""
            DELETE FROM checksum_treatment
            WHERE website_id = %s""", CONSTANT_NUMBER_SITE)


# Methode pour ajouter un checksum dans la base
def add_checksum(conn, cursor, file, checksum, num_site):
    datas = {"file": file, "checksum": checksum, "num_site": num_site}
    cursor.execute("""
    INSERT INTO checksum_treatment (Name_File, Checksum, website_id)
    VALUES (%(file)s, %(checksum)s, %(num_site)s)
    """, datas)
    conn.commit()


# Fonction qui permet d'obtenir un fichier avec les hashs de tous les fihciers d'un dossier
def create_checksum(path_to_hash, folders_exceptions, details, path_file, checksums):
    # On parcours le dossier recursivement pour traiter tous les fichiers
    for dossier, sous_dossiers, fichiers in os.walk(path_to_hash):
        for filename in fichiers:
            # On decoupe la chaine de caractere du chemin de chaque dossier pour recuperer chaque nom de sous-dossier
            # Cela permet de tester si un des sous-dossiers correspond a l'un des dossiers que l'on ne veut pas traiter
            dossier_decoupe = dossier.split('/')
            # Bolleen pour le traitement
            bool = True

            # On parcourt la liste des sous-dossiers obtenu avec le decoupage
            for d in dossier_decoupe:
                # Si l'un des sous-dossier se trouve dans la liste des dossiers a ne pas traiter on passe le booleen a false
                # Cela veut dire que l'on ne traitera pas tout le dossier et ce qu'il y a dedans
                if d in folders_exceptions:
                    bool = False
                    # On regarde l'etat du bolleen, s'il est a True on peut faire le traitement
            if bool:
                m = hashlib.sha512(
                    open(dossier + "/" + filename, 'r').read().encode('utf-8')).hexdigest()
                path_file.append(dossier + "/" + filename)
                checksums.append(m)

# Permet l'ouverture de la connexion a la BDD
conn = open_connection()

# Permet la creation d'un cursor
cursor = create_cursor(conn)

# Le chemin du dossier que l'on veut traite
path_to_hash = get_path_to_hash(cursor)

# La liste des dossiers que l'on veut exclure
folders_exceptions = get_folders_no_treatment(cursor)

# Variable permettant de stocker des donnees sur le traitement
details = []

# Liste qui va contenir le chemin des fichiers
path_file = []

# Liste qui va contenir les checsum des fichiers
checksums = []

void_checksum_treatment_table(conn, cursor, CONSTANT_NUMBER_SITE)

if path_to_hash != None:
    create_checksum(path_to_hash, folders_exceptions, details, path_file, checksums)

    for path, check in zip(path_file, checksums):
        add_checksum(conn, cursor, path, check, CONSTANT_NUMBER_SITE)

else:
    add_result(conn, cursor, False, "Il manque des donnees de configuration",
                               CONSTANT_NUMBER_SITE)

close_connection(cursor)
