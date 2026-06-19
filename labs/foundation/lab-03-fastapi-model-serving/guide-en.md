# Guide - Foundation Lab 03: FastAPI Model Serving

## What You Will Learn

This lab teaches how to serve a trained machine learning model using FastAPI.

You will learn:

    what model serving means
    why APIs are used in MLOps
    how to train and save a model
    how to load a saved model in an API
    how to create a health endpoint
    how to create a prediction endpoint
    how to send JSON input to an API
    how to receive prediction output as JSON
    how to use FastAPI Swagger UI

## Where This Lab Fits in MLOps

This lab belongs to the model serving stage of the MLOps lifecycle.

A simple MLOps lifecycle looks like this:

    Data understanding
        |
        v
    Model training
        |
        v
    Experiment tracking
        |
        v
    Reproducible training
        |
        v
    Model serving
        |
        v
    Deployment
        |
        v
    Monitoring

In previous labs, you trained models and created model files.

In this lab, you expose a trained model through an API so other applications can request predictions.

## Why Model Serving Matters

Training a model is only one part of MLOps.

A model becomes useful when another system can use it.

For example:

    a web application may need a prediction
    a mobile app may need a recommendation
    an internal business tool may need a risk score
    a backend system may need a forecast

Those systems should not directly open a Python notebook.

Instead, they send data to an API.

The API loads the trained model, runs prediction, and returns the result.

## Real-world Business Example

Imagine a retail company has trained a sales prediction model.

A business application wants to estimate future sales.

The application sends input data to the API.

The API returns a prediction.

The flow looks like this:

    Business application
        |
        v
    JSON request
        |
        v
    FastAPI prediction endpoint
        |
        v
    Saved ML model
        |
        v
    JSON prediction response

This is the basic idea of model serving.

## Key Concepts

### API

An API allows one system to communicate with another system.

In this lab, the API receives input data and returns a model prediction.

### Endpoint

An endpoint is a specific URL path in an API.

This lab has three main endpoints:

    GET /
        Basic API information.

    GET /health
        Checks whether the API is running and the model is loaded.

    POST /predict
        Accepts input features and returns a prediction.

### JSON

JSON is a common format for sending data between systems.

Example request:

    {
      "age": 0.0380759064334241,
      "sex": 0.0506801187398186,
      "bmi": 0.0616962065186885
    }

Example response:

    {
      "prediction": 181.99608277660315,
      "model_name": "Ridge Regression",
      "mlops_stage": "model serving"
    }

### FastAPI

FastAPI is a Python framework for building APIs.

It is useful for learning model serving because it provides:

    simple Python syntax
    automatic API documentation
    request validation
    JSON request and response support
    Swagger UI

### Pydantic Schema

FastAPI uses Pydantic models to validate request and response data.

In this lab:

    PredictionRequest
        defines the input fields expected by the API.

    PredictionResponse
        defines the response returned by the API.

### Health Endpoint

A health endpoint checks whether the API is working.

In this lab, the health endpoint returns:

    API status
    whether the model is loaded
    expected feature count

### Prediction Endpoint

The prediction endpoint receives input values, creates a DataFrame, sends it to the model, and returns a prediction.

## Files in This Lab

    requirements.txt
        Python packages required for training and API serving.

    src/train_model.py
        Trains a Ridge Regression model and saves model files.

    src/app.py
        FastAPI application that serves the trained model.

    models/
        Stores generated model files.

    outputs/
        Stores generated training metrics.

## Step 1: Create a Virtual Environment

From the Lab 03 folder:

    python3.12 -m venv .venv
    source .venv/bin/activate

Check Python version:

    python --version

Expected:

    Python 3.12.x

## Step 2: Install Dependencies

Run:

    python -m pip install -r requirements.txt

If your environment has SSL certificate issues, use:

    python -m pip install \
      --trusted-host pypi.org \
      --trusted-host files.pythonhosted.org \
      --trusted-host pypi.python.org \
      -r requirements.txt

