# Guide - Foundation Lab 00: Dataset and ML Workflow Basics

## මෙම Lab එකෙන් ඉගෙන ගන්න දේ

මෙම lab එකෙන් MLflow, Docker, Kubernetes, monitoring වගේ MLOps tools වලට යන්න කලින් basic machine learning workflow එක explain කරයි.

ඔබට ඉගෙන ගන්න පුළුවන්:

    dataset කියන්නේ මොකක්ද
    features කියන්නේ මොනවාද
    target value කියන්නේ මොකක්ද
    training data සහ test data කියන්නේ මොනවාද
    model train කරනවා කියන්නේ මොකක්ද
    model evaluate කරනවා කියන්නේ මොකක්ද
    metrics කියන්නේ මොනවාද
    model file එකක් save කරනවා කියන්නේ මොකක්ද
    saved model එකකින් predictions ගන්නවා කියන්නේ මොකක්ද

මෙම lab එක simpleව තියාගෙන තියෙන්නේ Lab 01 වල MLflow experiment tracking තේරුම් ගන්න පහසු වෙන්න.

## මෙම Lab එක MLOps Lifecycle එකේ කොතනද?

මෙම lab එක MLOps lifecycle එකේ මුල් stage එකට අදාළයි.

    Data understanding
        |
        v
    Basic model training
        |
        v
    Basic model evaluation
        |
        v
    Save model output
        |
        v
    Experiment tracking in the next lab

මෙම lab එකේදී model deploy කරන්නේ නැහැ.

මෙම lab එකෙන් ඉගෙන ගන්නේ tracking, packaging, serving, deployment, monitoring වලට කලින් තියෙන basic ML workflow එකයි.

## Real-world Business Example

Retail company එකක් weekly sales predict කරන්න model එකක් හදනවා කියලා හිතන්න.

Company එකට historical data තියෙන්න පුළුවන්:

    store size
    location
    number of employees
    promotion amount
    season
    previous week sales

Predict කරන්න ඕනේ value එක:

    next week sales

Machine learning language වලින්:

    features = model එකට දෙන input columns
    target   = model එක predict කරන්න හදන value එක

Retail example එකේ:

    features වෙන්නේ store size, location, promotion amount, previous sales වගේ columns
    target වෙන්නේ next week sales

Model එක past data වලින් patterns ඉගෙනගෙන new data වලට predictions දෙන්න ඉගෙන ගන්නවා.

## මෙම Lab එකේ භාවිතා කරන Dataset එක

මෙම lab එක scikit-learn වල built-in sample dataset එකක් භාවිතා කරනවා.

External data download කරන්න අවශ්‍ය නැහැ.

Important note:

    මෙම dataset එක learning purpose එකට පමණයි.
    Medical production model එකක් build කිරීම මෙහි අරමුණ නොවෙයි.
    අරමුණ basic ML workflow එක තේරුම් ගැනීමයි.

මේ same workflow එක sales prediction, customer churn prediction, fraud detection, demand forecasting වගේ business problems වලට later apply කරන්න පුළුවන්.

## Basic Concepts

### Dataset

Dataset එකක් කියන්නේ rows සහ columns වලින් තියෙන data collection එකක්.

Row එකක් සාමාන්‍යයෙන් එක record එකක්.

Column එකක් යම් information එකක්.

Business example එකකදී එක row එකක් store එකක එක week එකක sales record එකක් වෙන්න පුළුවන්.

### Features

Features කියන්නේ model එකට input විදිහට දෙන columns.

Examples:

    store size
    location
    promotion amount
    customer count
    previous sales

මෙම lab එකේ feature columns:

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

මෙම medical columns එකින් එක deeply තේරුම් ගන්න අවශ්‍ය නැහැ.

මෙතන වැදගත් idea එක:

    features කියන්නේ inputs

### Target

Target කියන්නේ model එක predict කරන්න හදන value එක.

Sales prediction example එකේ:

    target = next week sales

මෙම lab එකේ:

    target = sample dataset එකෙන් ලබාදෙන target value එක

මෙතන වැදගත් idea එක:

    target කියන්නේ model එක predict කරන්න ඉගෙන ගන්න answer එක

### Training Data සහ Test Data

Full dataset එක parts දෙකකට split කරනවා:

    training data
    test data

Training data භාවිතා කරන්නේ model එක train කරන්න.

