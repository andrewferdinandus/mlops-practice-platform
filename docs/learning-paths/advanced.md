# Advanced Track

## Goal

The Advanced Track explores platform engineering, governance, GitOps, feature management, hybrid architecture, and capstone-level MLOps workflows.

This track is for learners who want to move from using MLOps tools to designing MLOps platforms.

## Who This Track Is For

This track is suitable for learners who:

- completed the Professional Track
- understand local Kubernetes workflows
- understand model tracking, serving, monitoring, and cleanup
- want to design end-to-end MLOps platforms
- want to compare local and cloud architecture safely

## Main Learning Outcomes

By the end of this track, learners should understand:

- how GitOps-style deployment applies to MLOps
- where feature stores fit in ML systems
- how to promote models across environments
- how governance affects model release workflows
- how to design hybrid local and cloud workflows
- how to reason about cost before using cloud
- how to build an end-to-end capstone MLOps platform

## Tools and Concepts Introduced

- GitOps concepts
- feature store concepts
- model governance
- environment promotion
- policy checks
- advanced monitoring
- cost estimation
- hybrid local/cloud mapping
- capstone architecture

## Planned Labs

### Lab 01: GitOps-style MLOps Deployment

Practice a GitOps-style deployment workflow using local Kubernetes.

Key concepts:

- Git as desired state
- deployment manifests
- change review
- reconciliation concept
- rollback

### Lab 02: Feature Store Introduction

Introduce feature store concepts using a lightweight local example.

Key concepts:

- offline features
- online features
- feature reuse
- feature consistency
- training-serving skew

### Lab 03: Multi-environment Promotion

Simulate promotion across development, staging, and production-like local environments.

Key concepts:

- environment separation
- promotion rules
- versioned artifacts
- approval gates
- rollback planning

### Lab 04: Model Governance Workflow

Design a lightweight model governance workflow.

Key concepts:

- model review
- approval status
- audit trail
- model card basics
- risk notes

### Lab 05: Cost-aware Cloud Extension

Extend one local workflow to a minimal cloud environment with cost controls.

Key concepts:

- local-to-cloud mapping
- resource minimums
- cost estimation
- cleanup verification
- avoiding always-on services

### Lab 06: Hybrid Local and Cloud Architecture

Design a hybrid learning architecture that keeps development local and uses cloud only where useful.

Key concepts:

- local development
- cloud artifact storage
- cloud deployment target
- cost boundaries
- security boundaries

### Lab 07: Advanced Observability

Explore advanced observability patterns for ML systems.

Key concepts:

- service metrics
- model metrics
- data quality signals
- drift signals
- alert design
- dashboard design

### Lab 08: End-to-end Capstone Platform

Build a capstone MLOps workflow using the main concepts from all tracks.

Key concepts:

- training
- tracking
- artifact storage
- serving
- monitoring
- drift reporting
- deployment
- cleanup
- documentation

## Cost Model

This track remains local-first by default.

Expected cost:

```text
Cloud cost: 0 by default
Cloud cost may apply only in optional cloud extension labs

Any cloud lab must include:

estimated cost
exact resources created
cleanup commands
verification commands
warning about long-running resources
Completion Criteria

A learner completes this track after they can:

design a local-first MLOps platform
explain local-to-cloud tradeoffs
define a model promotion workflow
reason about governance and monitoring
estimate cost before creating cloud resources
build and clean up an end-to-end MLOps practice environment
