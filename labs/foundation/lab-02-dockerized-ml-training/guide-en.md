# Guide - Foundation Lab 02: Dockerized ML Training

## What You Will Learn

This lab teaches how to run a machine learning training workflow inside a Docker container.

You will learn:

    why Docker is useful in MLOps
    what problem Docker solves in ML training
    what a Dockerfile is
    what a Docker image is
    what a Docker container is
    how to build a Docker image
    how to run model training inside a container
    how to save model outputs back to your local machine
    how to clean up Docker images and generated files

This lab builds on Lab 00 and Lab 01.

Lab 00 taught the basic ML workflow.

Lab 01 taught experiment tracking with MLflow.

Lab 02 teaches how to make the training environment more repeatable using Docker.

## Where This Lab Fits in MLOps

This lab belongs to the reproducible training environment stage of the MLOps lifecycle.

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
    Reproducible training environment
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

    reproducible training environment
    dependency packaging
    containerized training
    output persistence

This lab does not deploy a model.

This lab does not use Kubernetes or cloud services.

Those topics come later.

## Why This Lab Matters

A common real-world problem in machine learning projects is:

    The training script works on one machine,
    but fails on another machine.

This can happen because of:

    different Python versions
    different package versions
    missing dependencies
    different operating systems
    different local setup

This is often called the:

    works on my machine problem

For MLOps, this is dangerous.

A training workflow should not depend only on one person's laptop.

The same workflow should be able to run on:

    another developer's laptop
    a training server
    a CI pipeline
    a scheduled job
    a production-like environment

Docker helps package the training environment so it can run more consistently.

## Real-world Business Example

Imagine a retail company wants to train a weekly sales prediction model.

A data scientist trains the model successfully on their laptop.

Later, the ML engineer needs to run the same training workflow on a different server.

The server has:

    a different Python version
    missing packages
    different package versions

The training script fails.

This delays the project.

With Docker, the team can define the training environment once:

    Python version
    required packages
    source code
    run command

Then the same Docker image can be used to run the training workflow more consistently.

## Key Concepts

### Dockerfile

A Dockerfile is a text file that describes how to build a Docker image.

It defines things such as:

    base image
    working directory
    files to copy
    packages to install
    default command to run

In this lab, the Dockerfile uses:

    python:3.12-slim

This means the container uses Python 3.12, even if your laptop has a different Python version.

### Docker Image

A Docker image is a packaged environment.

It contains:

    Python runtime
    installed dependencies
    training code
    default command

You can think of an image as a reusable training package.

In this lab, the image name is:

    mlops-lab-02-training:latest

### Docker Container

A container is a running instance of an image.

When you run the image, Docker starts a container.

In this lab, the container runs:

    python src/train.py

After the training finishes, the container stops.

Because this lab uses:

    --rm

the container is automatically removed after it exits.

### Volume Mount

A container is temporary.

If the model output is saved only inside the container, it may disappear when the container stops.

A volume mount connects a local folder to a folder inside the container.

In this lab:

    local outputs/ folder
        connects to
    container /app/outputs folder

The command is:

    -v "$(pwd)/outputs:/app/outputs"

This allows the training script inside the container to save files to your local machine.

## What This Lab Builds

This lab builds a Dockerized training workflow.

The workflow:

    builds a Docker image
    installs Python dependencies inside the image
    copies the training script into the image
    runs the training script inside a container
    saves model outputs to the local outputs folder

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
    /app/outputs inside container
        |
        v
    outputs/ folder on local machine

Important idea:

    Training runs inside Docker.
    Outputs are saved outside Docker on your local machine.

## Files in This Lab

    Dockerfile
        Defines the container training environment.

    requirements.txt
        Python packages installed inside the image.

    src/train.py
        Training script that runs inside the container.

    outputs/
        Local folder where generated files are saved.

## Output Files

After the container runs, this lab creates:

    outputs/dockerized_metrics.json
        Model performance metrics.

    outputs/dockerized_predictions.csv
        Sample predictions.

    outputs/runtime_environment.json
        Runtime environment details from inside the container.

    outputs/model/dockerized_model.joblib
        Saved trained model file.

## Step 1: Go to the Lab Folder

From the repository root:

    cd labs/foundation/lab-02-dockerized-ml-training

## Step 2: Build the Docker Image

Run:

    docker build -t mlops-lab-02-training:latest .

This command builds a Docker image from the Dockerfile.

