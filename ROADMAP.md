# Roadmap

This roadmap shows the recommended learning journey for the Low-cost MLOps Practice Platform.

Start with the beginner MLOps notes, then move through the tracks step by step.

## Recommended Order

    MLOps Notes
        |
        v
    Foundation Track
        |
        v
    Practitioner Track
        |
        v
    Professional Track
        |
        v
    Advanced Track

## Before Starting Labs

New learners should read these notes first:

    docs/mlops-notes/01-why-mlops-exists.md
    docs/mlops-notes/02-mlops-core-concepts.md
    docs/mlops-notes/03-mlops-tool-map.md

Sinhala notes are also available:

    docs/mlops-notes/01-why-mlops-exists-si.md
    docs/mlops-notes/02-mlops-core-concepts-si.md
    docs/mlops-notes/03-mlops-tool-map-si.md

These notes explain why MLOps exists, the core concepts, and how common tools fit into the workflow.

## Foundation Track

The Foundation Track introduces the basic building blocks of MLOps.

You will learn how to track experiments, save model artifacts, package training code, serve a model, and run simple inference workflows locally.

Recommended labs:

    1. Local MLflow Experiment Tracking
    2. Dockerized ML Training
    3. FastAPI Model Serving
    4. Local Model Artifact Management
    5. MinIO as Local Object Storage
    6. Basic Batch Inference

Main tools:

    Python
    scikit-learn
    MLflow
    Docker
    Docker Compose
    FastAPI
    MinIO

Expected cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, and disk usage only

## Practitioner Track

The Practitioner Track focuses on repeatable local MLOps workflows.

You will learn how to connect tools together, structure repeatable pipelines, validate data, check drift, deploy to local Kubernetes, and expose basic service metrics.

Recommended labs:

    1. MLflow with MinIO Backend
    2. Reproducible Training Pipeline
    3. API Inference with Docker Compose
    4. Basic CI with GitHub Actions
    5. Data Validation Checks
    6. Evidently Data Drift Report
    7. Local Kubernetes Deployment with kind
    8. Prometheus Metrics for Model API

Main tools:

    MLflow
    MinIO
    Docker Compose
    GitHub Actions
    Evidently
    kind or k3d
    kubectl
    Prometheus client libraries

Expected cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, and disk usage only

GitHub Actions may use free-tier CI minutes depending on your repository and account settings.

## Professional Track

The Professional Track introduces production-like MLOps patterns while still keeping the default environment local-first.

You will practice multi-service MLOps stacks, local Kubernetes deployments, monitoring dashboards, model registry workflows, configuration management, and deployment patterns.

Recommended labs:

    1. MLflow + MinIO + PostgreSQL Stack
    2. FastAPI Model Service on Kubernetes
    3. Prometheus and Grafana Monitoring
    4. Model Drift Monitoring Workflow
    5. Canary Deployment Practice
    6. Config and Secret Management
    7. Model Registry Workflow
    8. CI/CD Simulation with Local Kubernetes

Main tools:

    MLflow
    MinIO
    PostgreSQL
    FastAPI
    Docker Compose
    Kubernetes
    kind or k3d
    Prometheus
    Grafana
    Evidently
    GitHub Actions

Expected cost:

    Cloud cost: 0 by default
    Local cost: higher CPU, memory, and disk usage than earlier tracks

## Advanced Track

The Advanced Track explores platform engineering and advanced MLOps concepts.

You will learn about GitOps-style deployment, feature store concepts, environment promotion, governance, observability, cost-aware cloud extensions, and end-to-end platform design.

Recommended labs:

    1. GitOps-style MLOps Deployment
    2. Feature Store Introduction
    3. Multi-environment Promotion
    4. Model Governance Workflow
    5. Cost-aware Cloud Extension
    6. Hybrid Local and Cloud Architecture
    7. Advanced Observability
    8. End-to-end Capstone Platform

Main concepts:

    GitOps
    feature stores
    model governance
    environment promotion
    policy checks
    advanced observability
    cloud cost estimation
    hybrid local/cloud architecture

Expected cost:

    Cloud cost: 0 by default
    Cloud cost may apply only for optional cloud extension labs

Any cloud extension should clearly explain the estimated cost, created resources, cleanup commands, and verification steps.

## Learning Advice

Do not try to learn every MLOps tool at once.

Start with the problem first:

    Why do experiments need tracking?
    Why do model artifacts need to be organized?
    Why should training be reproducible?
    Why does a model need serving?
    Why does production data need monitoring?
    Why is rollback important?

Then learn the tool that helps solve that problem.

## Cleanup Rule

Every lab should include cleanup instructions.

Before moving to another lab, clean up the resources created by the current lab.

This keeps your local environment simple and avoids unnecessary resource usage.
