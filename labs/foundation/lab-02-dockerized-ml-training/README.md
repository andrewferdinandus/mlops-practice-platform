# Foundation Lab 02: Dockerized ML Training

This lab introduces Dockerized machine learning training.

In Lab 00, you learned the basic ML workflow.

In Lab 01, you tracked model training runs using MLflow.

In this lab, you package the training environment with Docker and run the training script inside a container.

## Where This Lab Fits in MLOps

This lab belongs to the reproducible training environment stage of the MLOps lifecycle.

    Data understanding
        |
        v
    Basic model training
        |
        v
    Experiment tracking
        |
        v
    Reproducible training environment
        |
        v
    Model serving
        |
        v
    Deployment
        |
        v
    Monitoring

This lab does not deploy a model.

This lab does not use Kubernetes or cloud services.

The goal is to understand how Docker helps make ML training more repeatable across machines.

## Why This Lab Matters

A common real-world problem is:

    The training script works on one laptop,
    but fails on another laptop or server.

This can happen because of:

    different Python versions
    different package versions
    missing dependencies
    different operating systems
    local environment differences

Docker helps reduce this problem by packaging:

    Python runtime
    dependencies
    training code
    default run command

## Real-world Business Example

Imagine a retail company trains a weekly sales prediction model.

A data scientist trains the model successfully on their laptop.

Later, another engineer needs to run the same training workflow on a different machine or in a CI pipeline.

If the environment is different, the training may fail.

Docker solves this by defining the training environment in a Dockerfile.

## What You Will Build

You will build a Docker image that contains:

    Python
    required Python packages
    training script
    default training command

Then you will run a Docker container that:

    trains a model
    evaluates the model
    saves metrics
    saves predictions
    saves the trained model
    saves runtime environment details

## Tools Used

    Docker
    Python
    scikit-learn
    pandas
    numpy
    joblib

## Files in This Lab

    Dockerfile
    requirements.txt
    src/train.py
    outputs/

## Local Architecture

    Dockerfile
        |
        v
    Docker image
        |
        v
    Docker container
        |
        v
    Training script runs inside container
        |
        v
    Outputs saved to mounted local outputs/ folder

The important point:

    Training runs inside the container.
    Outputs are saved on the local machine.

## Output Files

After running the container, this lab creates:

    outputs/dockerized_metrics.json
        Model performance metrics.

    outputs/dockerized_predictions.csv
        Sample predictions.

    outputs/runtime_environment.json
        Runtime details from inside the container.

    outputs/model/dockerized_model.joblib
        Saved trained model.

## Quick Start

From this lab folder:

    docker build -t mlops-lab-02-training:latest .

Run training inside the container:

    docker run --rm \
      -v "$(pwd)/outputs:/app/outputs" \
      mlops-lab-02-training:latest

Check outputs:

    ls -la outputs
    ls -la outputs/model
    cat outputs/dockerized_metrics.json
    cat outputs/runtime_environment.json
    head outputs/dockerized_predictions.csv

## Expected Result

You should see output similar to:

    Dockerized training completed
    Python version: 3.12.x
    scikit-learn version: ...
    Training rows: 353
    Test rows: 89
    Feature count: 10
    RMSE: 55.4745

You should also see files in the local outputs folder.

## Why the Volume Mount Matters

The container is temporary.

If outputs are saved only inside the container, they may be lost after the container exits.

This command connects the local outputs folder to the container outputs folder:

    -v "$(pwd)/outputs:/app/outputs"

Meaning:

    local outputs/ folder
        is connected to
    container /app/outputs folder

This allows model files and metrics to remain on the local machine.

## Guides

English guide:

    guide-en.md

Sinhala guide:

    guide-si.md

Cleanup guide:

    cleanup.md

## Connection to Previous Labs

Lab 00:

    basic ML workflow

Lab 01:

    experiment tracking with MLflow

Lab 02:

    reproducible training environment with Docker

## Next Lab

The next lab introduces model serving with FastAPI.

That lab will show how a saved model can be loaded by an API and used to return predictions.