The trusted-host option is a temporary workaround for local learning environments.

## Step 3: Train the Model

Run:

    python src/train_model.py

This script:

    loads the diabetes sample dataset
    trains a Ridge Regression model
    saves the model
    saves feature names
    saves training metrics

Expected output:

    Model training completed
    Model saved to: models/model.joblib
    Feature names saved to: models/feature_names.json
    Metrics saved to: outputs/training_metrics.json

## Step 4: Verify Generated Files

Run:

    ls -la models
    ls -la outputs

Expected files:

    models/model.joblib
    models/feature_names.json
    outputs/training_metrics.json

These files are generated locally when the lab is run.

They should not be committed to the repository.

## Step 5: Run the FastAPI Server

Run:

    python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8000

Expected output:

    Uvicorn running on http://127.0.0.1:8000

Keep this terminal open.

The API server runs in this terminal.

## Step 6: Open Swagger UI

Open this URL in your browser:

    http://127.0.0.1:8000/docs

You should see automatic API documentation.

You should see:

    GET /
    GET /health
    POST /predict

This documentation is generated by FastAPI.

## Step 7: Test the Health Endpoint

Open a new terminal.

Go to the Lab 03 folder and activate the virtual environment:

    cd labs/foundation/lab-03-fastapi-model-serving
    source .venv/bin/activate

Run:

    curl http://127.0.0.1:8000/health

Expected response:

    {"status":"healthy","model_loaded":true,"feature_count":10}

This confirms:

    API is running
    model is loaded
    feature count is correct

## Step 8: Test the Prediction Endpoint

Run:

    curl -X POST http://127.0.0.1:8000/predict \
      -H "Content-Type: application/json" \
      -d '{
        "age": 0.0380759064334241,
        "sex": 0.0506801187398186,
        "bmi": 0.0616962065186885,
        "bp": 0.0218723855140367,
        "s1": -0.0442234984244464,
        "s2": -0.0348207628376986,
        "s3": -0.0434008456520269,
        "s4": -0.00259226199818328,
        "s5": 0.0199074861704627,
        "s6": -0.0176461251598038
      }'

Expected response:

    {
      "prediction": 181.99608277660315,
      "model_name": "Ridge Regression",
      "mlops_stage": "model serving"
    }

The exact prediction value may differ slightly depending on package versions.

## What You Proved

By completing this lab, you proved that:

    a trained ML model can be saved
    a FastAPI app can load the saved model
    an API can receive JSON input
    the model can generate a prediction
    the API can return the prediction as JSON

This is the foundation of model serving.

## Common Issues

### Model file not found

If you see:

    Model file not found

Run:

    python src/train_model.py

Then start the API again.

### Port 8000 already in use

If port 8000 is busy, use another port:

    python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8001

Then open:

    http://127.0.0.1:8001/docs

### Cannot connect to API

Make sure Uvicorn is still running.

The terminal running Uvicorn must stay open.

### Validation error

If the prediction endpoint returns a validation error, check that all 10 input fields are included:

    age
    sex
    bmi
    bp
    s1
    s2
    s3
    s4
    s5
    s6

## Cleanup

Stop the API server:

    CTRL + C

Remove generated files:

    rm -f models/model.joblib
    rm -f models/feature_names.json
    rm -f outputs/training_metrics.json

Remove Python cache:

    rm -rf src/__pycache__

Optional:

    rm -rf .venv

See cleanup.md for the full cleanup guide.

## What You Learned

You learned how to:

    train and save a model
    load a model in a FastAPI application
    create health and prediction endpoints
    test an API with curl
    use Swagger UI
    return model predictions as JSON

## Connection to Previous Labs

Lab 00:

    You learned the basic ML workflow.

Lab 01:

    You learned experiment tracking with MLflow.

Lab 02:

    You learned Dockerized ML training.

Lab 03:

    You learned model serving with FastAPI.

## Next Lab

The next lab focuses on local model artifact management.

That lab will improve how model files and related metadata are organized.
