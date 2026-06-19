from pathlib import Path
import json

import joblib
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs"

MODELS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    dataset = load_diabetes(as_frame=True)

    X = dataset.data
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    rmse = float(np.sqrt(mean_squared_error(y_test, predictions)))
    mae = float(mean_absolute_error(y_test, predictions))
    r2 = float(r2_score(y_test, predictions))

    model_path = MODELS_DIR / "model.joblib"
    metrics_path = OUTPUTS_DIR / "training_metrics.json"
    features_path = MODELS_DIR / "feature_names.json"

    joblib.dump(model, model_path)

    with features_path.open("w", encoding="utf-8") as file:
        json.dump(list(X.columns), file, indent=2)

    metrics = {
        "model_type": "Ridge Regression",
        "alpha": 1.0,
        "train_rows": int(X_train.shape[0]),
        "test_rows": int(X_test.shape[0]),
        "feature_count": int(X_train.shape[1]),
        "metrics": {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        },
        "mlops_stage": "model serving preparation"
    }

    with metrics_path.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=2)

    print("Model training completed")
    print(f"Model saved to: {model_path}")
    print(f"Feature names saved to: {features_path}")
    print(f"Metrics saved to: {metrics_path}")
    print("")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"R2  : {r2:.4f}")


if __name__ == "__main__":
    main()
