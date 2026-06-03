# Cost-minimizing Architecture - සිංහල Guide

මෙම document එකෙන් project එකේ cost අඩු කරන architecture approach එක explain කරයි.

MLOps ඉගෙන ගන්නකොට cloud services භාවිතා කළොත් cost එක ඉක්මනින් වැඩි වෙන්න පුළුවන්. Managed Kubernetes, cloud databases, object storage, monitoring tools, GPU instances වගේ දේවල් වැරදි විදිහට run කරලා තියලා දැම්මොත් bill එකක් එන්න පුළුවන්.

ඒ නිසා මෙම project එකේ default rule එක මෙයයි:

```text
Core learning path එකට cloud cost එකක් තිබිය යුතු නැහැ.
Cost philosophy

Default learning path එක local machine එකේ run වෙන්න ඕනේ.

Learnerට අවශ්‍ය වන්නේ:

laptop එකක් හෝ local workstation එකක්
Docker
Python
Git
open-source tools

Cloud account එකක් main labs සඳහා අවශ්‍ය නොවිය යුතුයි.

Default local architecture
Local Machine
│
├── Git
│   └── source code සහ documentation
│
├── Python
│   └── training, inference, testing
│
├── Docker Compose
│   ├── MLflow tracking server
│   ├── MinIO object storage
│   ├── FastAPI model service
│   ├── Prometheus
│   ├── Grafana
│   └── Evidently reports
│
└── Optional local Kubernetes
    ├── kind
    └── k3d
Tool choices සහ cost reason
MLflow

MLflow localව run කරනවා.

එයින් learnerට ඉගෙන ගන්න පුළුවන්:

experiment tracking
parameters
metrics
artifacts
model comparison

Cloud managed ML platform එකක් මුලින්ම use කළොත් cost එකක් එන්න පුළුවන්. ඒ නිසා මුලින් local MLflow හොඳයි.

MinIO

MinIO local object storage එකක් විදිහට use කරනවා.

Production වල S3, Azure Blob Storage, Google Cloud Storage වගේ object storage use කරනවා. නමුත් learning phase එකේ MinIO use කරලා ඒ concept එක localව practice කරන්න පුළුවන්.

Docker සහ Docker Compose

Docker use කරන්නේ services localව isolated විදිහට run කරන්න.

Docker Compose use කරන්නේ multiple services එකට run කරන්න.

උදාහරණ:

MLflow + MinIO + FastAPI

මේවා cloud VMs වල run කරනවා වෙනුවට laptop එකේ Docker containers විදිහට run කරන නිසා cost අඩුයි.

kind සහ k3d

Kubernetes ඉගෙන ගන්න managed cloud Kubernetes cluster එකක් අවශ්‍ය නැහැ.

kind හෝ k3d use කරලා local Kubernetes cluster එකක් create කරන්න පුළුවන්.

ඒකෙන් Kubernetes concepts ඉගෙන ගන්න පුළුවන්:

deployment
service
pod
port-forwarding
cleanup
Prometheus සහ Grafana

Monitoring concepts ඉගෙන ගන්න paid monitoring platform එකක් අවශ්‍ය නැහැ.

Prometheus metrics collect කරනවා. Grafana dashboards පෙන්වනවා.

මෙය localව run කරන්න පුළුවන්.

Avoid කළ යුතු cost risks

Main learning path එකේදී avoid කරන්න ඕනේ:

managed Kubernetes clusters
always-on virtual machines
managed databases
cloud GPUs
paid observability tools
public cloud load balancers
large cloud storage buckets
unnecessary CI/CD runs
Cloud use කරනවා නම් rules

Cloud labs later optional විදිහට add කළොත්, හැම cloud lab එකකම පහත දේවල් තිබිය යුතුයි:

estimated cost
create කරන resources list එක
cleanup commands
cleanup verify කරන commands
long-running resource warning
Cleanup mindset

Cost minimize කරන්න cleanup අනිවාර්යයි.

Local cleanup examples:

docker compose down -v
docker container prune
docker network prune
kind delete cluster --name <cluster-name>
k3d cluster delete <cluster-name>
rm -rf mlruns
rm -rf artifacts/*

Cloud cleanup examples later add කළ යුතුයි:

delete cluster
delete storage bucket
delete database
delete container registry image if needed
verify billing resources
Local to cloud mapping

Localව ඉගෙන ගන්න දේ cloud එකට map වෙන්නේ මෙහෙමයි:

Local MLflow              -> managed tracking or cloud-hosted MLflow
Local MinIO               -> S3 / Azure Blob / GCS
Local Docker              -> container registry + cloud runtime
Local kind/k3d            -> managed Kubernetes
Local Prometheus/Grafana  -> managed or self-hosted monitoring
Final rule

Learner කෙනෙක් core MLOps concepts ඉගෙන ගන්න paid cloud account එකක් අවශ්‍ය නොවිය යුතුයි.

Cloud යනු main learning path එක නොව, optional advanced extension එකක් පමණයි.
