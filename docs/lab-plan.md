# Lab Plan

This document defines the detailed hands-on lab sequence for the Low-cost MLOps Practice Platform.

The README and ROADMAP provide the general learning direction. This file contains the detailed lab-by-lab plan.

The plan may be refined as the learning path improves, but the main project README and ROADMAP should stay general and stable.

## Current Repository Areas

The repository is organized into these main areas:

    docs/
        architecture/       Local-first and cost-aware architecture guides
        learning-paths/     High-level learning track descriptions
        mlops-notes/        Beginner-friendly MLOps notes

    labs/
        shared/             Shared setup, cleanup, and troubleshooting guides
        foundation/         Foundation-level hands-on labs
        practitioner/       Practitioner-level hands-on labs
        professional/       Professional-level hands-on labs
        advanced/           Advanced-level hands-on labs

    platform/
        docker/             Reusable Docker-related templates
        mlflow/             Reusable MLflow-related templates
        minio/              Reusable MinIO-related templates
        evidently/          Reusable Evidently-related templates
        kubernetes/         Local Kubernetes templates for kind and k3d
        monitoring/         Prometheus and Grafana templates

    scripts/
        check-prereqs.sh    Local prerequisite checking script
        cleanup-all.sh      Safe cleanup helper script

## Learning Philosophy

MLOps should be learned step by step.

Do not start with too many tools at once.

Start with the problem, then introduce the tool that solves that problem.

Recommended learning flow:

    understand the MLOps problem
        |
        v
    practice one concept locally
        |
        v
    verify the result
        |
        v
    clean up resources
        |
        v
    connect the concept to real-world MLOps

## Core Tool Order

The recommended tool order is:

    1. Git basics
    2. MLflow
    3. Docker
    4. FastAPI
    5. MinIO
    6. DVC
    7. Evidently
    8. Prometheus and Grafana
    9. Kubernetes
    10. Advanced serving, GitOps, governance, and cloud extensions

Git basics are assumed. This project does not teach Git from zero, but learners should understand basic clone, add, commit, and push commands.

## Why This Order?

The order is designed to avoid beginner overload.

    MLflow teaches experiment tracking.
    Docker teaches reproducible environments.
    FastAPI teaches model serving.
    MinIO teaches local object storage.
    DVC teaches data versioning.
    Evidently teaches data quality and drift.
    Prometheus and Grafana teach monitoring.
    Kubernetes teaches deployment and scaling concepts.
    Advanced tools come after the basics are clear.

## Lab Guide Standard

Each lab should include:

    README.md
    guide-en.md
    guide-si.md
    cleanup.md
    requirements.txt if Python packages are needed
    src/ folder if code is needed

Each lab guide should explain:

    what you will build
    why the lab matters
    the concept behind the lab
    a real-world example
    tools used
    local architecture
    step-by-step commands
    what important commands do
    verification steps
    common mistakes
    cleanup steps
    what you learned
    next lab connection

## Lab Design Rules

Each lab should:

    start from a clean or minimal state
    create only what it needs
    avoid depending on previous lab leftovers
    keep cloud usage optional
    include full cleanup
    explain cost clearly
    use simple English and clear Sinhala guides
    avoid unnecessary advanced tools in beginner labs

## Foundation Track

Goal: Learn the basic building blocks of MLOps using local tools.

### Lab 01: Local MLflow Experiment Tracking

Current folder:

    labs/foundation/lab-01-local-mlflow-tracking/

Main concept:

    experiment tracking

Problem:

    After training multiple models, it becomes hard to remember which model performed best and which parameters were used.

Tools:

    Python
    scikit-learn
    MLflow
    pandas
    numpy

Approach:

    Run locally using a Python virtual environment.
    Do not use Docker in this lab.
    Train multiple model runs.
    Log parameters, metrics, and artifacts with MLflow.
    Compare runs in the MLflow UI.

Learner should understand:

    experiment
    run
    parameter
    metric
    artifact
    model comparison
    why tracking matters

### Lab 02: Dockerized ML Training

Main concept:

    reproducible training environment

Problem:

    A training script may work on one laptop but fail on another because dependencies are different.

Tools:

    Docker
    Python
    scikit-learn

Approach:

    Package the training script and dependencies into a Docker image.
    Run training inside a container.

Learner should understand:

    Dockerfile
    image
    container
    dependencies
    reproducibility

