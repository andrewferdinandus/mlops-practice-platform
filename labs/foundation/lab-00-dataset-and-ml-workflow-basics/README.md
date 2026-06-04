# Foundation Lab 00: Dataset and ML Workflow Basics

This lab introduces the basic machine learning workflow that appears before experiment tracking.

It helps you understand what data, features, target values, training, evaluation, metrics, model files, and predictions mean before moving into MLflow in Lab 01.

## Where This Lab Fits in MLOps

This lab belongs to the early stage of the MLOps lifecycle:

    Data understanding
        |
        v
    Basic model training
        |
        v
    Basic model evaluation
        |
        v
    Save model output

This lab does not use MLflow, Docker, Kubernetes, or cloud services.

Those tools are introduced later.

## Why This Lab Matters

Before tracking experiments with MLflow, you need to understand the basic workflow:

    load data
    understand input columns
    identify the target value
    split data into training and testing sets
    train a model
    evaluate the result
    save the model
    generate predictions

Lab 01 will build on this workflow by training multiple model runs and tracking them with MLflow.

## Real-world Business Example

Imagine a retail company wants to predict weekly sales.

The company may have input data such as:

    store size
    location
    promotion amount
    season
    previous week sales

The value to predict may be:

    next week sales

In machine learning:

    input columns are called features
    the value to predict is called the target

This lab uses a small built-in dataset from scikit-learn so you do not need to download external data.

The goal is not to build a medical production model. The goal is to understand the basic ML workflow.

## Tools Used

    Python
    pandas
    numpy
    scikit-learn
    joblib

## Files in This Lab

    requirements.txt
    src/explore_data.py
    src/train_basic_model.py
    outputs/

## What the Scripts Do

### explore_data.py

This script loads the sample dataset and creates basic dataset summary files.

It creates:

    outputs/dataset_preview.csv
    outputs/dataset_summary.json
    outputs/feature_summary.csv

### train_basic_model.py

This script trains one basic model, evaluates it, saves the model, and generates predictions.

It creates:

    outputs/model/basic_model.joblib
    outputs/basic_metrics.json
    outputs/basic_predictions.csv

## Quick Start

From this lab folder:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

Explore the dataset:

    python src/explore_data.py

Train the basic model:

    python src/train_basic_model.py

Check outputs:

    ls -la outputs
    cat outputs/dataset_summary.json
    cat outputs/basic_metrics.json
    head outputs/basic_predictions.csv

## Expected Result

You should see:

    dataset summary files
    model metrics
    saved model file
    sample prediction output

## Guides

English guide:

    guide-en.md

Sinhala guide:

    guide-si.md

Cleanup guide:

    cleanup.md

## Next Lab

Next lab:

    Foundation Lab 01: Local MLflow Experiment Tracking

Lab 00 trains one model manually.

Lab 01 trains multiple model runs and tracks parameters, metrics, and artifacts using MLflow.
