# Local-first Design

This project follows a local-first MLOps learning design.

The main goal is to help learners understand MLOps concepts without needing paid cloud infrastructure.

## Principles

### 1. Local by Default

Labs should run on a local machine whenever possible.

Preferred local tools:

- Docker
- Docker Compose
- Python virtual environments
- kind
- k3d
- kubectl
- MLflow
- MinIO
- Prometheus
- Grafana
- Evidently

Cloud services should be optional extensions, not the default learning path.

### 2. Clean and Repeatable Labs

Each lab must start from a clean or minimal state.

A lab must not assume that another lab has already created:

- Docker containers
- Docker networks
- Kubernetes clusters
- MLflow experiments
- MinIO buckets
- model artifacts
- local environment variables

Each lab must include setup and cleanup steps.

### 3. One Lab, One Main Learning Goal

Each lab should focus on one main MLOps concept.

Examples:

- experiment tracking
- model packaging
- model serving
- artifact storage
- batch inference
- monitoring
- drift detection
- local Kubernetes deployment

Avoid combining too many tools in early labs.

### 4. Cloud is Optional

The default path should avoid:

- managed Kubernetes
- cloud databases
- managed ML platforms
- always-on virtual machines
- paid monitoring services

Cloud can be introduced later as optional advanced exercises.

### 5. Open-source First

Prefer open-source tools that learners can run locally.

Examples:

- MLflow instead of managed experiment tracking
- MinIO instead of S3 or Azure Blob by default
- kind or k3d instead of managed Kubernetes by default
- Prometheus and Grafana instead of paid observability platforms
- Evidently for local drift reports

### 6. English and Sinhala Guides

Each important lab should include:

- English guide
- Sinhala guide

The Sinhala guide should explain concepts clearly, not only translate commands.

## Recommended Local Architecture

```text
Developer Laptop
│
├── Git repository
│
├── Python virtual environment
│   ├── training scripts
│   ├── inference scripts
│   └── test scripts
│
├── Docker / Docker Compose
│   ├── MLflow
│   ├── MinIO
│   ├── FastAPI services
│   ├── Prometheus
│   ├── Grafana
│   └── Evidently reports
│
└── Optional local Kubernetes
    ├── kind
    ├── k3d
    └── kubectl
Lab Design Pattern

Every lab should follow this pattern:

1. Start from clean state
2. Check prerequisites
3. Create only required resources
4. Run the MLOps workflow
5. Verify the result
6. Explain what happened
7. Clean up all created resources
What Should Not Happen

Labs should not require hidden previous state.

Avoid instructions like:

Use the MLflow server from the previous lab
Use the Kubernetes cluster created earlier
Use the MinIO bucket from Lab 02

Instead, each lab should either:

create what it needs, or
clearly mark a dependency as optional.
Why Local-first Matters

Local-first learning helps learners:

practice more often
avoid cloud billing mistakes
understand the underlying tools
repeat labs many times
debug safely
build confidence before using cloud platforms
Future Cloud Extensions

Cloud extensions may be added after the local version is understood.

Examples:

push Docker image to a cloud registry
deploy the same API to managed Kubernetes
store artifacts in cloud object storage
compare local MinIO with cloud storage
estimate cloud cost for a production-like setup

Cloud extensions should always include cost notes and cleanup instructions.
