# Low-cost MLOps Practice Platform

A hands-on, local-first learning platform for understanding MLOps step by step.

This repository helps you learn practical MLOps concepts using low-cost, open-source tools that can run mostly on your local machine.

## Start Here

New to MLOps? Start with the beginner notes before running labs.

### English Notes

- [Why MLOps Exists](docs/mlops-notes/01-why-mlops-exists.md)
- [MLOps Core Concepts](docs/mlops-notes/02-mlops-core-concepts.md)
- [MLOps Tool Map](docs/mlops-notes/03-mlops-tool-map.md)

### Sinhala Notes

- [MLOps අවශ්‍ය වෙන්නේ ඇයි?](docs/mlops-notes/01-why-mlops-exists-si.md)
- [MLOps Core Concepts - සිංහල](docs/mlops-notes/02-mlops-core-concepts-si.md)
- [MLOps Tool Map - සිංහල](docs/mlops-notes/03-mlops-tool-map-si.md)

## What You Will Learn

This platform helps you practice how machine learning models move from notebooks to real-world systems.

You will learn concepts such as:

    experiment tracking
    model artifacts
    reproducible training
    Dockerized ML workflows
    model serving with APIs
    local object storage
    data validation
    drift detection
    monitoring
    local Kubernetes deployment
    CI/CD basics
    model release and rollback concepts

## Why Local-first?

MLOps can become expensive and complicated when cloud services are introduced too early.

Local-first learning helps you:

    practice without cloud cost
    repeat labs safely
    understand each tool clearly
    avoid accidental cloud billing
    build confidence before using cloud platforms

Cloud-based labs may be added as optional advanced extensions, but the main learning path should work locally.

## Core Tools

The learning path uses practical open-source tools such as:

    Python
    Docker
    Docker Compose
    kind or k3d
    Kubernetes
    MLflow
    MinIO
    FastAPI
    Prometheus
    Grafana
    Evidently
    GitHub Actions

## Learning Tracks

The platform is organized into four learning tracks.

### 1. Foundation

Learn the basic building blocks of MLOps.

Topics include:

    MLflow experiment tracking
    model artifacts
    Dockerized training
    FastAPI model serving
    local object storage
    batch inference

### 2. Practitioner

Build repeatable local MLOps workflows.

Topics include:

    MLflow with MinIO
    reproducible training pipelines
    Docker Compose workflows
    data validation
    Evidently drift reports
    local Kubernetes with kind or k3d
    basic model API metrics

### 3. Professional

Practice production-like MLOps patterns locally.

Topics include:

    MLflow with MinIO and PostgreSQL
    Kubernetes model service deployment
    Prometheus and Grafana monitoring
    model registry workflow
    canary-style deployment concepts
    configuration and secret management
    CI/CD simulation

### 4. Advanced

Explore platform engineering and advanced MLOps concepts.

Topics include:

    GitOps-style deployment
    feature store concepts
    multi-environment promotion
    model governance
    cost-aware cloud extensions
    hybrid local and cloud architecture
    end-to-end capstone platform

See [ROADMAP.md](ROADMAP.md) for the full roadmap.

## Repository Layout

    docs/
      mlops-notes/       Beginner-friendly MLOps explanations
      architecture/       Local-first and cost-aware architecture docs
      learning-paths/     Learning track descriptions

    labs/
      shared/             Shared setup, cleanup, and troubleshooting guides
      foundation/         Foundation-level labs
      practitioner/       Practitioner-level labs
      professional/       Professional-level labs
      advanced/           Advanced-level labs

    platform/             Reusable local platform templates

    scripts/              Helper scripts

    examples/             Small examples used by guides or labs

## Lab Design Principles

Each lab should be easy to run, understand, and clean up.

A lab should:

    explain the concept before using the tool
    start from a clean or minimal state
    create only the resources it needs
    avoid depending on previous lab leftovers
    include verification steps
    include cleanup steps
    include cost notes
    provide English and Sinhala guides where applicable

## Cost Philosophy

The main learning path is designed for local practice.

Expected default cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, and disk usage only

Cloud resources should be optional and clearly explained with cleanup steps.

## Getting Started

Clone the repository:

    git clone https://github.com/<your-username>/mlops-practice-platform.git
    cd mlops-practice-platform

Read the beginner notes first:

    docs/mlops-notes/01-why-mlops-exists.md
    docs/mlops-notes/01-why-mlops-exists-si.md

Then review the shared setup guides:

    labs/shared/setup-en.md
    labs/shared/setup-si.md

## Current Focus

The first hands-on lab will introduce local MLflow experiment tracking.

Before starting labs, review the MLOps notes and make sure the required local tools are installed.
