# Foundation Lab 03: FastAPI Model Serving

This lab introduces model serving with FastAPI.

In previous labs, you trained machine learning models and learned how to track experiments and run training in Docker.

In this lab, you expose a trained model through an API so other applications can request predictions using JSON.

## Where This Lab Fits in MLOps

This lab belongs to the model serving stage of the MLOps lifecycle.

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

## What You Will Learn

You will learn how to:

    train and save a simple ML model
    save feature names for serving
    create a FastAPI application
    create a health endpoint
    create a prediction endpoint
    send JSON input to an API
    receive prediction output as JSON
    view automatic API documentation with Swagger UI

## Why Model Serving Matters

Training a model is not enough.

A business application needs a simple way to send input data and receive predictions.

Model serving allows a trained model to be used by:

    web applications
    mobile applications
    internal tools
    batch jobs
    other backend services

## Real-world Example

Imagine a retail company has trained a sales prediction model.

A business application can send customer or sales-related data to the API.

The API loads the trained model, runs the prediction, and returns the result as JSON.

## Files in This Lab

    requirements.txt
        Python dependencies for training and API serving.

    src/train_model.py
        Trains a Ridge Regression model and saves it.

    src/app.py
        FastAPI application that serves the trained model.

    models/
        Stores generated model files.

    outputs/
        Stores generated metrics.

## API Endpoints

    GET /
        Returns basic API information.

    GET /health
        Checks whether the API is running and the model is loaded.

    POST /predict
        Accepts input features and returns a prediction.

## Quick Start

Create and activate a virtual environment:

    python3.12 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

Train the model:

    python src/train_model.py

Run the API:

    python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8000

Open API documentation:

    http://127.0.0.1:8000/docs

Test health endpoint:

    curl http://127.0.0.1:8000/health

Test prediction endpoint:

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

## Expected Result

The health endpoint should return:

    {"status":"healthy","model_loaded":true,"feature_count":10}

The prediction endpoint should return a JSON response similar to:

    {
      "prediction": 181.99608277660315,
      "model_name": "Ridge Regression",
      "mlops_stage": "model serving"
    }

The exact prediction value may differ slightly depending on package versions.

## Cleanup

See:

    cleanup.md

## Next Lab

The next lab will focus on local model artifact management.
