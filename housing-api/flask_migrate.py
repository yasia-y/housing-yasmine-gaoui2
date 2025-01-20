from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2005@localhost:5432/real_estate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Property(db.Model):
    __tablename__ = "properties"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer)
    rooms = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer)
    population = db.Column(db.Integer)
    households = db.Column(db.Integer)
    income = db.Column(db.Float)
    value = db.Column(db.Float)
    proximity = db.Column(db.String(100))

# Route pour récupérer les propriétés
@app.route('/properties', methods=['GET'])
def list_properties():
    properties = Property.query.all()
    return jsonify([{
        "id": p.id,
        "longitude": p.longitude,
        "latitude": p.latitude,
        "age": p.age,
        "rooms": p.rooms,
        "bedrooms": p.bedrooms,
        "population": p.population,
        "households": p.households,
        "income": p.income,
        "value": p.value,
        "proximity": p.proximity
    } for p in properties])

# Route pour ajouter une propriété
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.json
    property = Property(**data)
    db.session.add(property)
    db.session.commit()
    return jsonify({"message": "Propriété ajoutée avec succès !"}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
