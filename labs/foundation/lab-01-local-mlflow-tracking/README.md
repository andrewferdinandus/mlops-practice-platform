# Foundation Lab 01: Local MLflow Experiment Tracking

This lab introduces experiment tracking with MLflow.

In Lab 00, you trained one basic model and saved one result.

In this lab, you train the same type of model multiple times using different parameter values. Each training attempt is tracked with MLflow.

## Where This Lab Fits in MLOps

This lab belongs to the experimentation and experiment tracking stage of the MLOps lifecycle.

    Data understanding
        |
        v
    Basic model training
        |
        v
    Experiment tracking
        |
        v
    Model comparison
        |
        v
    Best model selection

This lab does not deploy a model.

This lab does not use Docker, Kubernetes, or cloud services.

The goal is to learn how to keep model training experiments organized before moving to packaging, serving, deployment, and monitoring.

## Why This Lab Matters

In real machine learning projects, a team may train many models with different settings.

Without experiment tracking, it becomes difficult to answer:

    Which model performed best?
    What parameters were used?
    What metrics were produced?
    Where is the model file?
    Can the result be reproduced later?

MLflow helps record this information in an organized way.

## Real-world Business Example

Imagine a retail company wants to predict weekly sales.

A data scientist may train several models with different settings.

For each training attempt, the team needs to know:

    which settings were used
    how well the model performed
    where the trained model was saved
    which model should be used later

This lab uses a small built-in sample dataset from scikit-learn, but the experiment tracking idea is the same for real business problems such as:

    sales prediction
    customer churn prediction
    fraud detection
    demand forecasting
    price prediction

## What You Will Build

You will build a local MLflow experiment tracking workflow.

The training script will:

    load a sample dataset
    train a Ridge Regression model multiple times
    change the alpha parameter for each run
    log parameters to MLflow
    log metrics to MLflow
    log model artifacts to MLflow
    select the best model using RMSE
    save the best model locally
    generate predictions from the saved model

## Tools Used

    Python
    scikit-learn
    MLflow
    pandas
    numpy
    joblib
    SQLite

## Local Architecture

This lab runs fully on your local machine.

    Python training script
        |
        v
    MLflow tracking database
        |
        +--> parameters
        +--> metrics
        +--> run history
        |
        v
    Artifact folder
        |
        +--> MLflow model artifacts

    outputs/
        |
        +--> best model
        +--> training summary
        +--> sample predictions

## Important Files and Folders

    requirements.txt
        Python dependencies for this lab.

    src/train.py
        Trains multiple model runs and logs them to MLflow.

    src/predict.py
        Loads the selected best model and generates sample predictions.

    mlflow.db
        Local SQLite database used by MLflow to store experiment metadata.

    artifacts/
        Folder used by MLflow to store model artifacts.

    outputs/training_summary.json
        Summary of all runs and the selected best run.

    outputs/best_model/model.joblib
        Best model saved locally.

    outputs/sample_predictions.csv
        Sample predictions generated from the saved model.

## Quick Start

From this lab folder:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

Train and track model runs:

    python src/train.py

Generate predictions:

    python src/predict.py

Open MLflow UI:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000

Open in browser:

    http://127.0.0.1:5000

If port 5000 is already in use, use port 5001:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

Then open:

    http://127.0.0.1:5001

## Expected Result

You should see four MLflow runs:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

Each run should contain:

    parameters
    metrics
    model artifact

The best model should be saved to:

    outputs/best_model/model.joblib

Sample predictions should be saved to:

    outputs/sample_predictions.csv

## Guides

English guide:

    guide-en.md

Sinhala guide:

    guide-si.md

Cleanup guide:

    cleanup.md

## Connection to Lab 00

Lab 00 trained one model and saved one result.

Lab 01 trains multiple model runs and tracks each run with MLflow.

Simple connection:

    Lab 00 = basic ML workflow
    Lab 01 = tracked ML experiments with MLflow

## Next Lab

The next lab introduces Dockerized ML training.

That lab will show how to package the training workflow into a reproducible container environment.
