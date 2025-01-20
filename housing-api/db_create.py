import psycopg2

# Connexion à la base 'postgres' pour vérifier ou créer une nouvelle base de données
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="newpassword",
    host="localhost",
    port="5432"
)
connection.autocommit = True
cursor = connection.cursor()

# permet juste de vérifier l'existence de la base de données 'real_estate'
cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", ('real_estate',))
if cursor.fetchone() is None:
    cursor.execute("CREATE DATABASE real_estate")
    print("Base de données 'real_estate' créée avec succès.")
else:
    print("La base de données 'real_estate' existe déjà.")

cursor.close()
connection.close()
