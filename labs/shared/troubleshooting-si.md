# පොදු Troubleshooting Guide

මෙම guide එකෙන් local MLOps labs run කරනකොට එන්න පුළුවන් common problems explain කරයි.

බොහෝ issues එන්නේ missing tools, Docker run නොවීම, port conflicts, හෝ previous lab එකකින් ඉතිරි වූ resources නිසා.

## 1. Command Not Found

Example:

    docker: command not found
    python3: command not found
    kubectl: command not found

මෙයින් අදහස් වෙන්නේ tool එක install කරලා නැතිවීම හෝ terminal PATH එකේ නොතිබීම.

Tool එක check කරන්න:

    docker --version
    python3 --version
    kubectl version --client

Command එක තවම fail වෙනවා නම් missing tool එක install කරලා new terminal එකක් open කරන්න.

## 2. Docker Run වෙන්නේ නැහැ

Example error:

    Cannot connect to the Docker daemon

මෙය සාමාන්‍යයෙන් Docker Desktop හෝ Docker service එක run නොවීම නිසා එන error එකක්.

macOS වල Docker Desktop open කරන්න.

Linux වල:

    sudo systemctl start docker

ඊට පස්සේ check කරන්න:

    docker ps

Docker හරියට වැඩ කරනවා නම් container list එකක් පෙන්වයි.

## 3. Linux වල Docker Permission Error

Example error:

    permission denied while trying to connect to the Docker daemon socket

Linux වලදී userට Docker use කරන්න permission නැතිවිය හැක.

Temporary option:

    sudo docker ps

Better option:

    sudo usermod -aG docker $USER

ඊට පස්සේ log out වෙලා log back in වෙන්න.

Check කරන්න:

    docker ps

## 4. Docker Compose Command එක වැඩ කරන්නේ නැහැ

Run කරන්න:

    docker compose version

ඒක fail වෙනවා නම් Docker installation එකේ Docker Compose v2 නැතිවිය හැක.

Older systems වල මෙහෙම තිබිය හැක:

    docker-compose version

Labs වලදී preferred command එක:

    docker compose

## 5. Port Already in Use

Example:

    bind: address already in use

මෙයින් අදහස් වෙන්නේ required port එක වෙන process එකක් භාවිතා කරන බවයි.

Common ports:

    5000  MLflow
    8000  FastAPI
    9000  MinIO API
    9001  MinIO Console
    9090  Prometheus
    3000  Grafana

macOS හෝ Linux වල port එකක් check කරන්න:

    lsof -i :5000

ඒ port එක use කරන service එක stop කරන්න, නැත්නම් lab එක allow කරනවා නම් port එක change කරන්න.

## 6. Container එක Restart වෙමින් තියෙනවා

Running containers බලන්න:

    docker ps

All containers බලන්න:

    docker ps -a

Logs බලන්න:

    docker logs <container-name>

Docker Compose labs සඳහා:

    docker compose logs

Logs වල බොහෝ විට real error එක පෙන්වනවා.

Common causes:

    wrong environment variable
    missing file
    port conflict
    invalid command
    service dependency not ready

## 7. Python Package Install Fail වෙනවා

Example:

    pip install -r requirements.txt

Install fail වෙනවා නම් check කරන්න:

    python3 --version
    pip --version

Virtual environment එකක් create කර activate කරන්න:

    python3 -m venv .venv
    source .venv/bin/activate

pip upgrade කරන්න:

    python -m pip install --upgrade pip

ඊට පස්සේ නැවත install කරන්න:

    pip install -r requirements.txt

## 8. Wrong Python Environment

සමහර වෙලාවට packages එක Python environment එකකට install වෙලා, script එක වෙන environment එකකින් run වෙනවා.

Python location check කරන්න:

    which python
    which python3

Installed packages බලන්න:

    pip list

Virtual environment එකක් use කරනවා නම් activate වෙලාද බලන්න:

    source .venv/bin/activate

## 9. File or Folder Not Found

Example:

    No such file or directory

Current folder එක check කරන්න:

    pwd

Files list කරන්න:

    ls -la

Lab guide එක වෙනස් විදිහට කියන්නේ නැත්නම් commands repository root එකෙන් run කරන්න.

Example:

    cd ~/mlops-practice-platform

## 10. MLflow UI Open වෙන්නේ නැහැ

MLflow expected URL එක:

    http://localhost:5000

Service එක run වෙනවාද බලන්න:

    docker ps

Logs බලන්න:

    docker compose logs

Port එක check කරන්න:

    lsof -i :5000

Port 5000 වෙන service එකක් use කරනවා නම් ඒ service එක stop කරන්න හෝ lab port එක change කරන්න.

## 11. MinIO Console Open වෙන්නේ නැහැ

MinIO console සාමාන්‍යයෙන් use කරන URL එක:

    http://localhost:9001

Containers check කරන්න:

    docker ps

Logs බලන්න:

    docker compose logs

Common causes:

    container not running
    port conflict
    wrong username or password
    service still starting

## 12. Kubernetes Cluster Not Found

kind clusters check කරන්න:

    kind get clusters

k3d clusters check කරන්න:

    k3d cluster list

kubectl context check කරන්න:

    kubectl config current-context

Lab එක cluster එකක් create කරනවා නම් cluster creation step එක successfully complete වෙලාද බලන්න.

## 13. kubectl Connect වෙන්නේ නැහැ

Example:

    The connection to the server localhost:8080 was refused

මෙය සාමාන්‍යයෙන් kubectl valid cluster එකකට connect වී නැති නිසා එන error එකක්.

Contexts බලන්න:

    kubectl config get-contexts

Current context බලන්න:

    kubectl config current-context

kind හෝ k3d use කරනවා නම් correct cluster එක recreate කරන්න හෝ select කරන්න.

## 14. Disk Space Issues

Docker images, volumes, artifacts disk space use කරන්න පුළුවන්.

Docker disk usage check කරන්න:

    docker system df

Volumes list කරන්න:

    docker volume ls

Global Docker cleanup commands use කරන්න කලින් lab cleanup commands use කරන්න.

Carefulව use කරන්න:

    docker system prune
    docker volume prune

මේ commands වෙන projects වල resources වලට බලපාන්න පුළුවන්.

## 15. General Debugging Flow

දෙයක් fail උනාම:

    1. Error message එක කියවන්න
    2. pwd command එකෙන් current folder එක check කරන්න
    3. --version commands වලින් tools check කරන්න
    4. docker ps වලින් running containers බලන්න
    5. docker compose logs වලින් logs බලන්න
    6. lsof වලින් ports check කරන්න
    7. lab cleanup steps run කරන්න
    8. clean state එකකින් නැවත try කරන්න

## Final Tip

බොහෝ local lab issues fix කරන්න පුළුවන් පහත දේවල් check කිරීමෙන්:

    current folder
    installed tools
    running containers
    logs
    ports
    leftover resources

එකවර ගොඩක් දේවල් change නොකර, එක issue එකක් එකවර debug කරන්න.
