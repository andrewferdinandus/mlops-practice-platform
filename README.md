# Low-cost MLOps Practice Platform

A hands-on, local-first MLOps learning platform designed for maximum practical learning with minimum cost.

This repository is intentionally separate from any cloud-specific infrastructure repository. It is not part of the `terraform-azure-aks` project.

## Goals

The goal of this project is to help learners practice real-world MLOps concepts using mostly local and open-source tools.

The platform focuses on:

- Local-first MLOps learning
- Low-cost experimentation
- Clean, repeatable labs
- Docker-based local environments
- Optional Kubernetes using kind or k3d
- Optional cloud extensions only after local understanding
- English and Sinhala learning guides

## Core Tools

The platform will use tools such as:

- Docker
- Docker Compose
- kind or k3d
- Kubernetes
- MLflow
- MinIO
- FastAPI
- Prometheus
- Grafana
- Evidently
- GitHub Actions

## Important Design Rules

Each lab must:

- Start from a clean or minimal state
- Create only the resources it needs
- Avoid depending on leftovers from previous labs
- Include a full cleanup section
- Be possible to run locally where practical
- Include English and Sinhala guides
- Keep cloud usage optional

## Repository Layout

```text
labs/        Hands-on MLOps labs
labs/shared Shared setup and cleanup guides
docs/        Architecture and learning path documentation
platform/    Reusable local infrastructure templates
scripts/     Utility scripts
examples/    Small reusable examples
Learning Tracks

The platform is organized into four tracks:

Foundation
Practitioner
Professional
Advanced

See ROADMAP.md for the full roadmap.

Cost Philosophy

The default learning path should cost nothing except the learner's local machine resources.

Cloud services may be added later as optional extensions, but the primary path should work locally.

Getting Started
git clone https://github.com/<your-username>/mlops-practice-platform.git
cd mlops-practice-platform

Then read:

labs/shared/setup-en.md
labs/shared/setup-si.md
labs/README.md
Current Status

This project is in the initial structure and roadmap phase.

The first planned lab is:

Foundation Lab 01: Local MLflow Experiment Tracking

