# Foundation Track

## Goal

The Foundation Track introduces the basic building blocks of MLOps using local-first tools.

This track is for learners who want to understand the core workflow before moving into production-like systems.

## Who This Track Is For

This track is suitable for learners who:

- know basic Python
- have basic machine learning knowledge
- are new to MLOps
- want hands-on practice without cloud cost
- want to understand tools before using managed platforms

## Main Learning Outcomes

By the end of this track, learners should understand:

- what experiment tracking is
- how to log parameters, metrics, and artifacts
- why reproducibility matters
- how Docker helps package ML workflows
- how to serve a model using an API
- how local object storage fits into MLOps
- how to run simple batch inference

## Tools Introduced

- Python
- scikit-learn
- MLflow
- Docker
- Docker Compose
- FastAPI
- MinIO

## Planned Labs

### Lab 01: Local MLflow Experiment Tracking

Learn how to train a simple model and track parameters, metrics, and artifacts using MLflow.

Key concepts:

- experiments
- runs
- parameters
- metrics
- artifacts
- local tracking server

### Lab 02: Dockerized ML Training

Package a training script inside a Docker container.

Key concepts:

- Dockerfile
- containerized training
- reproducible runtime
- dependency isolation

### Lab 03: FastAPI Model Serving

Serve a trained model using a local FastAPI application.

Key concepts:

- prediction endpoint
- request and response schema
- local API testing
- model loading

### Lab 04: Local Model Artifact Management

Store and load model artifacts from a structured local folder.

Key concepts:

- artifact versioning basics
- model file organization
- reproducible paths
- cleanup

### Lab 05: MinIO as Local Object Storage

Use MinIO as a local object storage service for model artifacts.

Key concepts:

- buckets
- object storage
- S3-compatible local storage
- artifact separation

### Lab 06: Basic Batch Inference

Run predictions on a batch dataset and save the output.

Key concepts:

- batch input
- batch output
- repeatable inference
- simple validation

## Cost Model

This track should run locally with no cloud cost.

Expected cost:

```text
Cloud cost: 0
Local cost: laptop CPU, memory, and disk usage only
Completion Criteria

A learner can move to the Practitioner Track after they can:

run a local training script
track experiments with MLflow
package a simple ML workflow with Docker
serve a model locally with FastAPI
clean up lab resources safely
