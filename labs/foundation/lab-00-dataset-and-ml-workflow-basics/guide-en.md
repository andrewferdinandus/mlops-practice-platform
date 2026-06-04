# Guide - Foundation Lab 00: Dataset and ML Workflow Basics

## What You Will Learn

This lab explains the basic machine learning workflow before using MLOps tools such as MLflow, Docker, Kubernetes, or monitoring systems.

You will learn:

    what a dataset is
    what features are
    what a target value is
    why data is split into training and testing sets
    what model training means
    what model evaluation means
    what metrics are
    what a saved model file is
    how predictions are generated from a saved model

This lab is intentionally simple. The goal is to understand the basic workflow before moving into experiment tracking in Lab 01.

## Where This Lab Fits in MLOps

This lab belongs to the early part of the MLOps lifecycle.

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
        |
        v
    Experiment tracking in the next lab

In this lab, you are not deploying a model yet.

You are learning the basic workflow that happens before tracking, packaging, serving, deploying, and monitoring a model.

## Real-world Business Example

Imagine a retail company wants to predict weekly sales for each store.

The company may have historical data like this:

    store size
    location
    number of employees
    promotion amount
    season
    previous week sales

The company wants to predict:

    next week sales

In machine learning terms:

    features = input columns used by the model
    target   = value the model tries to predict

For the retail example:

    features could be store size, location, promotion amount, and previous sales
    target could be next week sales

A model learns patterns from past data and uses those patterns to make predictions for new data.

## Dataset Used in This Lab

This lab uses a small built-in sample dataset from scikit-learn.

The dataset is loaded directly from Python, so you do not need to download any external data.

Important note:

    This dataset is used only for learning.
    The goal is not to build a medical production model.
    The goal is to understand the basic machine learning workflow.

The same workflow can later be applied to business problems such as sales prediction, customer churn prediction, fraud detection, or demand forecasting.

## Basic Concepts

### Dataset

A dataset is a collection of rows and columns.

Each row usually represents one record.

Each column represents a piece of information.

In a business example, one row might represent one store for one week.

### Features

Features are the input columns used by the model.

Examples:

    store size
    location
    promotion amount
    customer count
    previous sales

In this lab, the feature columns are:

    age
    sex
    bmi
    bp
    s1
    s2
    s3
    s4
    s5
    s6

You do not need to understand each medical column deeply for this lab.

The important idea is:

    features are inputs

### Target

The target is the value the model tries to predict.

In a sales prediction example:

    target = next week sales

In this lab:

    target = the value provided by the sample dataset

The important idea is:

    target is the answer the model learns to predict

### Training Data and Test Data

The full dataset is split into two parts:

    training data
    test data

Training data is used to teach the model.

Test data is used to check how well the model performs on data it has not seen during training.

This matters because a model should not only memorize training data. It should also work reasonably well on new data.

### Model Training

Model training means the model learns patterns from the training data.

In this lab, the model looks at input features and learns how they relate to the target value.

The script trains one simple Ridge Regression model.

You do not need to fully understand Ridge Regression for this lab.

For now, think of the model as:

    a prediction function learned from data

### Model Evaluation

After training, the model is tested using the test dataset.

The model generates predictions.

Then those predictions are compared with the actual target values.

This comparison gives model performance metrics.

### Metrics

Metrics are numbers that show how well the model performed.

This lab saves:

    RMSE
    MAE
    R2

For this beginner lab, focus mainly on RMSE.

Simple idea:

    lower RMSE usually means smaller prediction errors

### Model File

After training, the model is saved as a file:

    outputs/model/basic_model.joblib

This file is a saved version of the trained model.

A saved model can be loaded later to generate predictions without training again.

### Predictions

The script also creates sample predictions:

    outputs/basic_predictions.csv

This file shows:

    input features
    actual target value
    predicted target value

This helps you see how the model output compares with the real value.

## Local Architecture

This lab runs fully on your local machine.

    Python script
        |
        v
    Built-in sample dataset
        |
        v
    Basic model training
        |
        v
    Metrics and saved model
        |
        v
    Output files

No Docker, cloud account, or Kubernetes cluster is required.

## Files Created by This Lab

After running the scripts, the lab creates these files:

    outputs/dataset_preview.csv
        First few rows of the dataset.

    outputs/dataset_summary.json
        Basic information such as row count, feature count, and target column.

    outputs/feature_summary.csv
        Statistical summary of dataset columns.

    outputs/model/basic_model.joblib
        Saved trained model file.

    outputs/basic_metrics.json
        Model performance metrics.

    outputs/basic_predictions.csv
        Sample predictions from the saved model.

## Step 1: Go to the Lab Folder

From the repository root:

    cd labs/foundation/lab-00-dataset-and-ml-workflow-basics

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

This installs the Python libraries needed for the lab.

## Step 5: Explore the Dataset

Run:

    python src/explore_data.py

This script loads the dataset and creates summary files.

Expected output includes:

    Dataset exploration completed
    Rows: 442
    Features: 10
    Target column: target

## Step 6: Train a Basic Model

Run:

    python src/train_basic_model.py

This script:

    loads the dataset
    splits data into train and test sets
    trains one model
    evaluates the model
    saves metrics
    saves the trained model
    saves sample predictions

Expected output includes:

    Basic model training completed
    Training rows: 353
    Test rows: 89
    Feature count: 10

You should also see metric values such as RMSE, MAE, and R2.

## Step 7: Check Generated Outputs

Run:

    ls -la outputs
    ls -la outputs/model

You should see files such as:

    dataset_preview.csv
    dataset_summary.json
    feature_summary.csv
    basic_metrics.json
    basic_predictions.csv
    model/basic_model.joblib

View the dataset summary:

    cat outputs/dataset_summary.json

View the model metrics:

    cat outputs/basic_metrics.json

View sample predictions:

    head outputs/basic_predictions.csv

## What Result Did You Produce?

By the end of this lab, you produced:

    a dataset summary
    a feature summary
    a trained model file
    model metrics
    sample predictions

This means you completed a basic ML workflow locally.

## Why This Matters in MLOps

MLOps does not start with Kubernetes or deployment.

It starts with understanding the ML workflow:

    What data is used?
    What is the target?
    How was the model trained?
    How was it evaluated?
    Where is the model saved?
    Can the output be checked later?

Without this basic workflow, experiment tracking, model serving, monitoring, and deployment will not make sense.

## Connection to Lab 01

Lab 00 trains one model and saves one result.

Lab 01 will take the next step.

In Lab 01, you will:

    train multiple model runs
    change parameter values
    track parameters with MLflow
    track metrics with MLflow
    save model artifacts with MLflow
    compare runs in the MLflow UI
    select the best model

Simple connection:

    Lab 00 = learn the basic ML workflow
    Lab 01 = track the workflow using MLflow

## Common Mistakes

### Virtual environment is not active

If packages are missing, activate the virtual environment:

    source .venv/bin/activate

### Running commands from the wrong folder

Make sure you are inside the Lab 00 folder:

    pwd

Expected path should end with:

    labs/foundation/lab-00-dataset-and-ml-workflow-basics

### Output folder is missing

The scripts create the outputs folder automatically.

If needed, you can recreate it:

    mkdir -p outputs
    touch outputs/.gitkeep

## Cleanup

Use the cleanup guide:

    cleanup.md

Basic cleanup command:

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

You learned the basic workflow that comes before MLOps tooling:

    load data
    understand features and target
    split data
    train a model
    evaluate a model
    save a model
    generate predictions

This foundation is needed before learning MLflow experiment tracking in the next lab.
