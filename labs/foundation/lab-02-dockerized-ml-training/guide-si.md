# Guide - Foundation Lab 02: Dockerized ML Training

## මෙම Lab එකෙන් ඉගෙන ගන්න දේ

මෙම lab එකෙන් machine learning training workflow එකක් Docker container එකක් ඇතුළේ run කරන ආකාරය ඉගෙන ගන්නවා.

ඔබට ඉගෙන ගන්න පුළුවන්:

    MLOps වල Docker වැදගත් ඇයි
    ML training වල Docker solve කරන problem එක මොකක්ද
    Dockerfile කියන්නේ මොකක්ද
    Docker image කියන්නේ මොකක්ද
    Docker container කියන්නේ මොකක්ද
    Docker image build කරන්නේ කොහොමද
    container එකක් ඇතුළේ model training run කරන්නේ කොහොමද
    model outputs local machine එකට save කරන්නේ කොහොමද
    Docker image සහ generated files cleanup කරන්නේ කොහොමද

මෙම lab එක Lab 00 සහ Lab 01 මත build වෙනවා.

Lab 00 එකෙන් basic ML workflow එක ඉගෙන ගත්තා.

Lab 01 එකෙන් MLflow භාවිතා කරලා experiment tracking ඉගෙන ගත්තා.

Lab 02 එකෙන් Docker භාවිතා කරලා training environment එක repeatable කරන්නේ කොහොමද කියලා ඉගෙන ගන්නවා.

## මෙම Lab එක MLOps Lifecycle එකේ කොතනද?

මෙම lab එක MLOps lifecycle එකේ reproducible training environment stage එකට අදාළයි.

Simple MLOps lifecycle එකක් මෙහෙමයි:

    Data understanding
        |
        v
    Basic model training
        |
        v
    Experiment tracking
        |
        v
    Reproducible training environment
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

    reproducible training environment
    dependency packaging
    containerized training
    output persistence

මෙම lab එකේ model deploy කරන්නේ නැහැ.

මෙම lab එකේ Kubernetes හෝ cloud services භාවිතා කරන්නේ නැහැ.

ඒ topics පසුව labs වලදී ඉගෙන ගන්නවා.

## මෙම Lab එක වැදගත් ඇයි?

Machine learning projects වල common real-world problem එකක් තියෙනවා:

    Training script එක එක machine එකක වැඩ කරනවා.
    වෙන machine එකක fail වෙනවා.

මෙයට හේතු විය හැක:

    Python version වෙනස්
    package versions වෙනස්
    dependencies missing
    operating system වෙනස්
    local setup වෙනස්

මේකට බොහෝ විට කියන්නේ:

    works on my machine problem

MLOps වලදී මෙය dangerous.

Training workflow එක එක් පුද්ගලයෙකුගේ laptop එකට විතරක් depend වෙන්න හොඳ නැහැ.

Same workflow එක run වෙන්න ඕනේ:

    වෙන developer කෙනෙක්ගේ laptop එකේ
    training server එකක
    CI pipeline එකක
    scheduled job එකක
    production-like environment එකක

Docker training environment එක package කරලා more consistentව run කරන්න උදව් කරනවා.

## Real-world Business Example

Retail company එකක් weekly sales prediction model එක train කරනවා කියලා හිතන්න.

Data scientist කෙනෙක්ගේ laptop එකේ model training success වෙනවා.

පසුව ML engineer කෙනෙක්ට same training workflow එක වෙන server එකක run කරන්න වෙනවා.

Server එකේ:

    Python version වෙනස්
    packages missing
    package versions වෙනස්

Training script එක fail වෙනවා.

මෙයින් project එක delay වෙන්න පුළුවන්.

Docker භාවිතා කළොත් team එකට training environment එක once define කරන්න පුළුවන්:

    Python version
    required packages
    source code
    run command

ඊට පස්සේ same Docker image එක use කරලා training workflow එක more consistently run කරන්න පුළුවන්.

## Key Concepts

### Dockerfile

Dockerfile එකක් කියන්නේ Docker image එක build කරන ආකාරය describe කරන text file එකක්.

ඒක define කරන දේවල්:

    base image
    working directory
    copy කරන files
    install කරන packages
    default run command

මෙම lab එකේ Dockerfile එක use කරන්නේ:

    python:3.12-slim

ඒ කියන්නේ ඔබගේ laptop එකේ Python version එක වෙනස් වුණත් container එකේ Python 3.12 use වෙනවා.

### Docker Image

Docker image එකක් කියන්නේ packaged environment එකක්.

ඒකේ තියෙනවා:

    Python runtime
    installed dependencies
    training code
    default command

Image එක reusable training package එකක් වගේ හිතන්න.

මෙම lab එකේ image name එක:

    mlops-lab-02-training:latest

### Docker Container

Container එකක් කියන්නේ image එක run වෙන instance එකක්.

