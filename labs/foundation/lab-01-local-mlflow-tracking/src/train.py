from pathlib import Path
import json

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from mlflow.tracking import MlflowClient
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


LAB_DIR = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = LAB_DIR / "outputs"
BEST_MODEL_DIR = OUTPUTS_DIR / "best_model"
ARTIFACTS_DIR = LAB_DIR / "artifacts"
MLFLOW_DB = LAB_DIR / "mlflow.db"

EXPERIMENT_NAME = "foundation-lab-01-local-mlflow-tracking"

OUTPUTS_DIR.mkdir(exist_ok=True)
BEST_MODEL_DIR.mkdir(exist_ok=True)
ARTIFACTS_DIR.mkdir(exist_ok=True)

mlflow.set_tracking_uri(f"sqlite:///{MLFLOW_DB}")

client = MlflowClient()
experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

if experiment is None:
    client.create_experiment(
        name=EXPERIMENT_NAME,
        artifact_location=ARTIFACTS_DIR.as_uri()
    )

mlflow.set_experiment(EXPERIMENT_NAME)


def load_dataset():
    dataset = load_diabetes(as_frame=True)

    X = dataset.data
    y = dataset.target

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def train_and_log_model(alpha, X_train, X_test, y_train, y_test):
    model = Ridge(alpha=alpha)

    with mlflow.start_run(run_name=f"ridge-alpha-{alpha}") as run:
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        rmse = float(np.sqrt(mean_squared_error(y_test, predictions)))
        mae = float(mean_absolute_error(y_test, predictions))
        r2 = float(r2_score(y_test, predictions))

        mlflow.log_param("model_type", "Ridge")
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        mlflow.sklearn.log_model(
            sk_model=model,
            name="model"
        )

        run_result = {
            "run_id": run.info.run_id,
            "alpha": alpha,
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }

        print(
            f"Run completed | alpha={alpha} | "
            f"rmse={rmse:.4f} | mae={mae:.4f} | r2={r2:.4f}"
        )

        return run_result, model


def main():
    X_train, X_test, y_train, y_test = load_dataset()

    alpha_values = [0.01, 0.1, 1.0, 10.0]

    all_results = []
    best_result = None
    best_model = None

    for alpha in alpha_values:
        result, model = train_and_log_model(
            alpha,
            X_train,
            X_test,
            y_train,
            y_test
        )

        all_results.append(result)

        if best_result is None or result["rmse"] < best_result["rmse"]:
            best_result = result
            best_model = model

    summary = {
        "experiment_name": EXPERIMENT_NAME,
        "selection_metric": "rmse",
        "best_run": best_result,
        "all_runs": all_results
    }

    summary_path = OUTPUTS_DIR / "training_summary.json"
    with summary_path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    best_model_path = BEST_MODEL_DIR / "model.joblib"
    joblib.dump(best_model, best_model_path)

    print("")
    print("Best model selected")
    print(f"Best alpha: {best_result['alpha']}")
    print(f"Best RMSE : {best_result['rmse']:.4f}")
    print(f"Best model saved to: {best_model_path}")
    print(f"Training summary saved to: {summary_path}")
    print("")
    print("To open MLflow UI, run this from the lab folder:")
    print("mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000")


if __name__ == "__main__":
    main()
