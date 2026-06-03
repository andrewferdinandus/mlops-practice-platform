# MLOps Tool Map - සිංහල Guide

MLOps වල tools ගොඩක් තියෙනවා. Beginner කෙනෙක්ට මේක මුලදී confusing වෙන්න පුළුවන්.

Tools මතක තියාගන්න හොඳම විදිහ තමයි tool එක solve කරන problem එකට connect කරලා බලන එක.

## Simple Tool Map

    Problem: model experiments track කරන්න
    Tool: MLflow

    Problem: code සහ dependencies package කරන්න
    Tool: Docker

    Problem: local services කිහිපයක් එකට run කරන්න
    Tool: Docker Compose

    Problem: model එක API එකක් විදිහට serve කරන්න
    Tool: FastAPI

    Problem: model artifacts object storage වගේ save කරන්න
    Tool: MinIO

    Problem: Kubernetes localව practice කරන්න
    Tool: kind හෝ k3d

    Problem: service metrics collect කරන්න
    Tool: Prometheus

    Problem: dashboards බලන්න
    Tool: Grafana

    Problem: data drift සහ data quality check කරන්න
    Tool: Evidently

    Problem: code changes වලදී automation run කරන්න
    Tool: GitHub Actions

## MLflow

MLflow භාවිතා කරන්නේ machine learning experiments track කරන්න.

MLflow වල save කරන්න පුළුවන්:

    parameters
    metrics
    artifacts
    model information

MLflow වැදගත් වෙන්නේ මේ ප්‍රශ්න වලට answers ගන්න:

    හොඳම model එක මොකක්ද?
    මොන parameters use කළාද?
    artifacts කොහෙද?
    runs කිහිපයක් compare කරන්න පුළුවන්ද?

## Docker

Docker භාවිතා කරන්නේ code, dependencies, runtime settings package කරන්න.

Docker වැදගත් වෙන්නේ මේ ප්‍රශ්න වලට:

    මේ workflow එක වෙන machine එකක run කරන්න පුළුවන්ද?
    dependencies consistent ද?
    training හෝ serving code එක package කරන්න පුළුවන්ද?

Docker training workflows සහ serving workflows දෙකටම useful.

## Docker Compose

Docker Compose භාවිතා කරන්නේ containers කිහිපයක් එකට run කරන්න.

Example local stack එකක්:

    MLflow
    MinIO
    FastAPI
    Prometheus
    Grafana

Service එකකට තනිවම වැඩ කරන්න බැරි වෙලා services කිහිපයක් එකට connect වෙන්න ඕනේ නම් Docker Compose useful.

## FastAPI

FastAPI කියන්නේ Python වලින් APIs build කරන්න භාවිතා කරන tool එකක්.

MLOps වලදී FastAPI බොහෝ විට trained model එක serve කරන්න use කරනවා.

Example:

    input: customer details
    output: prediction

Application එකකට model එක call කරලා prediction එකක් ගන්න ඕනේ නම් FastAPI use කරන්න පුළුවන්.

## MinIO

MinIO කියන්නේ local object storage එකක්.

Cloud storage use නොකර object storage concept එක localව ඉගෙන ගන්න MinIO useful.

Production systems වල object storage සඳහා AWS S3, Azure Blob Storage, Google Cloud Storage වගේ services use කරන්න පුළුවන්.

Local practice වලදී MinIO වල store කරන්න පුළුවන්:

    model files
    reports
    datasets
    artifacts

## kind සහ k3d

kind සහ k3d භාවිතා කරන්නේ Kubernetes localව run කරන්න.

Managed cloud Kubernetes clusters cost වෙන්න පුළුවන්. ඒ නිසා Kubernetes concepts localව practice කරන්න kind හෝ k3d හොඳයි.

ඉගෙන ගන්න concepts:

    pods
    deployments
    services
    port forwarding
    local Kubernetes cleanup

## Prometheus

Prometheus භාවිතා කරන්නේ metrics collect කරන්න.

Model API එකකට Prometheus collect කරන්න පුළුවන් metrics:

    request count
    error count
    response time
    resource usage

Metrics වලින් service එක කාලයත් සමඟ behave වෙන ආකාරය තේරුම් ගන්න පුළුවන්.

## Grafana

Grafana භාවිතා කරන්නේ dashboards create කරන්න.

Prometheus metrics store කරනවා. Grafana ඒ metrics visual dashboards විදිහට පෙන්වනවා.

Grafana වලින් බලන්න පුළුවන්:

    API traffic
    latency trends
    error trends
    service health

## Evidently

Evidently භාවිතා කරන්නේ data quality සහ data drift analyze කරන්න.

Evidently වලින් compare කරන්න පුළුවන්:

    reference data
    current data

Input data වෙනස් වෙලාද කියලා තේරුම් ගන්න reports generate කරන්න Evidently useful.

## GitHub Actions

GitHub Actions භාවිතා කරන්නේ code changes වලදී automation run කරන්න.

Examples:

    tests run කිරීම
    formatting check කිරීම
    Docker image build කිරීම
    files validate කිරීම

Beginner level එකේදී GitHub Actions lightweight විදිහට use කිරීම හොඳයි.

## Tools එකට connect වෙන ආකාරය

Simple local MLOps workflow එකක් මෙහෙම වෙන්න පුළුවන්:

    Python වලින් model train කරනවා
        |
        v
    MLflow වලින් experiment track කරනවා
        |
        v
    model artifact save කරනවා
        |
        v
    FastAPI වලින් model serve කරනවා
        |
        v
    Docker වලින් service package කරනවා
        |
        v
    Prometheus සහ Grafana වලින් service monitor කරනවා
        |
        v
    Evidently වලින් data quality සහ drift check කරනවා

## Simple Summary

Tools ඔක්කොම එකවර ඉගෙන ගන්න උත්සාහ කරන්න එපා.

මුලින් problem එක තේරුම් ගන්න.

ඊට පස්සේ ඒ problem එක solve කරන tool එක ඉගෙන ගන්න.

Recommended order:

    MLflow
    Docker
    FastAPI
    MinIO
    Docker Compose
    Evidently
    Prometheus and Grafana
    kind or k3d
    GitHub Actions
