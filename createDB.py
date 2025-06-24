import psycopg2

DB_HOST = "127.0.0.1"
DB_NAME = "votre_base_de_donnees"
DB_USER = "smartcampus"
DB_PASSWORD = "1234"

# Connexion à la base de données
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("Connexion réussie à la base de données")

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = conn.cursor()

    # Requête pour créer la table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS equipements (
        id SERIAL PRIMARY KEY,
        equipement TEXT NOT NULL
    );
    """

    # Exécution de la requête
    cursor.execute(create_table_query)
    conn.commit()

    print("Table 'equipements' créée avec succès")

except Exception as e:
    print("Erreur lors de la connexion ou de la création de la table :", e)

finally:
    # Fermeture du curseur et de la connexion
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Connexion fermée")