### Lab 03: FastAPI Model Serving

Main concept:

    model serving

Problem:

    A trained model is not useful to applications unless it can receive input and return predictions.

Tools:

    FastAPI
    Python
    joblib
    curl

Approach:

    Load a trained model.
    Create a prediction API.
    Test predictions using curl.

Learner should understand:

    API endpoint
    request
    response
    prediction service
    model loading

### Lab 04: Local Model Artifact Management

Main concept:

    artifact organization

Problem:

    Model files can become messy when many versions are created manually.

Tools:

    Python
    local filesystem

Approach:

    Organize models, reports, and outputs in a clear folder structure.

Learner should understand:

    artifact
    model file
    output folder
    naming convention
    basic versioning idea

### Lab 05: MinIO as Local Object Storage

Main concept:

    object storage

Problem:

    Real MLOps systems often store models and artifacts outside the application folder.

Tools:

    MinIO
    Docker Compose
    Python client

Approach:

    Run MinIO locally.
    Create a bucket.
    Upload and download model artifacts.

Learner should understand:

    bucket
    object
    artifact storage
    local S3-compatible storage

### Lab 06: Basic Batch Inference

Main concept:

    batch prediction

Problem:

    Some ML workflows need predictions for many records at once instead of one API request at a time.

Tools:

    Python
    pandas
    saved model artifact

Approach:

    Load a dataset.
    Load a trained model.
    Generate predictions.
    Save output CSV.

Learner should understand:

    batch input
    batch output
    offline prediction
    repeatable inference

## Practitioner Track

Goal: Build repeatable local MLOps workflows by connecting tools together.

### Lab 01: MLflow with MinIO Backend

Main concept:

    separating tracking metadata and artifact storage

Tools:

    MLflow
    MinIO
    Docker Compose

Learner should understand:

    tracking server
    artifact store
    local object storage
    service configuration

### Lab 02: Reproducible Training Pipeline

Main concept:

    pipeline structure

Tools:

    Python
    config files
    Makefile or shell commands

Learner should understand:

    pipeline steps
    config-driven training
    repeatable command structure
    input and output paths

### Lab 03: Data Versioning Basics with DVC

Main concept:

    data versioning

Tools:

    Git
    DVC
    local storage

Learner should understand:

    why Git alone is not enough for large datasets
    how DVC tracks data files
    how data versions connect to code versions

### Lab 04: DVC + MLflow Reproducible Workflow

Main concept:

    reproducibility across code, data, parameters, and metrics

Tools:

    DVC
    MLflow
    Python

Learner should understand:

    code version
    data version
    parameter tracking
    metric tracking
    reproducible experiment workflow

### Lab 05: API Inference with Docker Compose

Main concept:

    multi-service local inference workflow

Tools:

    Docker Compose
    FastAPI
    Python

Learner should understand:

    service dependency
    environment variables
    local API workflow
    container logs

### Lab 06: Basic CI with GitHub Actions

Main concept:

    automated checks

Tools:

    GitHub Actions
    Python

Learner should understand:

    CI workflow
    tests
    dependency installation
    lightweight automation

### Lab 07: Data Validation Checks

Main concept:

    checking data before training or inference

Tools:

    Python
    pandas

Learner should understand:

    schema checks
    missing values
    type checks
    quality gates

### Lab 08: Evidently Data Drift Report

Main concept:

    data drift detection

Tools:

    Evidently
    Python

Learner should understand:

    reference data
    current data
    drift report
    report artifact

### Lab 09: Prometheus Metrics for Model API

Main concept:

    application metrics

Tools:

    FastAPI
    Prometheus client

Learner should understand:

    request count
    error count
    latency
    metrics endpoint

### Lab 10: Local Kubernetes Deployment with kind

Main concept:

    local Kubernetes deployment

Tools:

    kind
    kubectl
    Docker

Learner should understand:

    pod
    deployment
    service
    port-forwarding
    cluster cleanup

## Professional Track

Goal: Practice production-like MLOps patterns locally.

### Lab 01: MLflow + MinIO + PostgreSQL Stack

Main concept:

    production-like MLflow architecture

Tools:

    MLflow
    MinIO
    PostgreSQL
    Docker Compose

Learner should understand:

    backend store
    artifact store
    metadata
    service composition

### Lab 02: FastAPI Model Service on Kubernetes

