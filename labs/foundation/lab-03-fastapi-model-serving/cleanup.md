# Cleanup - Lab 03

This guide removes local files created during Lab 03.

Lab 03 does not create cloud resources, Docker images, or Kubernetes resources.

## Stop the API Server

If Uvicorn is running, stop it with:

    CTRL + C

## Deactivate Virtual Environment

If the virtual environment is active:

    deactivate

## Remove Generated Model and Output Files

From the Lab 03 folder:

    rm -f models/model.joblib
    rm -f models/feature_names.json
    rm -f outputs/training_metrics.json

Keep placeholder files:

    touch models/.gitkeep
    touch outputs/.gitkeep

## Remove Python Cache Files

    rm -rf src/__pycache__

## Optional: Remove Virtual Environment

The virtual environment is local only and should not be committed.

    rm -rf .venv

## Verify Cleanup

Run:

    find . -maxdepth 3 -type f | sort

Expected important files:

    ./README.md
    ./cleanup.md
    ./guide-en.md
    ./guide-si.md
    ./models/.gitkeep
    ./outputs/.gitkeep
    ./requirements.txt
    ./src/app.py
    ./src/train_model.py

## Cost Note

This lab runs locally.

Expected cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, and disk usage
