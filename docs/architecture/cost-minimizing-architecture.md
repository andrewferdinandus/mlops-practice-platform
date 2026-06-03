# Cost-minimizing Architecture

This document explains how the project minimizes cost while still teaching practical MLOps skills.

## Cost Philosophy

The default learning path should cost nothing except local machine resources.

Learners should be able to practice the core platform using:

- their laptop or local workstation
- open-source software
- Docker
- local Kubernetes
- local object storage
- local monitoring tools

Cloud services are optional and should not be required for the main learning path.

## Default Architecture

```text
Local Machine
│
├── Git
│   └── source control and documentation
│
├── Python
│   └── training, inference, and testing
│
├── Docker Compose
│   ├── MLflow tracking server
│   ├── MinIO object storage
│   ├── FastAPI model service
│   ├── Prometheus
│   ├── Grafana
│   └── Evidently report generation
│
└── Optional Local Kubernetes
    ├── kind
    └── k3d
Tool Choices
Experiment Tracking

Default:

MLflow running locally

Why:

open source
easy to run locally
teaches parameters, metrics, artifacts, and model comparison
can later be extended with MinIO and PostgreSQL

Avoid by default:

managed ML experiment tracking services
Object Storage

Default:

MinIO running locally

Why:

S3-compatible API
runs locally
helps learners understand object storage concepts
avoids cloud storage cost

Avoid by default:

AWS S3
Azure Blob Storage
Google Cloud Storage

These may be used only in optional cloud extensions.

Compute

Default:

local Python
Docker
Docker Compose

Optional:

kind
k3d

Avoid by default:

cloud virtual machines
managed Kubernetes clusters
GPU instances
Model Serving

Default:

FastAPI running locally or in Docker

Why:

simple
practical
production-relevant
easy to containerize
Monitoring

Default:

Prometheus
Grafana
local application metrics

Why:

open source
production-relevant
works locally
teaches metrics-based thinking
Drift and Data Quality

Default:

Evidently

Why:

works locally
useful for reports
easy to connect to batch workflows
Cost Risk Areas

The project should avoid accidental cost from:

always-running cloud services
managed Kubernetes clusters
managed databases
large storage buckets
GPU workloads
paid observability tools
repeated CI jobs with high usage
public cloud load balancers
Required Cost Controls

Every lab that uses cloud resources must include:

estimated cost note
resource list
cleanup instructions
verification that resources were deleted
warning about long-running resources
Local Resource Controls

Even local labs should avoid wasting resources.

Labs should clean up:

Docker containers
Docker volumes
Docker networks
Kubernetes clusters
temporary files
generated artifacts
local logs
Cleanup-first Mindset

Every lab should include cleanup commands.

Examples:

docker compose down -v
docker container prune
docker network prune
kind delete cluster --name <cluster-name>
k3d cluster delete <cluster-name>
rm -rf mlruns
rm -rf artifacts/*

Cleanup commands should be specific to the lab.

Avoid dangerous commands unless clearly explained.

Cloud Extension Pattern

When cloud is introduced, it should follow this pattern:

1. Complete the workflow locally
2. Explain which local component maps to which cloud service
3. Create the minimum required cloud resources
4. Run the workflow
5. Compare local vs cloud
6. Clean up cloud resources
7. Verify no billable resources remain
Example Local-to-Cloud Mapping
Local MLflow              -> managed tracking or self-hosted cloud MLflow
Local MinIO               -> S3 / Azure Blob / GCS
Local Docker              -> container registry + cloud runtime
Local kind/k3d            -> managed Kubernetes
Local Prometheus/Grafana  -> managed monitoring or self-hosted stack
Recommended Learning Progression
Local script
    ↓
Local experiment tracking
    ↓
Dockerized training
    ↓
Local artifact storage
    ↓
FastAPI model serving
    ↓
Docker Compose workflow
    ↓
Local Kubernetes
    ↓
Monitoring and drift detection
    ↓
Optional cloud comparison
Final Rule

The learner should never need a paid cloud account to complete the core learning path.
