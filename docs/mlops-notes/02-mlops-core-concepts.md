# MLOps Core Concepts

This note explains the basic MLOps terms you will see in the labs.

The goal is to understand the meaning of each concept before using tools like MLflow, Docker, FastAPI, MinIO, Prometheus, Grafana, and Evidently.

## Experiment

An experiment is a group of model training attempts that belong to the same goal.

Example:

    House price prediction experiment

Inside this experiment, you may train many models with different settings.

## Run

A run is one training attempt inside an experiment.

Example:

    Run 1: train model with max_depth = 3
    Run 2: train model with max_depth = 5
    Run 3: train model with max_depth = 10

Each run can have different parameters, metrics, and artifacts.

## Parameter

A parameter is a setting used before or during training.

Examples:

    learning_rate = 0.01
    max_depth = 5
    n_estimators = 100
    batch_size = 32

Parameters help explain how a model was trained.

If a model performs well, parameters help reproduce that result later.

## Metric

A metric is a number that tells you how well the model performed.

Examples:

    accuracy = 0.87
    precision = 0.84
    recall = 0.80
    f1_score = 0.82
    rmse = 1200.50

Metrics help compare different model runs.

## Artifact

An artifact is a file created during training, evaluation, or inference.

Examples:

    trained model file
    confusion matrix image
    metrics report
    prediction output
    data validation report
    drift report

Artifacts should be saved clearly so they can be reused later.

## Model

A model is the trained machine learning object that can make predictions.

Example:

    A house price model predicts the price of a house.
    A fraud detection model predicts whether a transaction is risky.
    A churn model predicts whether a customer may leave.

In MLOps, the model file must be saved, versioned, tested, and deployed carefully.

## Model Version

A model version is a specific saved version of a model.

Example:

    house-price-model:v1
    house-price-model:v2
    house-price-model:v3

Model versions help identify which model was used at a specific time.

This is important for debugging, rollback, and comparison.

## Model Registry

A model registry is a place where model versions are organized and managed.

A model registry can track stages such as:

    candidate
    approved
    staging
    production
    archived

A registry helps teams decide which model is ready to use.

## Pipeline

A pipeline is a set of steps that run in order.

A simple ML pipeline can look like this:

    load data
    validate data
    train model
    evaluate model
    save model
    generate report

Pipelines make ML workflows repeatable.

## Reproducibility

Reproducibility means getting the same or very similar result when the workflow is run again.

To improve reproducibility, you need to track:

    code version
    data version
    parameters
    environment
    dependencies
    random seed
    model artifacts

Without reproducibility, it becomes difficult to trust model results.

## Model Serving

Model serving means making a trained model available for predictions.

Common serving methods:

    API serving
    batch inference
    streaming inference
    embedded model inside an application

In beginner labs, API serving with FastAPI is a simple and practical starting point.

## Batch Inference

Batch inference means running predictions for many records at once.

Example:

    input file: customers.csv
    output file: predictions.csv

Batch inference is useful for scheduled jobs, reports, and offline predictions.

## Monitoring

Monitoring means checking whether the system is working correctly over time.

For a model API, monitoring can include:

    request count
    response time
    error count
    CPU and memory usage

For ML quality, monitoring can include:

    prediction distribution
    input data changes
    model performance
    drift signals

## Data Drift

Data drift happens when current data becomes different from the data used to train the model.

Example:

    A model was trained on January customer behavior.
    By June, customer behavior has changed.
    The model may no longer perform well.

Data drift does not always mean the model is broken, but it is a warning sign.

## Deployment

Deployment means releasing a model or model service so it can be used.

Examples:

    run model API in Docker
    deploy model service to Kubernetes
    publish batch inference job
    promote a model to production

Deployment should include testing and rollback planning.

## Rollback

Rollback means returning to a previous working version when a new version has problems.

Example:

    model v3 has errors
    switch back to model v2

Rollback is important because new models can fail even if they looked good during testing.

## Cleanup

Cleanup means removing resources created during a lab or workflow.

Examples:

    stop containers
    delete Docker volumes
    remove temporary files
    delete local Kubernetes clusters
    remove generated artifacts

Cleanup is important because it keeps the environment clean and avoids unnecessary cost.

## Simple Summary

MLOps is easier to understand when the main concepts are clear.

The most important concepts are:

    experiment
    run
    parameter
    metric
    artifact
    model version
    model registry
    pipeline
    reproducibility
    serving
    monitoring
    drift
    deployment
    rollback
    cleanup

The labs will show how these concepts work in practice.
