# Guide - Foundation Lab 01: Local MLflow Experiment Tracking

## මෙම Lab එකෙන් ඉගෙන ගන්න දේ

මෙම lab එකෙන් MLflow භාවිතා කරලා experiment tracking කරන ආකාරය ඉගෙන ගන්නවා.

ඔබට ඉගෙන ගන්න පුළුවන්:

    experiment කියන්නේ මොකක්ද
    run කියන්නේ මොකක්ද
    parameters කියන්නේ මොනවාද
    metrics කියන්නේ මොනවාද
    artifacts කියන්නේ මොනවාද
    model training runs track කරන්නේ ඇයි
    model runs කිහිපයක් compare කරන්නේ කොහොමද
    best model එක select කරන්නේ කොහොමද
    MLflow experiment data save කරන්නේ කොහෙද
    saved model එකකින් predictions generate කරන්නේ කොහොමද

මෙම lab එක Lab 00 එකට directly connect වෙනවා.

Lab 00 එකේදී එක model එකක් train කරලා එක result එකක් save කළා.

Lab 01 එකේදී model runs කිහිපයක් train කරලා, ඒ හැම run එකම MLflow වල track කරනවා.

## මෙම Lab එක MLOps Lifecycle එකේ කොතනද?

මෙම lab එක MLOps lifecycle එකේ experimentation සහ experiment tracking stage එකට අදාළයි.

Simple MLOps lifecycle එකක් මෙහෙම හිතන්න:

    Data understanding
        |
        v
    Basic model training
        |
        v
    Experiment tracking
        |
        v
    Model comparison
        |
        v
    Best model selection
        |
        v
    Model packaging
        |
        v
    Model serving
        |
        v
    Deployment
        |
        v
    Monitoring

මෙම lab එක focus කරන්නේ:

    experiment tracking
    model comparison
    best model selection

මෙම lab එකේදී model එක deploy කරන්නේ නැහැ.

මෙම lab එකේදී Docker, Kubernetes, cloud services භාවිතා කරන්නේ නැහැ.

ඒ topics පසුව labs වලදී ඉගෙන ගන්නවා.

## මෙම Lab එක වැදගත් ඇයි?

Real machine learning projects වල model එකක් සාමාන්‍යයෙන් එක වරක් train කරලා නවතින්නේ නැහැ.

Data scientist හෝ ML engineer කෙනෙක් different settings දාලා models කිහිපයක් train කරනවා.

Example:

    Run 1: alpha = 0.01
    Run 2: alpha = 0.1
    Run 3: alpha = 1.0
    Run 4: alpha = 10.0

Training attempts කිහිපයක් කළාට පස්සේ ප්‍රශ්න එනවා:

    හොඳම model එක මොකක්ද?
    මොන settings use කළාද?
    මොන metrics ලැබුණාද?
    model file එක save වෙලා තියෙන්නේ කොහෙද?
    මේ result එක later check කරන්න පුළුවන්ද?
    වෙන කෙනෙක්ට මේක තේරුම් ගන්න පුළුවන්ද?

Experiment tracking නැත්නම් මේ answers messy වෙනවා.

MLflow මේ information organized විදිහට save කරන්න උදව් කරනවා.

## Real-world Business Example

Retail company එකක් weekly sales predict කරන්න model එකක් හදනවා කියලා හිතන්න.

Company එක model versions කිහිපයක් train කරනවා.

හැම model training attempt එකකටම team එකට දැනගන්න ඕනේ:

    මොන settings use කළාද
    model එක කොච්චර හොඳට perform කළාද
    trained model file එක කොහෙද save වෙලා තියෙන්නේ
    later use කරන්න හොඳම model එක මොකක්ද

Real company එකක මේ information වැදගත් වෙන්නේ model එක API එකක් විදිහට serve කරන්න, production වලට deploy කරන්න, හෝ monitor කරන්න කලින්.

මෙම lab එක scikit-learn වල built-in sample dataset එකක් භාවිතා කරනවා.

