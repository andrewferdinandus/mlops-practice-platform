from pathlib import Path
import json

import joblib
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


LAB_DIR = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = LAB_DIR / "outputs"
MODEL_DIR = OUTPUTS_DIR / "model"

OUTPUTS_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)


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
        "note": (
            "This is a basic model training example. "
            "The next lab will train multiple runs and track them using MLflow."
        )
    }

    model_path = MODEL_DIR / "basic_model.joblib"
    metrics_path = OUTPUTS_DIR / "basic_metrics.json"
    predictions_path = OUTPUTS_DIR / "basic_predictions.csv"

    joblib.dump(model, model_path)

    with metrics_path.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=2)

    prediction_output = X_test.copy()
    prediction_output["actual_target"] = y_test
    prediction_output["predicted_target"] = predictions
    prediction_output.head(20).to_csv(predictions_path, index=False)

    print("Basic model training completed")
    print("")
    print(f"Training rows: {metrics['train_rows']}")
    print(f"Test rows: {metrics['test_rows']}")
    print(f"Feature count: {metrics['feature_count']}")
    print("")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"R2  : {r2:.4f}")
    print("")
    print(f"Model saved to: {model_path}")
    print(f"Metrics saved to: {metrics_path}")
    print(f"Sample predictions saved to: {predictions_path}")


if __name__ == "__main__":
    main()
