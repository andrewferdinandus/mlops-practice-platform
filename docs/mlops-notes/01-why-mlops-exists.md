# Why MLOps Exists

Training a machine learning model is only one part of a real machine learning system.

In real-world projects, a model must be tracked, saved, tested, served, monitored, updated, and sometimes rolled back.

MLOps helps manage that full lifecycle.

## A Simple Example

Imagine you are building a house price prediction model.

The model receives input values:

    bedrooms = 3
    bathrooms = 2
    location = Colombo
    size = 1200 sqft

The model returns a prediction:

    predicted price = 35,000,000 LKR

This may work well inside a training notebook.

But real-world usage creates more questions.

## Problem 1: Which model is the best?

You may train many versions of the same model.

    Model A accuracy = 82%
    Model B accuracy = 87%
    Model C accuracy = 79%

Now you need to know:

    Which model performed best?
    Which parameters were used?
    Can the result be reproduced?
    Where is the trained model file?

Manually writing these details in a notebook or text file becomes messy very quickly.

This is why experiment tracking is important.

Experiment tracking helps record details related to each training run.

Examples:

    parameters
    metrics
    artifacts
    training runs

## Problem 2: Where is the model file?

After training, you may save the model as:

    model.pkl

After a few experiments, the folder may look like this:

    model.pkl
    model_final.pkl
    model_final_new.pkl
    best_model.pkl
    best_model_really_final.pkl

This is risky in real projects.

It becomes difficult to identify the correct model later.

A model file is an artifact.

An artifact is a file created during training, evaluation, or inference.

Examples:

    trained model file
    plots
    metrics report
    prediction output
    data validation report

Good artifact management helps you find the correct model later.

## Problem 3: Can another person run the model?

A training script may work on your laptop.

But another person may get errors when running the same code.

Common reasons include:

    different Python version
    different library versions
    missing dependency
    different file path
    missing environment variable

This is why reproducible environments are important.

Tools like Docker help package code and dependencies so the workflow can run more consistently across machines.

## Problem 4: How does an application use the model?

A trained model is not very useful if only one notebook can use it.

In a real application, another system may need predictions.

Example workflow:

    A user enters house details on a website.
    The backend service sends those details to the model.
    The model returns a predicted price.
    The website shows the result to the user.

This is model serving.

A common way to serve a model is to expose it through an API.

FastAPI is one tool that can be used to build a simple model API.

## Problem 5: What happens when data changes?

A model may be trained using January data.

But by June, the real-world data may look different.

For example:

    house prices may change
    user behavior may change
    input data patterns may change

This is called data drift.

Data drift can reduce model performance.

MLOps workflows help monitor data and model behavior over time.

## Problem 6: How do you safely release a new model?

A new model may look better than the old model during testing.

But replacing the production model immediately can be risky.

A safer release process may include:

    test the new model
    compare metrics
    review the result
    release to a small group first
    monitor behavior
    roll back if there is a problem

This is part of model deployment and release management.

## What is MLOps?

A simple way to think about MLOps is:

    MLOps = Machine Learning + Software Engineering + DevOps practices

MLOps helps machine learning models move from experiments to reliable real-world systems.

## What Problems Does MLOps Solve?

MLOps helps with:

    experiment tracking
    model versioning
    artifact management
    reproducible training
    model serving
    monitoring
    data drift detection
    deployment
    rollback
    automation

## Simple Summary

Training a model is only the first step.

A real machine learning system also needs a way to:

    track experiments
    save artifacts
    manage versions
    serve predictions
    monitor behavior
    update models
    clean up resources

MLOps provides practices and tools for managing this full lifecycle.

## Next Note

The next note explains core MLOps concepts:

    experiment
    run
    parameter
    metric
    artifact
    model registry
    pipeline
    deployment
    monitoring
    drift