Dataset එක learning purpose එකට විතරයි.

Medical production model එකක් build කිරීම මෙහි goal එක නොවෙයි.

Goal එක experiment tracking concept එක ඉගෙන ගැනීමයි.

## Key Concepts

### Experiment

Experiment එකක් කියන්නේ related training attempts කිහිපයක් group කරන එක.

මෙම lab එකේ experiment name එක:

    foundation-lab-01-local-mlflow-tracking

මෙම experiment එක ඇතුළේ model training runs කිහිපයක් තියෙනවා.

### Run

Run එකක් කියන්නේ එක් training attempt එකක්.

මෙම lab එකේ alpha value එකකට එක run එකක් create වෙනවා.

Example:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

හැම run එකකටම parameters, metrics, සහ model artifact තියෙනවා.

### Parameter

Parameter කියන්නේ model train කරනකොට use කරන setting එකක්.

මෙම lab එකේ main parameter එක:

    alpha

alpha එක control knob එකක් වගේ හිතන්න.

alpha වෙනස් කළාම model එක data වලින් ඉගෙන ගන්න ආකාරය වෙනස් වෙන්න පුළුවන්.

මෙම lab එක test කරන alpha values:

    0.01
    0.1
    1.0
    10.0

MLflow හැම run එකකටම alpha value එක record කරනවා.

### Metric

Metric එකක් කියන්නේ model එක කොච්චර හොඳට perform කළාද කියලා පෙන්වන number එකක්.

මෙම lab එක record කරන metrics:

    RMSE
    MAE
    R2

Beginner level එකේදී RMSE එකට focus කරන්න.

Simple idea:

    RMSE අඩු නම් usually prediction errors අඩුයි

Script එක lowest RMSE තියෙන model එක best model ලෙස select කරනවා.

### Artifact

Artifact කියන්නේ training හෝ evaluation process එකකින් generate වෙන file එකක්.

මෙම lab එකේදී MLflow හැම run එකකටම model artifact save කරනවා.

Lab එක selected best model එක local folder එකකටත් save කරනවා:

    outputs/best_model/model.joblib

Artifact වැදගත් වෙන්නේ model result එකක් තියුණත් actual model file එක පසුව හොයාගන්න බැරි නම් ඒ result එක practicalව use කරන්න අමාරු නිසා.

## මෙම Lab එකෙන් Build කරන දේ

මෙම lab එක local experiment tracking workflow එකක් build කරනවා.

Training script එකෙන්:

    sample dataset එක load කරනවා
    Ridge Regression model එක multiple times train කරනවා
    හැම run එකකටම alpha value වෙනස් කරනවා
    parameters MLflow වලට log කරනවා
    metrics MLflow වලට log කරනවා
    model artifacts MLflow වලට log කරනවා
    RMSE අනුව best model එක select කරනවා
    best model එක localව save කරනවා
    training summary එකක් write කරනවා
    saved model එකෙන් predictions generate කරනවා

## Local Architecture

මෙම lab එක සම්පූර්ණයෙන් local machine එකේ run වෙනවා.

    Python training script
        |
        v
    MLflow tracking database
        |
        +--> experiment name
        +--> run history
        +--> parameters
        +--> metrics
        |
        v
    Artifact folder
        |
        +--> MLflow model artifacts

    outputs/
        |
        +--> best model
        +--> training summary
        +--> sample predictions

## Data Save වෙන තැන්

මෙම lab එක local files සහ folders කිහිපයක් create කරනවා.

### mlflow.db

    mlflow.db

මෙය local SQLite database එකක්.

MLflow experiment metadata save කරන්න මෙය භාවිතා කරනවා.

මෙහි save වෙන දේවල්:

    experiment names
    run IDs
    parameters
    metrics
    artifact locations

### artifacts/

    artifacts/

MLflow model artifacts save කරන්න මෙම folder එක භාවිතා කරනවා.

Model artifact කියන්නේ training run එකක saved model output එක.