The image name is:

    mlops-lab-02-training

The tag is:

    latest

The dot at the end means:

    use the current folder as the Docker build context

## Step 3: Run Training Inside the Container

Run:

    docker run --rm \
      -v "$(pwd)/outputs:/app/outputs" \
      mlops-lab-02-training:latest

This command starts a container from the image.

The container runs the training script.

The important parts are:

    --rm
        Automatically remove the container after it finishes.

    -v "$(pwd)/outputs:/app/outputs"
        Mount the local outputs folder into the container.

    mlops-lab-02-training:latest
        Docker image to run.

## Step 4: Check the Training Output

Expected terminal output includes:

    Dockerized training completed
    Python version: 3.12.x
    scikit-learn version: ...
    Training rows: 353
    Test rows: 89
    Feature count: 10
    RMSE: 55.4745
    MAE : 46.1389
    R2  : 0.4192

The exact values may be slightly different depending on package versions.

## Step 5: Verify Local Output Files

Run:

    ls -la outputs
    ls -la outputs/model

You should see:

    dockerized_metrics.json
    dockerized_predictions.csv
    runtime_environment.json
    model/dockerized_model.joblib

View model metrics:

    cat outputs/dockerized_metrics.json

View runtime environment:

    cat outputs/runtime_environment.json

View sample predictions:

    head outputs/dockerized_predictions.csv

## What the Runtime Environment File Shows

The file:

    outputs/runtime_environment.json

shows details from inside the container.

Example:

    Python version
    platform
    scikit-learn version
    running_inside_container

This is important because it proves the training ran inside the Docker environment, not directly on your laptop Python environment.

## What Result Did You Produce?

By the end of this lab, you produced:

    a Docker image
    a containerized training run
    a saved model file
    model metrics
    sample predictions
    runtime environment details

This means you completed a Dockerized ML training workflow.

## Why This Matters in Real MLOps

Dockerized training helps teams make ML workflows more repeatable.

It helps answer:

    Which Python version was used?
    Which packages were installed?
    Can another person run the same training workflow?
    Can this training run later in CI or on a training server?
    Are outputs saved outside the temporary container?

This is an important step before production-like MLOps workflows.

## Common Issues

### Docker is not running

If you see an error like:

    Cannot connect to the Docker daemon

Start Docker Desktop and try again.

Check Docker:

    docker ps

### Docker command not found

If you see:

    docker: command not found

Docker is not installed or not available in your terminal PATH.

Install Docker Desktop and open a new terminal.

### Permission issue on Linux

If Docker gives a permission error on Linux, try:

    sudo docker ps

A better long-term fix is to add your user to the Docker group.

### outputs folder is empty

If the container runs but outputs are missing, check the volume mount:

    -v "$(pwd)/outputs:/app/outputs"

Make sure you are running the docker run command from the Lab 02 folder.

Check current folder:

    pwd

Expected path should end with:

    labs/foundation/lab-02-dockerized-ml-training

### Image already exists

If you rebuild the image, Docker may reuse cached layers.

That is normal.

To rebuild without cache:

    docker build --no-cache -t mlops-lab-02-training:latest .

### Remove Docker image

To remove the image:

    docker rmi mlops-lab-02-training:latest

If the image does not exist, Docker may show an error. That is okay.

## Cleanup

Use the cleanup guide:

    cleanup.md

Basic cleanup commands:

    docker rmi mlops-lab-02-training:latest

    rm -rf outputs
    mkdir -p outputs
    touch outputs/.gitkeep

This lab uses:

    --rm

so the container is automatically removed after the run finishes.

## Cost Note

This lab runs locally using Docker.

Expected cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, Docker image storage, and disk usage

## What You Learned

You learned how to:

    write a Dockerfile for ML training
    build a Docker image
    run a training script inside a container
    mount a local outputs folder into the container
    save model outputs outside the container
    verify runtime environment details
    clean up Docker images and generated outputs

## Connection to Previous Labs

Lab 00:

    You learned the basic ML workflow.

Lab 01:

    You learned how to track model experiments with MLflow.

Lab 02:

    You learned how to run the training workflow inside a Docker container.

## Connection to the Next Lab

The next lab introduces FastAPI model serving.

That lab will show how to load a saved model and expose it through an API.

Simple connection:

    Lab 02 = package and run training with Docker
    Lab 03 = serve a trained model through an API
