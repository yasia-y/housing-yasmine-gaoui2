from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Charger les données
data = pd.read_csv("housing.csv")

# Séparer les features et la cible
X = data.drop(columns=["median_house_value"])
y = data["median_house_value"]

# Encoder les colonnes catégoriques
X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

# Diviser les données en jeu d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Sauvegarder le modèle
import joblib
joblib.dump(model, "model.pkl")
