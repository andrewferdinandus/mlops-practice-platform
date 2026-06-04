# Guide - Foundation Lab 01: Local MLflow Experiment Tracking

## What You Will Learn

This lab teaches experiment tracking with MLflow.

You will learn:

    what an experiment is
    what a run is
    what parameters are
    what metrics are
    what artifacts are
    why model training runs should be tracked
    how to compare multiple model runs
    how to select the best model
    where MLflow stores experiment data
    how a saved model can be used for predictions

This lab builds directly on Lab 00.

In Lab 00, you trained one model and saved one result.

In Lab 01, you train multiple model runs and track each run using MLflow.

## Where This Lab Fits in MLOps

This lab belongs to the experimentation and experiment tracking stage of the MLOps lifecycle.

A simple MLOps lifecycle looks like this:

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
        |
        v
    Model packaging
        |
        v
    Model serving
        |
        v
    Deployment
        |
        v
    Monitoring

This lab focuses on:

    experiment tracking
    model comparison
    best model selection

This lab does not deploy a model.

This lab does not use Docker, Kubernetes, or cloud services.

Those topics come in later labs.

## Why This Lab Matters

In real machine learning projects, a model is rarely trained only once.

A data scientist or ML engineer may train many versions of a model using different settings.

For example:

    Run 1: alpha = 0.01
    Run 2: alpha = 0.1
    Run 3: alpha = 1.0
    Run 4: alpha = 10.0

After training many versions, important questions appear:

    Which model performed best?
    What settings were used?
    What metrics were produced?
    Where is the model file?
    Can this result be checked later?
    Can another person understand what happened?

Without experiment tracking, these answers can become messy.

MLflow helps organize this information.

## Real-world Business Example

Imagine a retail company wants to predict weekly sales.

The company may train several models using different settings.

Each model may give different results.

The business team wants to know:

    Which model gives the best prediction?
    Which settings created that model?
    Can the model be reused later?
    Where is the saved model file?

In a real company, this information is important before a model is served through an API, deployed to production, or monitored.

This lab uses a small built-in sample dataset from scikit-learn.

The dataset is used only for learning.

The goal is not to build a medical production model.

The goal is to learn how experiment tracking works.

## Key Concepts

### Experiment

An experiment is a group of related training attempts.

In this lab, the experiment is:

    foundation-lab-01-local-mlflow-tracking

This experiment contains multiple training runs.

### Run

A run is one training attempt.

In this lab, each alpha value creates one run.

Example:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

Each run has its own parameters, metrics, and model artifact.

### Parameter

A parameter is a setting used during training.

In this lab, the main parameter is:

    alpha

Think of alpha like a control knob.

Changing alpha changes how the model learns from data.

This lab tests:

    0.01
    0.1
    1.0
    10.0

MLflow records the alpha value for each run.

### Metric

A metric is a number that shows how well the model performed.

This lab records:

    RMSE
    MAE
    R2

For this beginner lab, focus mainly on RMSE.

Simple idea:

    lower RMSE usually means smaller prediction errors

The script selects the best model using the lowest RMSE.

### Artifact

An artifact is a file created during training or evaluation.

In this lab, MLflow saves model artifacts for each run.

The lab also saves the selected best model to:

    outputs/best_model/model.joblib

Artifacts are important because a model result is not useful if the actual model file cannot be found later.

## What This Lab Builds

This lab builds a local experiment tracking workflow.

The training script:

    loads a sample dataset
    trains a Ridge Regression model multiple times
    changes the alpha value for each run
    logs parameters to MLflow
    logs metrics to MLflow
    logs model artifacts to MLflow
    selects the best model using RMSE
    saves the best model locally
    writes a training summary
    generates predictions using the saved model

## Local Architecture

This lab runs fully on your local machine.

    Python training script
        |
        v
    MLflow tracking database
        |
        +--> experiment name
        +--> run history
        +--> parameters
        +--> metrics
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

## Where Data Is Saved

This lab creates several local files and folders.

### mlflow.db

    mlflow.db

This is a local SQLite database.

MLflow uses it to store experiment metadata.

It stores information such as:

    experiment names
    run IDs
    parameters
    metrics
    artifact locations

### artifacts/

    artifacts/

MLflow uses this folder to store model artifacts.

A model artifact is the saved model output from a training run.

### outputs/training_summary.json

    outputs/training_summary.json

This file stores a simple summary of all runs and the selected best run.

### outputs/best_model/model.joblib

    outputs/best_model/model.joblib

This is the selected best model saved as a local file.

The prediction script loads this model.

### outputs/sample_predictions.csv

    outputs/sample_predictions.csv

This file stores sample predictions generated from the saved best model.

## Tools Used

    Python
    scikit-learn
    MLflow
    pandas
    numpy
    joblib
    SQLite

## Step 1: Go to the Lab Folder

From the repository root:

    cd labs/foundation/lab-01-local-mlflow-tracking

## Step 2: Create a Python Virtual Environment

Run:

    python3 -m venv .venv

This creates an isolated Python environment for this lab.

## Step 3: Activate the Virtual Environment

