from pathlib import Path

import joblib
from sklearn.datasets import load_diabetes


LAB_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = LAB_DIR / "outputs" / "best_model" / "model.joblib"
PREDICTIONS_PATH = LAB_DIR / "outputs" / "sample_predictions.csv"


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}\n"
            "Run src/train.py first."
        )

    model = joblib.load(MODEL_PATH)

    dataset = load_diabetes(as_frame=True)
    sample_data = dataset.data.head(10)

    predictions = model.predict(sample_data)

    result = sample_data.copy()
    result["prediction"] = predictions

    result.to_csv(PREDICTIONS_PATH, index=False)

    print("Sample predictions generated")
    print(f"Model used: {MODEL_PATH}")
    print(f"Predictions saved to: {PREDICTIONS_PATH}")
    print("")
    print(result[["prediction"]].head())


if __name__ == "__main__":
    main()
