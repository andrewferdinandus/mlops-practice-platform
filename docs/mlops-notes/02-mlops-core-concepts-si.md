# MLOps Core Concepts - සිංහල Guide

මෙම note එකෙන් MLOps වලදී නිතර භාවිතා වන basic terms සරලව explain කරයි.

Labs වලට යන්න කලින් මේ concepts තේරුම් ගත්තොත් MLflow, Docker, FastAPI, MinIO, Prometheus, Grafana, Evidently වගේ tools භාවිතා කරන එක ලේසි වෙනවා.

## Experiment

Experiment එකක් කියන්නේ එකම goal එකකට අදාළ model training attempts කිහිපයක් එකට group කරන එක.

Example:

    House price prediction experiment

මේ experiment එක ඇතුළේ different settings වලින් models කිහිපයක් train කරන්න පුළුවන්.

## Run

Run එකක් කියන්නේ experiment එකක් ඇතුළේ කරන එක් training attempt එකක්.

Example:

    Run 1: max_depth = 3 වලින් model train කිරීම
    Run 2: max_depth = 5 වලින් model train කිරීම
    Run 3: max_depth = 10 වලින් model train කිරීම

හැම run එකකටම parameters, metrics, artifacts තියෙන්න පුළුවන්.

## Parameter

Parameter එකක් කියන්නේ model train කරන විට භාවිතා කරන setting එකක්.

Examples:

    learning_rate = 0.01
    max_depth = 5
    n_estimators = 100
    batch_size = 32

Model එක train කළේ කොහොමද කියලා තේරුම් ගන්න parameters වැදගත්.

හොඳ result එකක් ලැබුණොත් ඒ result එක නැවත reproduce කරන්න parameters අවශ්‍ය වෙනවා.

## Metric

Metric එකක් කියන්නේ model එක කොච්චර හොඳට වැඩ කළාද කියලා පෙන්වන number එකක්.

Examples:

    accuracy = 0.87
    precision = 0.84
    recall = 0.80
    f1_score = 0.82
    rmse = 1200.50

Different model runs compare කරන්න metrics භාවිතා කරනවා.

## Artifact

Artifact එකක් කියන්නේ training, evaluation, හෝ inference process එකකින් generate වෙන file එකක්.

Examples:

    trained model file
    confusion matrix image
    metrics report
    prediction output
    data validation report
    drift report

Artifacts හොඳට save කරලා organize කළොත් පසුව reuse කරන්න ලේසි වෙනවා.

## Model

Model එකක් කියන්නේ train කරපු machine learning object එකක්. ඒක predictions දෙන්න භාවිතා කරනවා.

Examples:

    House price model එක house price predict කරනවා.
    Fraud detection model එක transaction එක risky ද කියලා predict කරනවා.
    Churn model එක customer කෙනෙක් leave වෙයිද කියලා predict කරනවා.

MLOps වලදී model file එක save කරන්න, version කරන්න, test කරන්න, deploy කරන්න අවශ්‍යයි.

## Model Version

Model version එකක් කියන්නේ model එකේ specific saved version එකක්.

Examples:

    house-price-model:v1
    house-price-model:v2
    house-price-model:v3

Model versioning වැදගත් වෙන්නේ පසුව debugging, rollback, සහ comparison කරන්න.

## Model Registry

Model registry එකක් කියන්නේ model versions organize කරලා manage කරන place එකක්.

Registry එකක stages මෙහෙම තියෙන්න පුළුවන්:

    candidate
    approved
    staging
    production
    archived

Model එකක් production වලට යන්න ready ද කියලා manage කරන්න registry එකක් උදව් වෙනවා.

## Pipeline

Pipeline එකක් කියන්නේ ordered steps කිහිපයක්.

Simple ML pipeline එකක් මෙහෙම වෙන්න පුළුවන්:

    load data
    validate data
    train model
    evaluate model
    save model
    generate report

Pipelines වලින් ML workflows repeatable වෙනවා.

## Reproducibility

Reproducibility කියන්නේ workflow එක නැවත run කළාම same හෝ similar result එකක් ලබාගන්න පුළුවන් වීම.

Reproducibility සඳහා track කරන්න ඕනේ දේවල්:

    code version
    data version
    parameters
    environment
    dependencies
    random seed
    model artifacts

Reproducibility නැතිනම් model results trust කරන්න අමාරු වෙනවා.

## Model Serving

Model serving කියන්නේ trained model එක predictions ලබාදීමට available කිරීම.

Common serving methods:

    API serving
    batch inference
    streaming inference
    application එකක් ඇතුළේ model එක use කිරීම

Beginner labs වලදී FastAPI භාවිතා කරලා API serving practice කිරීම හොඳ starting point එකක්.

## Batch Inference

Batch inference කියන්නේ records ගොඩකට එකවර predictions run කිරීම.

Example:

    input file: customers.csv
    output file: predictions.csv

Scheduled jobs, reports, offline predictions සඳහා batch inference භාවිතා කරනවා.

## Monitoring

Monitoring කියන්නේ system එක කාලයත් සමඟ හරියට වැඩ කරනවද කියලා බලන එක.

Model API එකකට monitoring examples:

    request count
    response time
    error count
    CPU and memory usage

ML quality monitoring examples:

    prediction distribution
    input data changes
    model performance
    drift signals

## Data Drift

Data drift කියන්නේ current data, model එක train කළ data වලට වඩා වෙනස් වීම.

Example:

    Model එක January customer behavior වලින් train කරලා තියෙනවා.
    June වෙද්දී customer behavior වෙනස් වෙලා.
    Model performance අඩු වෙන්න පුළුවන්.

Data drift කියන්නේ model එක අනිවාර්යෙන් broken කියන එක නෙවෙයි. නමුත් ඒක warning sign එකක්.

## Deployment

Deployment කියන්නේ model එක හෝ model service එක use කරන්න පුළුවන් තැනකට release කිරීම.

Examples:

    model API එක Docker වල run කිරීම
    model service එක Kubernetes වල deploy කිරීම
    batch inference job එක publish කිරීම
    model එක production stage එකට promote කිරීම

Deployment කරනකොට testing සහ rollback plan එකක් තිබිය යුතුයි.

## Rollback

Rollback කියන්නේ new version එකක problem එකක් තිබුණොත් කලින් වැඩ කළ version එකකට ආපසු යාම.

Example:

    model v3 එකේ errors තියෙනවා
    model v2 එකට ආපසු switch කරනවා

New model එක testing වල හොඳට පෙනුණත් real-world වල fail වෙන්න පුළුවන්. ඒ නිසා rollback වැදගත්.

## Cleanup

Cleanup කියන්නේ lab එකක හෝ workflow එකක create කරපු resources remove කිරීම.

Examples:

    containers stop කිරීම
    Docker volumes delete කිරීම
    temporary files remove කිරීම
    local Kubernetes clusters delete කිරීම
    generated artifacts remove කිරීම

Cleanup environment එක clean තියාගන්න සහ unnecessary cost avoid කරන්න උදව් වෙනවා.

## Simple Summary

MLOps තේරුම් ගන්න පහත concepts වැදගත්:

    experiment
    run
    parameter
    metric
    artifact
    model version
    model registry
    pipeline
    reproducibility
    serving
    monitoring
    drift
    deployment
    rollback
    cleanup

Labs වලදී මේ concepts practical විදිහට practice කරනවා.
