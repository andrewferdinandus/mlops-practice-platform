# Cleanup - Lab 02

This cleanup guide removes the local files and Docker image created by Lab 02.

Lab 02 does not create cloud resources or Kubernetes resources.

## Stop Running Containers

This lab runs the container with:

    --rm

That means the container is automatically removed after the training run finishes.

To check running containers:

    docker ps

To check all containers:

    docker ps -a

## Remove the Docker Image

From any folder, run:

    docker rmi mlops-lab-02-training:latest

If the image is already removed, Docker may show an error. That is okay.

## Remove Generated Output Files

From the Lab 02 folder:

    cd labs/foundation/lab-02-dockerized-ml-training

Remove generated outputs:

    rm -rf outputs
    mkdir -p outputs
    touch outputs/.gitkeep

This removes files such as:

    outputs/dockerized_metrics.json
    outputs/dockerized_predictions.csv
    outputs/runtime_environment.json
    outputs/model/dockerized_model.joblib

## Verify Cleanup

Check the outputs folder:

    ls -la outputs

Expected result:

    .gitkeep

Check Docker image:

    docker images | grep mlops-lab-02-training

Expected result:

    no output

## Cost Note

This lab runs locally using Docker.

Expected cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, Docker image storage, and disk usage

## Safety Note

This cleanup does not run global Docker prune commands.

Avoid running these unless you understand the impact:

    docker system prune
    docker volume prune

Those commands can affect other local projects.
