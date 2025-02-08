import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib
from flask import Flask

# Créer l'application Flask
app = Flask(__name__)

# Définir une route pour démarrer l'entraînement
@app.route('/')
def home():
    # Appeler la fonction pour entraîner le modèle
    return train_model()

def train_model():
    # Charger les données
    data = pd.read_csv("housing.csv")

    X = data.drop(columns=["median_house_value"])
    y = data["median_house_value"]
    # Séparer les features et la cible
    X = X.dropna()
    y = y.loc[X.index]  # Garde uniquement les valeurs correspondantes

    # Encoder les colonnes catégoriques
    X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

    # Diviser les données en jeu d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Démarrer un run MLflow
    with mlflow.start_run():
        # Initialiser le modèle
        model = LinearRegression()
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_params({
        "test_size": 0.2,
        "random_state": 42
        })

        # Entraînement
        model.fit(X_train, y_train)

        # Prédictions et métriques
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mlflow.log_metric("mse", mse)

        # Sauvegarde du modèle MLflow
        signature = infer_signature(X_test, y_pred)
        mlflow.sklearn.log_model(model, "housingpricemodel", signature=signature)

        # Sauvegarde traditionnelle pour compatibilité
        joblib.dump(model, "model.pkl")

    return "Model training has started!"

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