Image එක run කළාම Docker container එකක් start වෙනවා.

මෙම lab එකේ container එක run කරන්නේ:

    python src/train.py

Training ඉවර වුනාම container එක stop වෙනවා.

මෙම lab එක use කරනවා:

    --rm

ඒ නිසා container එක finish වුනාම automatically remove වෙනවා.

### Volume Mount

Container එක temporary.

Model output එක container එක ඇතුළේ විතරක් save කළොත් container එක stop වූ පසු ඒ output නැතිවෙන්න පුළුවන්.

Volume mount එකක් local folder එකක් container folder එකකට connect කරනවා.

මෙම lab එකේ:

    local outputs/ folder
        connect වෙනවා
    container /app/outputs folder එකට

Command එක:

    -v "$(pwd)/outputs:/app/outputs"

මේකෙන් container එක ඇතුළේ training script එක save කරන files local machine එකේ outputs folder එකට save වෙනවා.

## මෙම Lab එකෙන් Build කරන දේ

මෙම lab එක Dockerized training workflow එකක් build කරනවා.

Workflow එක:

    Docker image build කරනවා
    Python dependencies image එක ඇතුළේ install කරනවා
    training script image එකට copy කරනවා
    training script container එකක් ඇතුළේ run කරනවා
    model outputs local outputs folder එකට save කරනවා

## Local Architecture

    Dockerfile
        |
        v
    Docker image
        |
        v
    Docker container
        |
        v
    Training script runs inside container
        |
        v
    /app/outputs inside container
        |
        v
    outputs/ folder on local machine

වැදගත් idea එක:

    Training Docker ඇතුළේ run වෙනවා.
    Outputs local machine එකේ save වෙනවා.

## මෙම Lab එකේ Files

    Dockerfile
        Container training environment එක define කරනවා.

    requirements.txt
        Image එක ඇතුළේ install කරන Python packages.

    src/train.py
        Container එක ඇතුළේ run වෙන training script එක.

    outputs/
        Generated files save වෙන local folder එක.

## Output Files

Container එක run කළාට පස්සේ මෙම files create වෙනවා:

    outputs/dockerized_metrics.json
        Model performance metrics.

    outputs/dockerized_predictions.csv
        Sample predictions.

    outputs/runtime_environment.json
        Container එක ඇතුළේ runtime details.

    outputs/model/dockerized_model.joblib
        Saved trained model file.

## Step 1: Lab Folder එකට යන්න

Repository root එකේ සිට:

    cd labs/foundation/lab-02-dockerized-ml-training

## Step 2: Docker Image එක Build කරන්න

Run කරන්න:

    docker build -t mlops-lab-02-training:latest .

මෙම command එක Dockerfile එකෙන් Docker image එක build කරනවා.

Image name එක:

    mlops-lab-02-training

Tag එක:

    latest

අවසානයේ තියෙන dot එකෙන් අදහස් වෙන්නේ:

    current folder එක Docker build context එක ලෙස use කරන්න

## Step 3: Container එක ඇතුළේ Training Run කරන්න

Run කරන්න:

    docker run --rm \
      -v "$(pwd)/outputs:/app/outputs" \
      mlops-lab-02-training:latest

මෙම command එක image එකෙන් container එකක් start කරනවා.

Container එක training script එක run කරනවා.

වැදගත් parts:

    --rm
        Container එක finish වූ පසු automatically remove කරනවා.

    -v "$(pwd)/outputs:/app/outputs"
        Local outputs folder එක container එකට mount කරනවා.

    mlops-lab-02-training:latest
        Run කරන Docker image එක.

## Step 4: Training Output Check කරන්න

Expected terminal output:

    Dockerized training completed
    Python version: 3.12.x
    scikit-learn version: ...
    Training rows: 353
    Test rows: 89
    Feature count: 10
    RMSE: 55.4745
    MAE : 46.1389
    R2  : 0.4192

Package versions අනුව exact values පොඩ්ඩක් වෙනස් වෙන්න පුළුවන්.

## Step 5: Local Output Files Verify කරන්න

Run කරන්න:

    ls -la outputs
    ls -la outputs/model

පහත files පේන්න ඕනේ:

    dockerized_metrics.json
    dockerized_predictions.csv
    runtime_environment.json
    model/dockerized_model.joblib

Model metrics බලන්න:

    cat outputs/dockerized_metrics.json

Runtime environment බලන්න:

    cat outputs/runtime_environment.json

Sample predictions බලන්න:

    head outputs/dockerized_predictions.csv

## Runtime Environment File එකෙන් පේන දේ

File එක:

    outputs/runtime_environment.json

මෙම file එකෙන් container එක ඇතුළේ environment details පෙන්වනවා.

Examples:

    Python version
    platform
    scikit-learn version
    running_inside_container

