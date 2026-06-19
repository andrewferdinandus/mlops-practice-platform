# Guide - Foundation Lab 03: FastAPI Model Serving

## මෙම Lab එකෙන් ඉගෙන ගන්න දේ

මෙම lab එකෙන් trained machine learning model එකක් FastAPI භාවිතා කරලා serve කරන ආකාරය ඉගෙන ගන්නවා.

ඔබට ඉගෙන ගන්න පුළුවන්:

    model serving කියන්නේ මොකක්ද
    MLOps වල API භාවිතා කරන්නේ ඇයි
    model එකක් train කරලා save කරන්නේ කොහොමද
    saved model එක API එකක load කරන්නේ කොහොමද
    health endpoint එකක් create කරන්නේ කොහොමද
    prediction endpoint එකක් create කරන්නේ කොහොමද
    JSON input එකක් API එකට යවන්නේ කොහොමද
    prediction output එක JSON response එකක් විදිහට ගන්නේ කොහොමද
    FastAPI Swagger UI use කරන්නේ කොහොමද

## මෙම Lab එක MLOps Lifecycle එකේ කොතනද?

මෙම lab එක MLOps lifecycle එකේ model serving stage එකට අදාළයි.

Simple MLOps lifecycle එකක් මෙහෙමයි:

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

කලින් labs වලදී ඔබ model train කළා, experiment track කළා, Docker තුළ training run කළා.

මෙම lab එකේදී trained model එක API එකක් විදිහට expose කරනවා.

## Model Serving වැදගත් ඇයි?

Model එක train කරන එක විතරක් ප්‍රමාණවත් නැහැ.

Business application එකකට model එකෙන් prediction එකක් ගන්න simple way එකක් ඕනේ.

උදාහරණයක් ලෙස:

    web application එකකට prediction එකක් ඕනේ
    mobile app එකකට recommendation එකක් ඕනේ
    internal business tool එකකට risk score එකක් ඕනේ
    backend service එකකට forecast එකක් ඕනේ

ඒ systems Python notebook එකක් open කරලා model එක run කරන්නේ නැහැ.

ඒ වෙනුවට ඒවා API එකකට data යවනවා.

API එක trained model එක load කරලා prediction එක return කරනවා.

## Real-world Business Example

Retail company එකක් sales prediction model එකක් train කරලා තියෙනවා කියලා හිතන්න.

Business application එකකට future sales estimate කරන්න ඕනේ.

Application එක input data API එකට යවනවා.

API එක prediction එක return කරනවා.

Flow එක මෙහෙමයි:

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

මේක තමයි model serving වල basic idea එක.

## Key Concepts

### API

API එකක් මගින් system එකක් වෙන system එකක් සමඟ communicate කරනවා.

මෙම lab එකේ API එක input data receive කරලා model prediction එකක් return කරනවා.

### Endpoint

Endpoint එකක් කියන්නේ API එකේ specific URL path එකක්.

මෙම lab එකේ main endpoints තුනක් තියෙනවා:

    GET /
        Basic API information.

    GET /health
        API එක run වෙනවාද සහ model එක load වෙලාද කියලා check කරනවා.

    POST /predict
        Input features accept කරලා prediction එකක් return කරනවා.

### JSON

JSON කියන්නේ systems අතර data send කරන්න commonly use කරන format එකක්.

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

FastAPI කියන්නේ Python වලින් APIs build කරන්න use කරන framework එකක්.

Model serving ඉගෙන ගන්න FastAPI හොඳයි, මොකද එය ලබාදෙනවා:

    simple Python syntax
    automatic API documentation
    request validation
    JSON request and response support
    Swagger UI

### Pydantic Schema

FastAPI Pydantic models use කරලා request සහ response data validate කරනවා.

මෙම lab එකේ:

    PredictionRequest
        API එක expect කරන input fields define කරනවා.

    PredictionResponse
        API එක return කරන response එක define කරනවා.

### Health Endpoint

Health endpoint එකක් API එක working ද කියලා check කරනවා.

මෙම lab එකේ health endpoint එක return කරනවා:

    API status
    model loaded ද
    expected feature count

### Prediction Endpoint

Prediction endpoint එක input values receive කරලා DataFrame එකක් හදනවා. පසුව ඒ data model එකට දාලා prediction එක return කරනවා.

## මෙම Lab එකේ Files

    requirements.txt
        Training සහ API serving සඳහා අවශ්‍ය Python packages.

    src/train_model.py
        Ridge Regression model එක train කරලා model files save කරන script එක.

    src/app.py
        Trained model එක serve කරන FastAPI application එක.

    models/
        Generated model files save වෙන folder එක.

    outputs/
        Generated training metrics save වෙන folder එක.

## Step 1: Virtual Environment එක Create කරන්න

Lab 03 folder එකේ සිට:

    python3.12 -m venv .venv
    source .venv/bin/activate

Python version එක check කරන්න:

    python --version

Expected:

    Python 3.12.x

## Step 2: Dependencies Install කරන්න

Run කරන්න:

    python -m pip install -r requirements.txt

