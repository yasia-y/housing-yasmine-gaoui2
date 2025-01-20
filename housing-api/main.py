from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connexion à la base 'real_estate'
conn = psycopg2.connect(
    dbname="real_estate",
    user="postgres",
    password="2005",
    host="localhost",
    port="5432"
)
conn.autocommit = True
cur = conn.cursor()

# Création de la table si elle n'existe pas
cur.execute("""
    CREATE TABLE IF NOT EXISTS properties (
        id SERIAL PRIMARY KEY,
        longitude FLOAT NOT NULL,
        latitude FLOAT NOT NULL,
        age INT,
        rooms INT,
        bedrooms INT,
        population INT,
        households INT,
        income FLOAT,
        value FLOAT,
        proximity VARCHAR(100)
    )
""")

@app.route('/properties', methods=['GET'])
def fetch_properties():
    cur.execute("SELECT * FROM properties")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

@app.route('/properties', methods=['POST'])
def insert_property():
    data = request.json
    query = """
        INSERT INTO properties (longitude, latitude, age, rooms, bedrooms, population, households, income, value, proximity)
        VALUES (%(longitude)s, %(latitude)s, %(age)s, %(rooms)s, %(bedrooms)s, %(population)s, %(households)s, %(income)s, %(value)s, %(proximity)s)
    """
    cur.execute(query, data)
    return jsonify({"message": "Propriété ajoutée avec succès !"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
