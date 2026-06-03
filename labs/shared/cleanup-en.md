# Shared Cleanup Guide

This guide explains how cleanup works in the labs.

Cleanup is an important part of MLOps practice. It keeps your local machine clean and helps avoid unnecessary resource usage.

## Why Cleanup Matters

MLOps labs may create local resources such as:

    Docker containers
    Docker images
    Docker volumes
    Docker networks
    Python virtual environments
    temporary files
    model artifacts
    MLflow run data
    local Kubernetes clusters

If these resources are not removed, your machine can become messy over time.

Cleanup helps you:

    avoid port conflicts
    free disk space
    reduce confusion between labs
    prevent old files from affecting new labs
    keep each lab repeatable

## Clean Lab Principle

Each lab should start from a clean or minimal state.

Do not assume that resources from a previous lab still exist.

Before starting a new lab, check whether the previous lab has cleanup steps and run them if needed.

## Common Docker Cleanup Commands

Stop and remove services created by Docker Compose:

    docker compose down

Remove Docker Compose services and named volumes:

    docker compose down -v

List running containers:

    docker ps

List all containers:

    docker ps -a

List Docker volumes:

    docker volume ls

List Docker networks:

    docker network ls

## Important Warning

Be careful with global cleanup commands.

Commands such as these can remove resources used by other projects:

    docker system prune
    docker volume prune
    docker network prune

Only use global cleanup commands when you understand what they remove.

Lab guides should prefer project-specific cleanup commands.

## Common Local File Cleanup

Some labs may create local folders such as:

    mlruns
    mlartifacts
    artifacts
    outputs
    reports
    tmp

A lab may ask you to remove generated files using commands such as:

    rm -rf mlruns
    rm -rf mlartifacts
    rm -rf outputs
    rm -rf reports

Be careful with rm -rf.

Always check the path before running delete commands.

## Kubernetes Cleanup

Some later labs may create local Kubernetes clusters using kind or k3d.

Delete a kind cluster:

    kind delete cluster --name <cluster-name>

Delete a k3d cluster:

    k3d cluster delete <cluster-name>

List kind clusters:

    kind get clusters

List k3d clusters:

    k3d cluster list

## Port Conflicts

If a lab fails because a port is already in use, another service may still be running.

Common ports:

    5000  MLflow
    8000  FastAPI
    9000  MinIO API
    9001  MinIO Console
    9090  Prometheus
    3000  Grafana

On macOS or Linux, you can check a port:

    lsof -i :5000

Then stop the service that is using it.

## Recommended Cleanup Flow

After finishing a lab:

    1. Stop lab services
    2. Remove lab-specific volumes if instructed
    3. Remove generated artifacts if instructed
    4. Verify containers are stopped
    5. Confirm the next lab starts cleanly

## Cost Note

Local cleanup helps save disk space and reduce confusion.

For cloud extension labs, cleanup is even more important because running resources may create cost.

Any cloud lab should include:

    resources created
    cleanup commands
    verification commands
    cost warning

## Final Reminder

Cleanup is not optional.

A good MLOps workflow should be repeatable, understandable, and easy to reset.
