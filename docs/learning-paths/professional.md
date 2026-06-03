# Professional Track

## Goal

The Professional Track focuses on production-like MLOps workflows while still keeping the default environment local-first and low-cost.

This track introduces more realistic service composition, model registry workflows, monitoring, deployment patterns, and configuration management.

## Who This Track Is For

This track is suitable for learners who:

- completed the Practitioner Track
- understand Docker Compose and local Kubernetes
- have used MLflow, MinIO, and FastAPI
- want production-like MLOps practice
- want to understand platform-level tradeoffs before using cloud

## Main Learning Outcomes

By the end of this track, learners should understand:

- how MLflow can use MinIO and PostgreSQL together
- how to deploy model services to local Kubernetes
- how to monitor services with Prometheus and Grafana
- how to create a basic model registry workflow
- how to practice canary-style deployment locally
- how to manage configuration and secrets safely
- how to simulate CI/CD workflows locally
- how production MLOps components fit together

## Tools Introduced

- MLflow
- MinIO
- PostgreSQL
- FastAPI
- Docker Compose
- Kubernetes
- kind or k3d
- Prometheus
- Grafana
- Evidently
- kubectl
- GitHub Actions

## Planned Labs

### Lab 01: MLflow + MinIO + PostgreSQL Stack

Run a more production-like MLflow setup locally.

Key concepts:

- backend store
- artifact store
- PostgreSQL metadata
- MinIO artifact storage
- service composition

### Lab 02: FastAPI Model Service on Kubernetes

Deploy a containerized model API to local Kubernetes.

Key concepts:

- Kubernetes deployment
- service exposure
- container image loading
- port forwarding
- health checks

### Lab 03: Prometheus and Grafana Monitoring

Monitor a model service using Prometheus and Grafana.

Key concepts:

- metrics scraping
- dashboards
- service health
- latency and request metrics

### Lab 04: Model Drift Monitoring Workflow

Create a local workflow for model or data drift reporting.

Key concepts:

- reference data
- current data
- scheduled-style checks
- drift artifact generation
- report review

### Lab 05: Canary Deployment Practice

Practice a canary-style deployment locally.

Key concepts:

- stable version
- candidate version
- traffic split concept
- rollback thinking
- deployment comparison

### Lab 06: Config and Secret Management

Manage configuration and secrets in a safer way.

Key concepts:

- environment variables
- config files
- Kubernetes secrets
- secret cleanup
- avoiding hardcoded credentials

### Lab 07: Model Registry Workflow

Practice a simple model registry lifecycle.

Key concepts:

- candidate model
- approved model
- promoted model
- model versioning
- rollback

### Lab 08: CI/CD Simulation with Local Kubernetes

Simulate a CI/CD-style deployment flow using local tools.

Key concepts:

- build
- test
- package
- deploy
- verify
- cleanup

## Cost Model

This track should still be local-first.

Expected cost:

```text
Cloud cost: 0 by default
Local cost: higher laptop CPU, memory, and disk usage than previous tracks

Some labs may require more memory because multiple services run together.

Completion Criteria

A learner can move to the Advanced Track after they can:

run a multi-service local MLOps stack
deploy and monitor a model service locally
explain model registry workflow basics
practice deployment and rollback concepts
manage configs and secrets safely
clean up Docker and Kubernetes resources confidently