මෙය වැදගත් වෙන්නේ training run වුනේ ඔබගේ laptop Python environment එකේ නොව Docker environment එක ඇතුළේ බව prove කරන නිසා.

## ඔබ Generate කළ Result එක මොකක්ද?

මෙම lab එක අවසානයේ ඔබ generate කරන්නේ:

    Docker image එකක්
    containerized training run එකක්
    saved model file එකක්
    model metrics
    sample predictions
    runtime environment details

ඒ කියන්නේ ඔබ Dockerized ML training workflow එකක් complete කරලා තියෙනවා.

## Real MLOps වලට මෙය වැදගත් ඇයි?

Dockerized training teams වලට ML workflows repeatable කරන්න උදව් කරනවා.

එය මේ ප්‍රශ්න වලට answer දෙන්න උදව් කරනවා:

    මොන Python version එක use කළාද?
    මොන packages install වෙලා තිබුණාද?
    වෙන කෙනෙක්ට same training workflow එක run කරන්න පුළුවන්ද?
    මේ training run එක later CI එකක හෝ training server එකක run කරන්න පුළුවන්ද?
    outputs temporary container එකෙන් පිටත save වෙනවාද?

මෙය production-like MLOps workflows වලට යන්න පෙර වැදගත් step එකක්.

## Common Issues

### Docker run වෙන්නේ නැහැ

මෙහෙම error එකක් ආවොත්:

    Cannot connect to the Docker daemon

Docker Desktop start කරලා නැවත try කරන්න.

Check කරන්න:

    docker ps

### Docker command not found

මෙහෙම error එකක් ආවොත්:

    docker: command not found

Docker install කරලා නැතිවිය හැක හෝ terminal PATH එකේ නැතිවිය හැක.

Docker Desktop install කරලා new terminal එකක් open කරන්න.

### Linux permission issue

Linux වල Docker permission error එකක් ආවොත්, temporary check එකක් ලෙස:

    sudo docker ps

Long-term fix එකක් ලෙස user Docker group එකට add කරන්න පුළුවන්.

### outputs folder එක empty

Container එක run උනත් outputs missing නම් volume mount එක check කරන්න:

    -v "$(pwd)/outputs:/app/outputs"

Docker run command එක Lab 02 folder එකේ සිට run කරනවාද බලන්න.

Current folder එක check කරන්න:

    pwd

Expected path එක අවසන් වෙන්න ඕනේ:

    labs/foundation/lab-02-dockerized-ml-training

### Image already exists

Image එක නැවත build කරනකොට Docker cached layers reuse කරන්න පුළුවන්.

ඒක normal.

Cache නැතුව rebuild කරන්න:

    docker build --no-cache -t mlops-lab-02-training:latest .

### Docker image remove කිරීම

Image එක remove කරන්න:

    docker rmi mlops-lab-02-training:latest

Image එක නැත්නම් Docker error එකක් පෙන්වන්න පුළුවන්. ඒක අවුලක් නැහැ.

## Cleanup

Cleanup guide එක බලන්න:

    cleanup.md

Basic cleanup commands:

    docker rmi mlops-lab-02-training:latest

    rm -rf outputs
    mkdir -p outputs
    touch outputs/.gitkeep

මෙම lab එක use කරන්නේ:

    --rm

ඒ නිසා training run ඉවර වූ පසු container එක automatically remove වෙනවා.

## Cost Note

මෙම lab එක Docker භාවිතා කරලා localව run වෙනවා.

Expected cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, Docker image storage, and disk usage

## ඔබ ඉගෙන ගත්ත දේ

මෙම lab එකෙන් ඔබ ඉගෙන ගත්තා:

    ML training සඳහා Dockerfile එකක් ලිවීම
    Docker image එකක් build කිරීම
    container එකක් ඇතුළේ training script run කිරීම
    local outputs folder එක container එකට mount කිරීම
    model outputs container එකෙන් පිටත save කිරීම
    runtime environment details verify කිරීම
    Docker image සහ generated outputs cleanup කිරීම

## Previous Labs සමඟ සම්බන්ධය

Lab 00:

    Basic ML workflow එක ඉගෙන ගත්තා.

Lab 01:

    MLflow වලින් model experiments track කරන ආකාරය ඉගෙන ගත්තා.

Lab 02:

    Training workflow එක Docker container එකක් ඇතුළේ run කරන ආකාරය ඉගෙන ගත්තා.

## Next Lab සමඟ සම්බන්ධය

Next lab එකෙන් FastAPI model serving ඉගෙන ගන්නවා.

ඒ lab එකේදී saved model එක load කරලා API එකක් හරහා predictions return කරන ආකාරය ඉගෙන ගන්නවා.

Simple connection:

    Lab 02 = Docker වලින් training package/run කිරීම
    Lab 03 = trained model එක API එකක් විදිහට serve කිරීම
