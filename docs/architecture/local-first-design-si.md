# Local-first Design - සිංහල Guide

මෙම project එකේ ප්‍රධාන අදහස වන්නේ MLOps concepts local machine එකේ practice කරන්න පුළුවන් විදිහට design කිරීමයි.

සරලව කිව්වොත්, learner කෙනෙක්ට cloud account එකක්, paid Kubernetes cluster එකක්, managed database එකක් නැතුව MLOps ඉගෙන ගන්න පුළුවන් වෙන්න ඕනේ.

## Local-first කියන්නේ මොකක්ද?

Local-first කියන්නේ මුලින්ම හැම දෙයක්ම laptop එකේ හෝ local workstation එකේ run කරන approach එකක්.

උදාහරණ:

- MLflow local machine එකේ run කිරීම
- MinIO local object storage එකක් විදිහට run කිරීම
- FastAPI model service එක local Docker container එකක් විදිහට run කිරීම
- Kubernetes ඉගෙන ගන්න kind හෝ k3d භාවිතා කිරීම
- Monitoring සඳහා Prometheus සහ Grafana localව run කිරීම

Cloud services පසුව optional extension එකක් විදිහට add කරන්න පුළුවන්. නමුත් main learning path එක cloud මත depend වෙන්න හොඳ නැහැ.

## ඇයි Local-first වැදගත්?

MLOps ඉගෙන ගන්නකොට learnersලාට ගොඩක් වෙලාවට tools, services, cloud cost, architecture කියන දේවල් එකවරම confusing වෙනවා.

Local-first approach එකෙන් learnerට පහත වාසි ලැබෙනවා:

- cloud bill එකක් ගැන බය නැතුව practice කරන්න පුළුවන්
- lab එකක් නැවත නැවත run කරන්න පුළුවන්
- tool එක ඇත්තටම කරන වැඩේ තේරුම් ගන්න ලේසි
- වැරදි උනත් localව fix කරන්න පුළුවන්
- cloud platform එකකට යන්න කලින් confidence එක build වෙනවා

## මෙම project එකේ Local-first principles

### 1. මුලින් local

Default labs local machine එකේ run වෙන්න ඕනේ.

Preferred tools:

- Docker
- Docker Compose
- Python virtual environment
- MLflow
- MinIO
- FastAPI
- Prometheus
- Grafana
- Evidently
- kind
- k3d

### 2. Clean labs

හැම lab එකක්ම clean state එකකින් පටන් ගන්න ඕනේ.

Lab එකක් කලින් lab එකකින් ඉතිරි උන resource එකක් මත depend වෙන්න හොඳ නැහැ.

උදාහරණයක් විදිහට lab එකක් මෙහෙම assume කරන්න හොඳ නැහැ:

```text
කලින් lab එකේ MLflow server එක තවම run වෙනවා කියලා assume කිරීම
කලින් create කරපු MinIO bucket එක use කිරීම
කලින් kind cluster එක තියෙනවා කියලා assume කිරීම

ඒ වෙනුවට lab එකට අවශ්‍ය resources එම lab එකේම create කරන්න ඕනේ.

3. Cleanup අනිවාර්යයි

හැම lab එකකම cleanup section එකක් තිබිය යුතුයි.

Cleanup වලින් remove කරන්න ඕනේ දේවල්:

Docker containers
Docker volumes
Docker networks
Kubernetes clusters
generated model files
temporary artifacts
local logs
4. එක lab එකකට එක main concept එකක්

Beginner lab එකකට tools ගොඩක් එකවර දාන්න හොඳ නැහැ.

උදාහරණයක්:

හොඳ lab design එකක්:

Lab 01: MLflow experiment tracking only
Lab 02: Dockerized training only
Lab 03: FastAPI serving only

අමාරු lab design එකක්:

එකම lab එකේ MLflow + MinIO + PostgreSQL + Kubernetes + Prometheus + Grafana

Learnerට concept එක තේරුම් ගන්න නම් complexity එක step by step වැඩි කරන්න ඕනේ.

Simple Local Architecture
Developer Laptop
│
├── Git repository
│
├── Python environment
│   ├── training scripts
│   ├── inference scripts
│   └── tests
│
├── Docker / Docker Compose
│   ├── MLflow
│   ├── MinIO
│   ├── FastAPI
│   ├── Prometheus
│   ├── Grafana
│   └── Evidently reports
│
└── Optional local Kubernetes
    ├── kind
    ├── k3d
    └── kubectl
Real-world mapping

Localව ඉගෙන ගන්න දේ production එකට map වෙන්නේ මෙහෙමයි:

Local MLflow        -> production experiment tracking
Local MinIO         -> cloud object storage
Local Docker        -> production container image
Local kind/k3d      -> managed Kubernetes concept
Local Prometheus    -> production monitoring concept
Local Grafana       -> dashboards
Final idea

මෙම project එකේ main goal එක වන්නේ learnerට commands run කරන්න විතරක් නොව, MLOps workflow එක ඇත්තටම තේරුම් ගන්න උදව් කිරීමයි.

Local-first design එකෙන් අපි cost අඩු කරනවා, complexity අඩු කරනවා, සහ practical learning experience එක වැඩි කරනවා.
