# Shared Troubleshooting Guide

This guide explains common problems you may see while running local MLOps labs.

Most issues are related to missing tools, Docker not running, port conflicts, or leftover resources from previous labs.

## 1. Command Not Found

Example:

    docker: command not found
    python3: command not found
    kubectl: command not found

This means the tool is not installed or it is not available in your terminal PATH.

Check the tool:

    docker --version
    python3 --version
    kubectl version --client

If the command still fails, install the missing tool and open a new terminal.

## 2. Docker Is Not Running

Example error:

    Cannot connect to the Docker daemon

This usually means Docker Desktop or the Docker service is not running.

Try:

    open Docker Desktop

Or on Linux:

    sudo systemctl start docker

Then check:

    docker ps

If Docker is working, the command should show a container list.

## 3. Docker Permission Error on Linux

Example error:

    permission denied while trying to connect to the Docker daemon socket

On Linux, your user may not have permission to use Docker.

Temporary option:

    sudo docker ps

Better option:

    sudo usermod -aG docker $USER

Then log out and log back in.

After that, check:

    docker ps

## 4. Docker Compose Command Not Working

Try:

    docker compose version

If that fails, your Docker installation may not include Docker Compose v2.

Some older systems use:

    docker-compose version

Labs should prefer:

    docker compose

## 5. Port Already in Use

Example:

    bind: address already in use

This means another process is already using the required port.

Common ports:

    5000  MLflow
    8000  FastAPI
    9000  MinIO API
    9001  MinIO Console
    9090  Prometheus
    3000  Grafana

Check a port on macOS or Linux:

    lsof -i :5000

Stop the service using the port, or change the lab port if the lab allows it.

## 6. Container Keeps Restarting

Check running containers:

    docker ps

Check all containers:

    docker ps -a

View logs:

    docker logs <container-name>

For Docker Compose labs:

    docker compose logs

Logs usually show the real error.

Common causes:

    wrong environment variable
    missing file
    port conflict
    invalid command
    service dependency not ready

## 7. Python Package Install Fails

Example:

    pip install -r requirements.txt

If install fails, check:

    python3 --version
    pip --version

Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Upgrade pip:

    python -m pip install --upgrade pip

Then try again:

    pip install -r requirements.txt

## 8. Wrong Python Environment

Sometimes packages are installed in one Python environment, but the script runs with another environment.

Check Python location:

    which python
    which python3

Check installed packages:

    pip list

If using a virtual environment, make sure it is activated:

    source .venv/bin/activate

## 9. File or Folder Not Found

Example:

    No such file or directory

Check your current folder:

    pwd

List files:

    ls -la

Most commands should be run from the repository root unless the lab says otherwise.

Example:

    cd ~/mlops-practice-platform

## 10. MLflow UI Not Opening

If MLflow is expected at:

    http://localhost:5000

Check whether the service is running:

    docker ps

Check logs:

    docker compose logs

Check the port:

    lsof -i :5000

If another service uses port 5000, stop it or change the lab port.

## 11. MinIO Console Not Opening

MinIO commonly uses:

    http://localhost:9001

Check containers:

    docker ps

Check logs:

    docker compose logs

Common causes:

    container not running
    port conflict
    wrong username or password
    service still starting

## 12. Kubernetes Cluster Not Found

Check kind clusters:

    kind get clusters

Check k3d clusters:

    k3d cluster list

Check kubectl context:

    kubectl config current-context

If the lab created a cluster, make sure the cluster creation step completed successfully.

## 13. kubectl Cannot Connect

Example:

    The connection to the server localhost:8080 was refused

This usually means kubectl is not connected to a valid cluster.

Check contexts:

    kubectl config get-contexts

Check current context:

    kubectl config current-context

If using kind or k3d, recreate or select the correct cluster.

## 14. Disk Space Issues

Docker images, volumes, and artifacts can use disk space.

Check Docker disk usage:

    docker system df

List volumes:

    docker volume ls

Use cleanup commands from the lab guide before removing global Docker resources.

Be careful with:

    docker system prune
    docker volume prune

These can affect other projects.

## 15. General Debugging Flow

When something fails:

    1. Read the error message
    2. Check your current folder with pwd
    3. Check required tools with --version
    4. Check running containers with docker ps
    5. Check logs with docker compose logs
    6. Check ports with lsof
    7. Run the lab cleanup steps
    8. Try again from a clean state

## Final Tip

Most local lab issues are fixable by checking:

    current folder
    installed tools
    running containers
    logs
    ports
    leftover resources

Start simple and debug one issue at a time.