### outputs/training_summary.json

    outputs/training_summary.json

මෙම file එකේ all runs summary එක සහ selected best run එක save වෙනවා.

### outputs/best_model/model.joblib

    outputs/best_model/model.joblib

මෙය selected best model එක local file එකක් ලෙස save කරන තැන.

Prediction script එක මෙම model file එක load කරනවා.

### outputs/sample_predictions.csv

    outputs/sample_predictions.csv

Saved best model එකෙන් generate කළ sample predictions මෙම file එකේ save වෙනවා.

## භාවිතා කරන Tools

    Python
    scikit-learn
    MLflow
    pandas
    numpy
    joblib
    SQLite

## Step 1: Lab Folder එකට යන්න

Repository root එකේ සිට:

    cd labs/foundation/lab-01-local-mlflow-tracking

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

මෙයින් MLflow, scikit-learn, pandas, numpy, joblib install වෙනවා.

## Step 5: Model Runs Train කරලා Track කරන්න

Run කරන්න:

    python src/train.py

මෙම script එක model runs 4ක් train කරනවා.

හැම run එකකටම වෙනස් alpha value එකක් use කරනවා.

Expected run names:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

Script එක parameters, metrics, සහ model artifacts MLflow වලට log කරනවා.

Expected output:

    Run completed | alpha=0.01
    Run completed | alpha=0.1
    Run completed | alpha=1.0
    Run completed | alpha=10.0

Best model එකත් output එකේ පේනවා.

Example:

    Best model selected
    Best alpha: 0.1
    Best RMSE : 53.4461

Package versions අනුව exact numbers පොඩ්ඩක් වෙනස් වෙන්න පුළුවන්.

## Step 6: Predictions Generate කරන්න

Run කරන්න:

    python src/predict.py

මෙම script එකෙන්:

    best saved model එක load කරනවා
    sample data load කරනවා
    predictions generate කරනවා
    predictions CSV එකකට save කරනවා

Expected output:

    Sample predictions generated
    Model used: outputs/best_model/model.joblib
    Predictions saved to: outputs/sample_predictions.csv

## Step 7: MLflow UI Open කරන්න

Run කරන්න:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000

Browser එකේ open කරන්න:

    http://127.0.0.1:5000

Port 5000 already use වෙනවා නම්:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

ඊට පස්සේ browser එකේ open කරන්න:

    http://127.0.0.1:5001

Important:

    MLflow UI run කරන terminal එක busy වෙලා තියෙයි.
    ඒක normal.
    MLflow UI stop කරන්න Ctrl + C press කරන්න.

## Step 8: MLflow UI එකේ බලන්න ඕනේ දේවල්

MLflow UI එකේ experiment එක open කරන්න:

    foundation-lab-01-local-mlflow-tracking

Runs 4ක් පේන්න ඕනේ:

    ridge-alpha-0.01
    ridge-alpha-0.1
    ridge-alpha-1.0
    ridge-alpha-10.0

Run එකක් click කරලා බලන්න:

    Parameters
    Metrics
    Artifacts

Parameters වල:

    model_type
    alpha
    test_size
    random_state

Metrics වල:

    rmse
    mae
    r2

Artifacts වල model artifact එකක් තියෙනවාද බලන්න.

## Runs Compare කරන ආකාරය

මෙම lab එකේ main comparison එක RMSE.

Simple idea:

    RMSE අඩු නම් usually predictions හොඳයි

Runs 4ක RMSE values compare කරන්න.

Lowest RMSE තියෙන run එක best model ලෙස select වෙනවා.

Test output එකේ alpha 0.1 lowest RMSE දුන්නා.

ඒ නිසා best model එක ඒ run එකෙන් save කළා.

## Step 9: Local Output Files Check කරන්න

Run කරන්න:

    ls -la outputs
    ls -la outputs/best_model

පහත files පේන්න ඕනේ:

    training_summary.json
    sample_predictions.csv
    best_model/model.joblib

