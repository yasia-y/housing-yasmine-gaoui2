import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib

# Charger les données
data = pd.read_csv("housing.csv")

# Séparer les features et la cible
X = data.drop(columns=["median_house_value"])
y = data["median_house_value"]

# Encoder les colonnes catégoriques
X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

# Diviser les données en jeu d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Démarrer un run MLflow
with mlflow.start_run():
    # Initialiser le modèle
    model = LinearRegression()
    mlflow.log_param("model_type", "LinearRegression")

    # Entraînement
    model.fit(X_train, y_train)

    # Prédictions et métriques
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mlflow.log_metric("mse", mse)

    # Sauvegarde du modèle MLflow
    mlflow.sklearn.log_model(model, "model")

    # Sauvegarde traditionnelle pour compatibilité
    joblib.dump(model, "model.pkl")
