# පොදු Setup Guide

මෙම guide එකෙන් MLOps labs run කරන්න local machine එක prepare කරගන්න ආකාරය explain කරයි.

Main learning path එක local-first නිසා cloud account එකක් අවශ්‍ය නැහැ.

## Supported Environments

Recommended environments:

    macOS
    Linux
    WSL2 on Windows

Windows users සඳහා WSL2 + Docker Desktop recommended.

## Commands Run කරන තැන

Lab guide එක වෙනස් විදිහට කියන්නේ නැත්නම් commands run කරන්න repository root එකේ.

Example:

    cd ~/mlops-practice-platform

## අවශ්‍ය Tools

බොහෝ labs සඳහා පහත tools භාවිතා වෙනවා:

    Git
    Python 3.10 or newer
    Docker
    Docker Compose
    curl

සමහර later labs සඳහා පහත tools අවශ්‍ය විය හැක:

    make
    jq
    kubectl
    kind
    k3d
    Helm

හැම lab එකකටම හැම tool එකම අවශ්‍ය නැහැ. එක් එක් lab එකේ requirements වෙනම සඳහන් කරනවා.

## Git Check කිරීම

Run කරන්න:

    git --version

Git භාවිතා කරන්නේ repository clone කරන්න සහ code changes track කරන්න.

## Python Check කිරීම

Run කරන්න:

    python3 --version

Python භාවිතා කරන්නේ training scripts, inference scripts, සහ small utilities සඳහා.

Recommended version:

    Python 3.10 or newer

## Docker Check කිරීම

Run කරන්න:

    docker --version

Docker භාවිතා කරන්නේ MLflow, MinIO, FastAPI, Prometheus, Grafana වගේ services containers විදිහට run කරන්න.

## Docker Compose Check කිරීම

Run කරන්න:

    docker compose version

Docker Compose භාවිතා කරන්නේ services කිහිපයක් එකට localව run කරන්න.

Examples:

    MLflow + MinIO
    FastAPI + Prometheus + Grafana

## curl Check කිරීම

Run කරන්න:

    curl --version

curl භාවිතා කරන්නේ terminal එකෙන් APIs test කරන්න.

## Optional Kubernetes Tools

Later labs වලදී local Kubernetes use කරන්න පුළුවන්.

kubectl check කරන්න:

    kubectl version --client

kind check කරන්න:

    kind version

k3d check කරන්න:

    k3d version

Beginner notes සහ early Foundation labs සඳහා Kubernetes අවශ්‍ය නැහැ.

## Recommended Local Folder

Repository එක simple local folder එකක තියාගන්න පුළුවන්.

Example:

    mkdir -p ~/mlops-practice
    cd ~/mlops-practice

Repository clone කරන්න:

    git clone https://github.com/<your-username>/mlops-practice-platform.git
    cd mlops-practice-platform

## Helper Script

Helper script එක available උනාම common prerequisites check කරන්න:

    ./scripts/check-prereqs.sh

මෙම script එක local environment එක check කරලා helpful information print කරන්නයි.

Cloud resources create නොකළ යුතුයි.

## Cost Note

Main learning path එක local-first.

Expected default cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, disk usage only

## Next Step

Setup ඉවර වූ පසු beginner MLOps notes කියවන්න:

    docs/mlops-notes/01-why-mlops-exists-si.md
    docs/mlops-notes/02-mlops-core-concepts-si.md
    docs/mlops-notes/03-mlops-tool-map-si.md

ඊට පස්සේ first Foundation lab එක available උනාම පටන් ගන්න.