Training summary බලන්න:

    cat outputs/training_summary.json

Sample predictions බලන්න:

    head outputs/sample_predictions.csv

## ඔබ Generate කළ Result එක මොකක්ද?

මෙම lab එක අවසානයේ ඔබ generate කරන්නේ:

    tracked MLflow runs 4ක්
    logged parameters
    logged metrics
    logged model artifacts
    selected best model එකක්
    training summary එකක්
    saved model එකෙන් sample predictions

ඒ කියන්නේ ඔබ local experiment tracking workflow එකක් complete කරලා තියෙනවා.

## Real MLOps වලට මෙය වැදගත් ඇයි?

Experiment tracking කියන්නේ MLOps වල පළවෙනි practical skills වලින් එකක්.

එය teams වලට මේ ප්‍රශ්න වලට answer දෙන්න උදව් කරනවා:

    මොන model එක train කළාද?
    කොහොම train කළාද?
    කොච්චර හොඳට perform කළාද?
    best run එක මොකක්ද?
    model artifact එක කොහෙද?
    result එක later review කරන්න පුළුවන්ද?

Experiment tracking නැත්නම් model development එක experiments වැඩි වෙද්දී manage කරන්න අමාරු වෙනවා.

## Common Issues

### mlflow command not found

මෙහෙම error එකක් ආවොත්:

    zsh: command not found: mlflow

Virtual environment active නැතිවිය හැක.

Run කරන්න:

    source .venv/bin/activate

ඊට පස්සේ use කරන්න:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000

python -m mlflow use කිරීම safer. එයින් active Python environment එකේ MLflow run වෙනවා.

### Port already in use

මෙහෙම error එකක් ආවොත්:

    Address already in use

වෙන port එකක් use කරන්න:

    python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001

ඊට පස්සේ open කරන්න:

    http://127.0.0.1:5001

### Browser එක open උනත් runs පේන්නේ නැහැ

මුලින් database එකේ runs තියෙනවාද verify කරන්න:

    python - <<'PY'
    import mlflow

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    runs = mlflow.search_runs(
        experiment_names=["foundation-lab-01-local-mlflow-tracking"]
    )

    print("Runs found:", len(runs))
    print(runs[["run_id", "params.alpha", "metrics.rmse"]])
    PY

Runs found නම් MLflow UI නැවත start කරලා correct mlflow.db එකට point කරනවාද බලන්න.

### Pickle හෝ joblib security warning

pickle, cloudpickle, joblib model files ගැන warning එකක් පේන්න පුළුවන්.

මෙය normal security warning එකක්.

ඔබ trust කරන model files පමණක් load කරන්න.

මෙම lab එකේ model file එක ඔබගේ local script එකෙන් create කරපු එකක්.

## Cleanup

Cleanup guide එක බලන්න:

    cleanup.md

Basic cleanup commands:

    rm -f mlflow.db
    rm -rf artifacts/*
    touch artifacts/.gitkeep
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

මෙම lab එකෙන් ඔබ ඉගෙන ගත්තා:

    multiple model runs train කිරීම
    parameter values වෙනස් කිරීම
    parameters MLflow වලට log කිරීම
    metrics MLflow වලට log කිරීම
    model artifacts MLflow වලට log කිරීම
    MLflow UI එකෙන් runs compare කිරීම
    best model එක select කිරීම
    best model එක localව save කිරීම
    saved model එකකින් predictions generate කිරීම

## Next Lab සමඟ සම්බන්ධය

Lab 01 එකෙන් localව experiments track කරන ආකාරය ඉගෙන ගත්තා.

Next lab එකෙන් Dockerized ML training ඉගෙන ගන්නවා.

එහිදී training workflow එක container එකක් ඇතුළේ package කරනවා. ඒකෙන් වෙන machines වලත් workflow එක consistentව run කරන්න පුළුවන්.

Simple connection:

    Lab 01 = experiments track කිරීම
    Lab 02 = Docker වලින් training environment එක reproducible කිරීම
