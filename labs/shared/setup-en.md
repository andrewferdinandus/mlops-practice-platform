# Shared Setup Guide

This guide helps you prepare your local machine for the MLOps labs.

The labs are designed to run locally as much as possible. You do not need a cloud account for the main learning path.

## Supported Environments

Recommended environments:

    macOS
    Linux
    WSL2 on Windows

For Windows users, WSL2 with Docker Desktop is recommended.

## Where to Run Commands

Run commands from the repository root unless a lab guide says otherwise.

Example:

    cd ~/mlops-practice-platform

## Required Tools

Most labs use these tools:

    Git
    Python 3.10 or newer
    Docker
    Docker Compose
    curl

Some labs may also use:

    make
    jq
    kubectl
    kind
    k3d
    Helm

Not every lab needs every tool. Each lab will list its own requirements.

## Check Git

Run:

    git --version

Git is used to clone the repository and track code changes.

## Check Python

Run:

    python3 --version

Python is used for training scripts, inference scripts, and small utilities.

Recommended version:

    Python 3.10 or newer

## Check Docker

Run:

    docker --version

Docker is used to run services such as MLflow, MinIO, FastAPI, Prometheus, and Grafana in containers.

## Check Docker Compose

Run:

    docker compose version

Docker Compose is used when a lab needs multiple local services running together.

Example:

    MLflow + MinIO
    FastAPI + Prometheus + Grafana

## Check curl

Run:

    curl --version

curl is useful for testing APIs from the terminal.

## Optional Kubernetes Tools

Some later labs may use local Kubernetes.

Check kubectl:

    kubectl version --client

Check kind:

    kind version

Check k3d:

    k3d version

You do not need Kubernetes for the first beginner notes or early Foundation labs.

## Recommended Local Folder

You can keep the repository in a simple local folder.

Example:

    mkdir -p ~/mlops-practice
    cd ~/mlops-practice

Clone the repository:

    git clone https://github.com/<your-username>/mlops-practice-platform.git
    cd mlops-practice-platform

## Helper Script

After the helper script is available, you can check common prerequisites with:

    ./scripts/check-prereqs.sh

The script should only check your local environment and print helpful information.

It should not create cloud resources.

## Cost Note

The main learning path is local-first.

Expected default cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, and disk usage only

## Next Step

After setup, read the beginner MLOps notes:

    docs/mlops-notes/01-why-mlops-exists.md
    docs/mlops-notes/02-mlops-core-concepts.md
    docs/mlops-notes/03-mlops-tool-map.md

Then start the first Foundation lab when it is available.