ඔබගේ environment එකේ SSL certificate issue එකක් තිබුණොත්:

    python -m pip install \
      --trusted-host pypi.org \
      --trusted-host files.pythonhosted.org \
      --trusted-host pypi.python.org \
      -r requirements.txt

trusted-host option එක local learning environment එකකට temporary workaround එකක් විතරයි.

## Step 3: Model එක Train කරන්න

Run කරන්න:

    python src/train_model.py

මෙම script එක:

    diabetes sample dataset එක load කරනවා
    Ridge Regression model එක train කරනවා
    model එක save කරනවා
    feature names save කරනවා
    training metrics save කරනවා

Expected output:

    Model training completed
    Model saved to: models/model.joblib
    Feature names saved to: models/feature_names.json
    Metrics saved to: outputs/training_metrics.json

## Step 4: Generated Files Verify කරන්න

Run කරන්න:

    ls -la models
    ls -la outputs

Expected files:

    models/model.joblib
    models/feature_names.json
    outputs/training_metrics.json

මෙම files lab එක run කරන විට locally generate වෙනවා.

Repo එකට commit කරන්න හොඳ නැහැ.

## Step 5: FastAPI Server එක Run කරන්න

Run කරන්න:

    python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8000

Expected output:

    Uvicorn running on http://127.0.0.1:8000

මෙම terminal එක open තියාගන්න.

API server එක මේ terminal එකේ run වෙනවා.

## Step 6: Swagger UI Open කරන්න

Browser එකේ open කරන්න:

    http://127.0.0.1:8000/docs

ඔබට automatic API documentation එක පේන්න ඕනේ.

ඔබට මේ endpoints පේන්න ඕනේ:

    GET /
    GET /health
    POST /predict

මෙම documentation එක FastAPI automatically generate කරනවා.

## Step 7: Health Endpoint Test කරන්න

අලුත් terminal එකක් open කරන්න.

Lab 03 folder එකට ගිහින් virtual environment activate කරන්න:

    cd labs/foundation/lab-03-fastapi-model-serving
    source .venv/bin/activate

Run කරන්න:

    curl http://127.0.0.1:8000/health

Expected response:

    {"status":"healthy","model_loaded":true,"feature_count":10}

මේකෙන් confirm වෙනවා:

    API එක run වෙනවා
    model එක load වෙලා තියෙනවා
    feature count එක correct

## Step 8: Prediction Endpoint Test කරන්න

Run කරන්න:

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

Package versions අනුව exact prediction value එක පොඩ්ඩක් වෙනස් වෙන්න පුළුවන්.

## ඔබ Prove කළ දේ

මෙම lab එක complete කළාම ඔබ prove කරනවා:

    trained ML model එකක් save කරන්න පුළුවන්
    FastAPI app එකකට saved model එක load කරන්න පුළුවන්
    API එකකට JSON input receive කරන්න පුළුවන්
    model එකට prediction generate කරන්න පුළුවන්
    API එක prediction JSON response එකක් විදිහට return කරන්න පුළුවන්

මේක model serving වල foundation එක.

## Common Issues

### Model file not found

මෙහෙම error එකක් ආවොත්:

    Model file not found

Run කරන්න:

    python src/train_model.py

ඊට පස්සේ API එක නැවත start කරන්න.

### Port 8000 already in use

Port 8000 busy නම් වෙන port එකක් use කරන්න:

    python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8001

ඊට පස්සේ open කරන්න:

    http://127.0.0.1:8001/docs

### API connect වෙන්නේ නැහැ

Uvicorn තාම run වෙනවාද බලන්න.

Uvicorn run වෙන terminal එක open තියාගන්න ඕනේ.

### Validation error

Prediction endpoint එක validation error එකක් return කළොත්, input fields 10ම include කරලා තියෙනවාද බලන්න:

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

API server එක stop කරන්න:

    CTRL + C

Generated files remove කරන්න:

    rm -f models/model.joblib
    rm -f models/feature_names.json
    rm -f outputs/training_metrics.json

Python cache remove කරන්න:

    rm -rf src/__pycache__

Optional:

    rm -rf .venv

Full cleanup guide එක:

    cleanup.md

## ඔබ ඉගෙන ගත්ත දේ

ඔබ ඉගෙන ගත්තා:

    model එකක් train කරලා save කිරීම
    FastAPI application එකක model එක load කිරීම
    health සහ prediction endpoints create කිරීම
    curl වලින් API test කිරීම
    Swagger UI use කිරීම
    model prediction JSON response එකක් විදිහට return කිරීම

## Previous Labs සමඟ සම්බන්ධය

Lab 00:

    Basic ML workflow එක ඉගෙන ගත්තා.

Lab 01:

    MLflow experiment tracking ඉගෙන ගත්තා.

Lab 02:

    Dockerized ML training ඉගෙන ගත්තා.

Lab 03:

    FastAPI model serving ඉගෙන ගත්තා.

## Next Lab

Next lab එක local model artifact management ගැන focus කරනවා.

ඒ lab එකෙන් model files සහ related metadata organize කරන ආකාරය improve කරනවා.
