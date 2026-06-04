from pathlib import Path
import json

import pandas as pd
from sklearn.datasets import load_diabetes


LAB_DIR = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = LAB_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)


def main():
    dataset = load_diabetes(as_frame=True)

    features = dataset.data
    target = dataset.target

    data = features.copy()
    data["target"] = target

    dataset_info = {
        "dataset_name": "scikit-learn diabetes sample dataset",
        "purpose": "learning basic ML workflow concepts",
        "row_count": int(data.shape[0]),
        "feature_count": int(features.shape[1]),
        "target_column": "target",
        "feature_columns": list(features.columns),
        "important_note": (
            "This dataset is used only for learning. "
            "The goal of this lab is to understand the ML workflow, "
            "not to build a medical production model."
        )
    }

    preview_path = OUTPUTS_DIR / "dataset_preview.csv"
    summary_path = OUTPUTS_DIR / "dataset_summary.json"
    feature_summary_path = OUTPUTS_DIR / "feature_summary.csv"

    data.head(10).to_csv(preview_path, index=False)

    with summary_path.open("w", encoding="utf-8") as file:
        json.dump(dataset_info, file, indent=2)

    data.describe().to_csv(feature_summary_path)

    print("Dataset exploration completed")
    print("")
    print(f"Rows: {dataset_info['row_count']}")
    print(f"Features: {dataset_info['feature_count']}")
    print(f"Target column: {dataset_info['target_column']}")
    print("")
    print("Feature columns:")
    for column in dataset_info["feature_columns"]:
        print(f"- {column}")

    print("")
    print(f"Dataset preview saved to: {preview_path}")
    print(f"Dataset summary saved to: {summary_path}")
    print(f"Feature summary saved to: {feature_summary_path}")


if __name__ == "__main__":
    main()