Test data භාවිතා කරන්නේ model එක previously නොදුටු data මත කොච්චර හොඳට වැඩ කරනවාද බලන්න.

Model එක training data memorize කරන එක විතරක් ප්‍රමාණවත් නැහැ. New data වලටත් reasonable predictions දෙන්න ඕනේ.

### Model Training

Model training කියන්නේ model එක training data වලින් patterns ඉගෙන ගන්න එක.

මෙම lab එකේ model එක input features බලලා target value එකට relation එකක් ඉගෙන ගන්නවා.

මෙම lab එකේ simple Ridge Regression model එකක් train කරනවා.

Ridge Regression deeply තේරුම් ගන්න මෙම lab එකට අවශ්‍ය නැහැ.

සරලව හිතන්න:

    model එක කියන්නේ data වලින් ඉගෙන ගත්ත prediction function එකක්

### Model Evaluation

Training ඉවර වූ පසු model එක test dataset එක මත check කරනවා.

Model එක predictions generate කරනවා.

ඊට පස්සේ ඒ predictions actual target values සමඟ compare කරනවා.

මේ comparison එකෙන් model performance metrics ලැබෙනවා.

### Metrics

Metrics කියන්නේ model එක කොච්චර හොඳට වැඩ කළාද කියලා පෙන්වන numbers.

මෙම lab එක save කරන metrics:

    RMSE
    MAE
    R2

Beginner level එකේදී RMSE එකට වැඩි අවධානය දෙන්න.

Simple idea:

    RMSE අඩු නම් usually prediction errors අඩුයි

### Model File

Training ඉවර වුනාම model එක file එකක් විදිහට save කරනවා:

    outputs/model/basic_model.joblib

මෙය trained model එකේ saved version එක.

Saved model එක later load කරලා නැවත training නොකර predictions ගන්න පුළුවන්.

### Predictions

Script එක sample predictions file එකක්ද create කරනවා:

    outputs/basic_predictions.csv

මෙම file එකේ තියෙන්නේ:

    input features
    actual target value
    predicted target value

මෙයින් model output එක real value එකට compare කරන්න පුළුවන්.

## Local Architecture

මෙම lab එක සම්පූර්ණයෙන් local machine එකේ run වෙනවා.

    Python script
        |
        v
    Built-in sample dataset
        |
        v
    Basic model training
        |
        v
    Metrics and saved model
        |
        v
    Output files

Docker, cloud account, Kubernetes cluster අවශ්‍ය නැහැ.

## මෙම Lab එකෙන් Create වෙන Files

Scripts run කළාට පස්සේ පහත files create වෙනවා:

    outputs/dataset_preview.csv
        Dataset එකේ first rows කිහිපය.

    outputs/dataset_summary.json
        Row count, feature count, target column වගේ basic information.

    outputs/feature_summary.csv
        Dataset columns වල statistical summary.

    outputs/model/basic_model.joblib
        Saved trained model file.

    outputs/basic_metrics.json
        Model performance metrics.

    outputs/basic_predictions.csv
        Saved model එකෙන් generate කළ sample predictions.

## Step 1: Lab Folder එකට යන්න

Repository root එකේ සිට:

    cd labs/foundation/lab-00-dataset-and-ml-workflow-basics

## Step 2: Python Virtual Environment එක Create කරන්න

Run කරන්න:

    python3 -m venv .venv

මෙම command එකෙන් මෙම lab එකට isolated Python environment එකක් create වෙනවා.

## Step 3: Virtual Environment එක Activate කරන්න

Run කරන්න:

    source .venv/bin/activate

Activate උනාම terminal prompt එකේ මෙහෙම පේන්න ඕනේ:

    (.venv)

ඒ කියන්නේ Python packages මෙම lab environment එක ඇතුළේ install වෙනවා.

## Step 4: Required Packages Install කරන්න

Run කරන්න:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

මෙයින් lab එකට අවශ්‍ය Python libraries install වෙනවා.

## Step 5: Dataset එක Explore කරන්න

Run කරන්න:

    python src/explore_data.py

මෙම script එක dataset එක load කරලා summary files create කරනවා.

Expected output:

    Dataset exploration completed
    Rows: 442
    Features: 10
    Target column: target

## Step 6: Basic Model එක Train කරන්න

Run කරන්න:

    python src/train_basic_model.py

