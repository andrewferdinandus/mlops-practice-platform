# MLOps Tool Map

MLOps uses many tools. This can feel confusing at the beginning.

The easiest way to understand the tools is to connect each tool to the problem it solves.

## Simple Tool Map

    Problem: Track model experiments
    Tool: MLflow

    Problem: Package code and dependencies
    Tool: Docker

    Problem: Run multiple local services together
    Tool: Docker Compose

    Problem: Serve a model as an API
    Tool: FastAPI

    Problem: Store model artifacts like object storage
    Tool: MinIO

    Problem: Run containers using Kubernetes locally
    Tool: kind or k3d

    Problem: Collect service metrics
    Tool: Prometheus

    Problem: View dashboards
    Tool: Grafana

    Problem: Check data drift and data quality
    Tool: Evidently

    Problem: Run simple automation on code changes
    Tool: GitHub Actions

## MLflow

MLflow helps track machine learning experiments.

It can store:

    parameters
    metrics
    artifacts
    model information

Use MLflow when you need to answer:

    Which model performed best?
    Which parameters were used?
    Where are the artifacts?
    Can I compare multiple runs?

## Docker

Docker helps package code, dependencies, and runtime settings.

Use Docker when you need to answer:

    Can this workflow run on another machine?
    Are the dependencies consistent?
    Can I package this training or serving code?

Docker is useful for both training and serving workflows.

## Docker Compose

Docker Compose helps run multiple containers together.

Example local stack:

    MLflow
    MinIO
    FastAPI
    Prometheus
    Grafana

Use Docker Compose when one service is not enough and multiple services need to work together.

## FastAPI

FastAPI helps create APIs in Python.

For MLOps, FastAPI is often used to serve a trained model.

Example:

    input: customer details
    output: prediction

Use FastAPI when an application needs to call the model and receive predictions.

## MinIO

MinIO is local object storage.

It is useful for learning object storage concepts without using cloud storage.

In real production systems, object storage may be AWS S3, Azure Blob Storage, or Google Cloud Storage.

In local practice, MinIO can be used to store:

    model files
    reports
    datasets
    artifacts

## kind and k3d

kind and k3d help run Kubernetes locally.

They are useful because managed cloud Kubernetes can cost money.

Use kind or k3d when learning:

    pods
    deployments
    services
    port forwarding
    local Kubernetes cleanup

## Prometheus

Prometheus collects metrics.

For a model API, Prometheus can collect:

    request count
    error count
    response time
    resource usage

Metrics help understand how the service behaves over time.

## Grafana

Grafana helps create dashboards.

Prometheus stores the metrics. Grafana shows those metrics visually.

Use Grafana when you want to see:

    API traffic
    latency trends
    error trends
    service health

## Evidently

Evidently helps analyze data quality and data drift.

Use Evidently when you need to compare:

    reference data
    current data

It can generate reports that help identify whether input data has changed.

## GitHub Actions

GitHub Actions helps run automation when code changes.

Examples:

    run tests
    check formatting
    build Docker image
    validate files

For this learning platform, GitHub Actions should be introduced carefully and kept lightweight.

## How the Tools Connect

A simple local MLOps workflow can look like this:

    Train model with Python
        |
        v
    Track experiment with MLflow
        |
        v
    Save model artifact
        |
        v
    Serve model with FastAPI
        |
        v
    Package service with Docker
        |
        v
    Monitor service with Prometheus and Grafana
        |
        v
    Check data quality and drift with Evidently

## Simple Summary

Do not try to learn every tool at once.

Start with the problem.

Then learn the tool that solves that problem.

Recommended order:

    MLflow
    Docker
    FastAPI
    MinIO
    Docker Compose
    Evidently
    Prometheus and Grafana
    kind or k3d
    GitHub Actions
