# Practitioner Track

## Goal

The Practitioner Track focuses on repeatable MLOps workflows using local and open-source tools.

This track moves beyond isolated scripts and introduces workflow structure, local services, validation, CI, and local Kubernetes.

## Who This Track Is For

This track is suitable for learners who:

- completed the Foundation Track
- understand basic experiment tracking
- can run Docker containers
- want to build repeatable ML workflows
- want to practice production-style patterns locally

## Main Learning Outcomes

By the end of this track, learners should understand:

- how to connect MLflow with local object storage
- how to structure a reproducible training pipeline
- how to serve models using Docker Compose
- how to add basic CI checks
- how to validate data before training or inference
- how to generate drift reports
- how to deploy a simple service to local Kubernetes
- how to expose basic application metrics

## Tools Introduced

- MLflow
- MinIO
- Docker Compose
- GitHub Actions
- Evidently
- kind or k3d
- kubectl
- Prometheus client libraries

## Planned Labs

### Lab 01: MLflow with MinIO Backend

Use MLflow with MinIO as an artifact store.

Key concepts:

- tracking backend
- artifact backend
- object storage
- service configuration

### Lab 02: Reproducible Training Pipeline

Organize training into a repeatable pipeline structure.

Key concepts:

- config-driven training
- input and output paths
- reproducible commands
- pipeline folders

### Lab 03: API Inference with Docker Compose

Run a model API and supporting services using Docker Compose.

Key concepts:

- multi-container setup
- service dependency
- local API workflow
- environment variables

### Lab 04: Basic CI with GitHub Actions

Add lightweight CI checks for code quality and tests.

Key concepts:

- pull request checks
- Python dependency install
- lint or formatting checks
- unit test execution

### Lab 05: Data Validation Checks

Validate input data before training or inference.

Key concepts:

- schema checks
- missing values
- type checks
- simple quality gates

### Lab 06: Evidently Data Drift Report

Generate a local data drift report using Evidently.

Key concepts:

- reference dataset
- current dataset
- drift report
- report artifacts

### Lab 07: Local Kubernetes Deployment with kind

Deploy a simple model API to a local Kubernetes cluster.

Key concepts:

- local cluster
- deployment
- service
- port forwarding
- cleanup

### Lab 08: Prometheus Metrics for Model API

Expose basic metrics from a model API.

Key concepts:

- request count
- latency
- error count
- metrics endpoint
- Prometheus scraping basics

## Cost Model

This track should run locally with no cloud cost.

Expected cost:

```text
Cloud cost: 0
Local cost: laptop CPU, memory, and disk usage only

GitHub Actions may consume free-tier CI minutes depending on account and repository settings.

Completion Criteria

A learner can move to the Professional Track after they can:

run MLflow with local object storage
structure a repeatable training workflow
use Docker Compose for local services
understand basic CI checks
generate validation and drift reports
deploy a service to local Kubernetes
clean up all local resources