Main concept:

    model API deployment on Kubernetes

Tools:

    FastAPI
    Docker
    Kubernetes
    kubectl

Learner should understand:

    container image
    deployment
    service
    health check
    port-forwarding

### Lab 03: Prometheus and Grafana Monitoring

Main concept:

    service monitoring and dashboards

Tools:

    Prometheus
    Grafana
    FastAPI

Learner should understand:

    metrics scraping
    dashboard
    request metrics
    error metrics
    latency metrics

### Lab 04: Model Drift Monitoring Workflow

Main concept:

    monitoring ML quality over time

Tools:

    Evidently
    Python
    reports

Learner should understand:

    reference dataset
    current dataset
    drift signal
    review workflow

### Lab 05: Model Registry Workflow

Main concept:

    model lifecycle management

Tools:

    MLflow
    local registry workflow

Learner should understand:

    candidate model
    approved model
    production model
    archived model
    version promotion

### Lab 06: Canary Deployment Practice

Main concept:

    safer release strategy

Tools:

    Kubernetes
    FastAPI

Learner should understand:

    stable version
    candidate version
    traffic split concept
    comparison
    rollback thinking

### Lab 07: Config and Secret Management

Main concept:

    safe configuration handling

Tools:

    environment variables
    Kubernetes ConfigMaps
    Kubernetes Secrets

Learner should understand:

    config
    secret
    avoiding hardcoded values
    cleanup

### Lab 08: CI/CD Simulation with Local Kubernetes

Main concept:

    build, test, deploy, verify workflow

Tools:

    GitHub Actions or local simulation
    Docker
    Kubernetes

Learner should understand:

    build
    test
    package
    deploy
    verify

### Lab 09: Release and Rollback Workflow

Main concept:

    restoring a previous working version

Tools:

    Kubernetes
    model versions

Learner should understand:

    release
    rollback
    failure detection
    previous working version

## Advanced Track

Goal: Develop MLOps platform engineering thinking.

### Lab 01: GitOps-style MLOps Deployment

Main concept:

    Git as desired state

Tools:

    Git
    Kubernetes
    optional Argo CD concept

Learner should understand:

    desired state
    manifests
    reconciliation
    rollback

### Lab 02: Feature Store Concepts

Main concept:

    reusable features

Tools:

    lightweight local example

Learner should understand:

    offline features
    online features
    feature reuse
    training-serving skew

### Lab 03: Multi-environment Promotion

Main concept:

    development, staging, production promotion

Tools:

    local folder or namespace simulation

Learner should understand:

    environment separation
    promotion rules
    approval gate
    rollback plan

### Lab 04: Model Governance Workflow

Main concept:

    review and approval before release

Tools:

    markdown model card
    approval checklist

Learner should understand:

    model review
    model card
    risk notes
    approval status
    audit trail

### Lab 05: Advanced Observability

Main concept:

    combined service and ML monitoring

Tools:

    Prometheus
    Grafana
    Evidently

Learner should understand:

    service metrics
    model metrics
    data quality signals
    drift signals
    alert design

### Lab 06: KServe Concept and Local Comparison

Main concept:

    advanced Kubernetes-native model serving

Tools:

    conceptual KServe overview
    optional local comparison

Learner should understand:

    why KServe exists
    how it differs from simple FastAPI serving
    when it is useful
    why it is not a beginner tool

### Lab 07: Cost-aware Cloud Extension

Main concept:

    mapping local workflow to minimal cloud resources

Tools:

    optional cloud provider

Learner should understand:

    local-to-cloud mapping
    cost estimation
    cleanup verification
    avoiding always-on services

### Lab 08: Hybrid Local and Cloud Architecture

Main concept:

    using local and cloud resources together

Tools:

    architecture design exercise

Learner should understand:

    local development
    cloud deployment target
    artifact storage options
    cost boundary
    security boundary

### Lab 09: End-to-end Capstone Platform

Main concept:

    complete MLOps workflow

Tools:

    selected tools from previous labs

Learner should understand:

    training
    tracking
    artifacts
    serving
    monitoring
    drift
    deployment
    rollback
    cleanup
    documentation

## Update Rule

README.md and ROADMAP.md should stay general and stable.

Detailed changes to lab order, tools, or learning flow should be made in this file.

This helps avoid repeated changes to the main project entry points.
