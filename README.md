Voici une version adaptée et originale pour ton README : 

---

# Flask et Intégration avec PostgreSQL en Python

## **Vue d'ensemble**

Ce projet illustre comment intégrer une application web Flask en Python avec une base de données PostgreSQL. Il inclut des outils pour la migration et la gestion de base de données en utilisant Flask-Migrate et psycopg2.

---

## **Prérequis**

### **Outils et bibliothèques nécessaires** :
- Python
- PostgreSQL
- Flask
- Flask-Migrate
- psycopg2

### **Préparation requise avant l'exécution** :
1. Active un environnement virtuel Python (`venv`).
2. Assure-toi que le serveur PostgreSQL est en cours d'exécution.

---

## **Installation**

### **Étape 1 : Cloner le dépôt**
```bash
git clone https://github.com/ton-username/housing-yasmine-gaoui.git
cd housing-yasmine-gaoui
cd housing-api
```

### **Étape 2 : Configurer l’environnement virtuel**
```bash
python -m venv venv  # Optionnel
source venv/bin/activate  # Pour Windows : venv\Scripts\activate
```

### **Étape 3 : Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **Étape 4 : Configurer PostgreSQL**
Modifie les identifiants PostgreSQL dans les fichiers nécessaires (par exemple, `db_create.py`) :
```python
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="votre_mot_de_passe",
    host="127.0.0.1",
    port="5432"
)
```
Vérifie que :
- La base de données `postgres` existe.
- L'utilisateur PostgreSQL dispose des permissions nécessaires pour créer des bases et des tables.

---

## **Exécution du projet**

### **Étape 1 : Créer la base de données**
Exécute le script de création :
```bash
python db_create.py
```

### **Étape 2 : Initialiser et appliquer les migrations**

1. **Initialiser Flask-Migrate** :
   ```bash
   export FLASK_APP=app_migration.py  # Pour Windows : set FLASK_APP=app_migration.py
   flask db init
   ```

2. **Créer un script de migration** :
   ```bash
   flask db migrate -m "Migration initiale"
   ```

3. **Appliquer la migration à la base de données** :
   ```bash
   flask db upgrade
   ```

### **Étape 3 : Lancer l'application**
Démarre l'application Flask :
```bash
python app_migration.py
```

---

## **Endpoints de l'API**

### **1. `GET /houses`**
Récupère toutes les entrées de la table `houses`.

**Exemple de réponse** :
```json
[
  {
    "house_id": 1,
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600,
    "ocean_proximity": "NEAR BAY"
  }
]
```

### **2. `POST /houses`**
Ajoute une nouvelle entrée à la table `houses`.

**Exemple de corps de requête** :
```json
{
  "house_id": 2,
  "longitude": -122.22,
  "latitude": 37.86,
  "housing_median_age": 21,
  "total_rooms": 7099,
  "total_bedrooms": 1106,
  "population": 2401,
  "households": 1138,
  "median_income": 8.3014,
  "median_house_value": 358500,
  "ocean_proximity": "NEAR BAY"
}
```

**Exemple de réponse** :
```json
{
  "message": "Maison ajoutée avec succès !"
}
```

---

## **Notes**

1. La base de données et les tables sont automatiquement créées si elles n’existent pas.
2. Les erreurs d'exécution sont affichées dans la console. Active le mode debug de Flask pour des détails supplémentaires.

---

## **Dépannage**

### **Problèmes fréquents** :
- **Erreur de connexion** : Vérifie que PostgreSQL est démarré et que les identifiants sont corrects.
- **Module manquant** : Exécute `pip install -r requirements.txt` pour installer les dépendances manquantes.

### **Logs** :
Tous les journaux sont affichés dans la console. Utilise `debug=True` pour des détails lors du développement.

---

## **Licence**

Ce projet est sous licence MIT.