මෙම script එකෙන්:

    dataset load කරනවා
    data train සහ test ලෙස split කරනවා
    model එක train කරනවා
    model එක evaluate කරනවා
    metrics save කරනවා
    trained model එක save කරනවා
    sample predictions save කරනවා

Expected output:

    Basic model training completed
    Training rows: 353
    Test rows: 89
    Feature count: 10

RMSE, MAE, R2 වගේ metric values ද පේන්න ඕනේ.

## Step 7: Generated Outputs Check කරන්න

Run කරන්න:

    ls -la outputs
    ls -la outputs/model

පහත files පේන්න ඕනේ:

    dataset_preview.csv
    dataset_summary.json
    feature_summary.csv
    basic_metrics.json
    basic_predictions.csv
    model/basic_model.joblib

Dataset summary බලන්න:

    cat outputs/dataset_summary.json

Model metrics බලන්න:

    cat outputs/basic_metrics.json

Sample predictions බලන්න:

    head outputs/basic_predictions.csv

## ඔබ Generate කළ Result එක මොකක්ද?

මෙම lab එක අවසානයේ ඔබ generate කරන්නේ:

    dataset summary එකක්
    feature summary එකක්
    trained model file එකක්
    model metrics
    sample predictions

ඒ කියන්නේ ඔබ local machine එකේ basic ML workflow එකක් complete කරලා තියෙනවා.

## MLOps වලට මෙය වැදගත් ඇයි?

MLOps Kubernetes හෝ deployment වලින් පටන් ගන්නේ නැහැ.

MLOps පටන් ගන්න කලින් basic ML workflow එක තේරුම් ගන්න ඕනේ:

    මොන data එකද use කළේ?
    target එක මොකක්ද?
    model එක train කළේ කොහොමද?
    model එක evaluate කළේ කොහොමද?
    model file එක save වෙලා තියෙන්නේ කොහෙද?
    output එක later check කරන්න පුළුවන්ද?

මෙම foundation එක නැතුව experiment tracking, model serving, monitoring, deployment තේරුම් ගන්න අමාරුයි.

## Lab 01 සමඟ සම්බන්ධය

Lab 00 එකේදී එක model එකක් train කරලා එක result එකක් save කරනවා.

Lab 01 එකේදී next step එකට යනවා.

Lab 01 එකේදී:

    multiple model runs train කරනවා
    parameter values වෙනස් කරනවා
    MLflow වල parameters track කරනවා
    MLflow වල metrics track කරනවා
    MLflow වල model artifacts save කරනවා
    MLflow UI එකේ runs compare කරනවා
    best model එක select කරනවා

Simple connection:

    Lab 00 = basic ML workflow එක ඉගෙන ගන්නවා
    Lab 01 = ඒ workflow එක MLflow වලින් track කරනවා

## Common Mistakes

### Virtual environment active නැහැ

Packages missing නම් virtual environment එක activate කරන්න:

    source .venv/bin/activate

### Wrong folder එකක commands run කිරීම

ඔබ Lab 00 folder එකේ ඉන්නවාද check කරන්න:

    pwd

Expected path එක අවසන් වෙන්න ඕනේ:

    labs/foundation/lab-00-dataset-and-ml-workflow-basics

### outputs folder එක missing

Scripts outputs folder එක automatically create කරනවා.

අවශ්‍ය නම් recreate කරන්න:

    mkdir -p outputs
    touch outputs/.gitkeep

## Cleanup

Cleanup guide එක බලන්න:

    cleanup.md

Basic cleanup command:

    rm -rf outputs
    mkdir -p outputs
    touch outputs/.gitkeep

Optional virtual environment cleanup:

    rm -rf .venv

## Cost Note

මෙම lab එක localව run වෙනවා.

Expected cost:

    Cloud cost: 0
    Local cost: small amount of CPU, memory, and disk usage

## ඔබ ඉගෙන ගත්ත දේ

මෙම lab එකෙන් MLOps tools වලට කලින් තියෙන basic workflow එක ඉගෙන ගත්තා:

    data load කිරීම
    features සහ target තේරුම් ගැනීම
    data split කිරීම
    model train කිරීම
    model evaluate කිරීම
    model save කිරීම
    predictions generate කිරීම

මෙම foundation එක next lab එකේ MLflow experiment tracking ඉගෙන ගන්න අවශ්‍යයි.