Run:

    source .venv/bin/activate

After activation, your terminal prompt should show:

    (.venv)

This means Python packages will be installed inside this lab environment.

## Step 4: Install Required Packages

Run:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

This installs MLflow, scikit-learn, pandas, numpy, and joblib.

## Step 5: Train and Track Model Runs

Run:

    python src/train.py

This script trains four model runs.

Each run uses a different alpha value.

Expected run names:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

The script logs parameters, metrics, and model artifacts to MLflow.

Expected output includes:

    Run completed | alpha=0.01
    Run completed | alpha=0.1
    Run completed | alpha=1.0
    Run completed | alpha=10.0

You should also see the selected best model.

Example:

    Best model selected
    Best alpha: 0.1
    Best RMSE : 53.4461

The exact numbers may be slightly different depending on package versions.

## Step 6: Generate Predictions

Run:

    python src/predict.py

This script:

    loads the best saved model
    loads sample data
    generates predictions
    saves predictions to CSV

Expected output:

    Sample predictions generated
    Model used: outputs/best_model/model.joblib
    Predictions saved to: outputs/sample_predictions.csv

## Step 7: Open the MLflow UI

Run:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000

Then open this URL in your browser:

    http://127.0.0.1:5000

If port 5000 is already in use, run:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

Then open:

    http://127.0.0.1:5001

Important:

    The terminal running MLflow UI will stay busy.
    That is normal.
    Press Ctrl + C to stop the MLflow UI.

## Step 8: What to Check in MLflow UI

In the MLflow UI, open the experiment:

    foundation-lab-01-local-mlflow-tracking

You should see four runs:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

Click a run and check:

    Parameters
    Metrics
    Artifacts

For parameters, check:

    model_type
    alpha
    test_size
    random_state

For metrics, check:

    rmse
    mae
    r2

For artifacts, check that a model artifact exists.

## How to Compare Runs

The main comparison in this lab is RMSE.

Simple idea:

    lower RMSE usually means better predictions

Compare the RMSE values across the four runs.

The run with the lowest RMSE is selected as the best model.

In the tested output, alpha 0.1 had the lowest RMSE.

That is why the best model was saved from that run.

## Step 9: Check Local Output Files

Run:

    ls -la outputs
    ls -la outputs/best_model

You should see:

    training_summary.json
    sample_predictions.csv
    best_model/model.joblib

View the training summary:

    cat outputs/training_summary.json

View sample predictions:

    head outputs/sample_predictions.csv

## What Result Did You Produce?

By the end of this lab, you produced:

    four tracked MLflow runs
    logged parameters
    logged metrics
    logged model artifacts
    a selected best model
    a training summary
    sample predictions from the saved model

This means you completed a local experiment tracking workflow.

## Why This Matters in Real MLOps

Experiment tracking is one of the first practical skills in MLOps.

It helps teams answer:

    What was trained?
    How was it trained?
    How well did it perform?
    Which run was best?
    Where is the model artifact?
    Can the result be reviewed later?

Without experiment tracking, model development becomes difficult to manage as the number of experiments grows.

## Common Issues

### mlflow command not found

If this happens:

    zsh: command not found: mlflow

Your virtual environment may not be active.

Run:

    source .venv/bin/activate

Then use:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000

Using python -m mlflow is safer because it runs MLflow from the active Python environment.

### Port already in use

If you see:

    Address already in use

Use another port:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

Then open:

    http://127.0.0.1:5001

### Browser opens but no runs appear

First, verify that runs exist in the database:

    python - <<'PY'
    import mlflow

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    runs = mlflow.search_runs(
        experiment_names=["foundation-lab-01-local-mlflow-tracking"]
    )

    print("Runs found:", len(runs))
    print(runs[["run_id", "params.alpha", "metrics.rmse"]])
    PY

If runs are found, restart the MLflow UI and make sure it points to the correct mlflow.db file.

### Pickle or joblib security warning

You may see a warning about pickle, cloudpickle, or joblib model files.

This is a normal security warning.

Only load model files that you trust.

In this lab, the model file is created locally by your own script.

## Cleanup

Use the cleanup guide:

    cleanup.md

Basic cleanup commands:

    rm -f mlflow.db
    rm -rf artifacts/*
    touch artifacts/.gitkeep
    rm -rf outputs
    mkdir -p outputs
    touch outputs/.gitkeep

Optional virtual environment cleanup:

    rm -rf .venv

## Cost Note

This lab runs locally.

Expected cost:

    Cloud cost: 0
    Local cost: small amount of CPU, memory, and disk usage

## What You Learned

You learned how to:

    train multiple model runs
    change parameter values
    log parameters to MLflow
    log metrics to MLflow
    log model artifacts to MLflow
    compare runs in MLflow UI
    select the best model
    save the best model locally
    generate predictions from a saved model

## Connection to the Next Lab

Lab 01 tracks model experiments locally.

The next lab will introduce Dockerized ML training.

That means the training workflow will be packaged into a container so it can run more consistently across different machines.

Simple connection:

    Lab 01 = track experiments
    Lab 02 = make the training environment reproducible with Docker
