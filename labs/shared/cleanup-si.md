# පොදු Cleanup Guide

මෙම guide එකෙන් labs වල cleanup process එක explain කරයි.

Cleanup කියන්නේ MLOps practice වල වැදගත් කොටසක්. ඒකෙන් local machine එක clean තියාගන්න සහ unnecessary resource usage අඩු කරගන්න පුළුවන්.

## Cleanup වැදගත් ඇයි?

MLOps labs වලදී local resources create වෙන්න පුළුවන්.

Examples:

    Docker containers
    Docker images
    Docker volumes
    Docker networks
    Python virtual environments
    temporary files
    model artifacts
    MLflow run data
    local Kubernetes clusters

මේවා remove නොකළොත් machine එක messy වෙන්න පුළුවන්.

Cleanup උදව් කරන්නේ:

    port conflicts avoid කරන්න
    disk space free කරන්න
    labs අතර confusion අඩු කරන්න
    old files new labs වලට බලපාන එක avoid කරන්න
    labs repeatable තියාගන්න

## Clean Lab Principle

හැම lab එකක්ම clean හෝ minimal state එකකින් පටන් ගන්න ඕනේ.

Previous lab එකේ resources තවම තියෙනවා කියලා assume කරන්න හොඳ නැහැ.

New lab එකක් පටන් ගන්න කලින් previous lab එකේ cleanup steps තිබුණොත් ඒවා run කරන්න.

## Common Docker Cleanup Commands

Docker Compose වලින් create කරපු services stop සහ remove කරන්න:

    docker compose down

Docker Compose services සහ named volumes remove කරන්න:

    docker compose down -v

Running containers list කරන්න:

    docker ps

All containers list කරන්න:

    docker ps -a

Docker volumes list කරන්න:

    docker volume ls

Docker networks list කරන්න:

    docker network ls

## Important Warning

Global cleanup commands carefulව use කරන්න.

මේ commands වෙන projects වල resources remove කරන්න පුළුවන්:

    docker system prune
    docker volume prune
    docker network prune

මේ commands run කරන්න කලින් ඒවා remove කරන දේවල් තේරුම් ගන්න.

Lab guides වලදී project-specific cleanup commands use කිරීම වඩා හොඳයි.

## Common Local File Cleanup

සමහර labs local folders create කරන්න පුළුවන්.

Examples:

    mlruns
    mlartifacts
    artifacts
    outputs
    reports
    tmp

Lab එකක් generated files remove කරන්න මෙවැනි commands කියන්න පුළුවන්:

    rm -rf mlruns
    rm -rf mlartifacts
    rm -rf outputs
    rm -rf reports

rm -rf command එක carefulව use කරන්න.

Delete command එකක් run කරන්න කලින් path එක හරියට බලන්න.

## Kubernetes Cleanup

Later labs වලදී kind හෝ k3d භාවිතා කරලා local Kubernetes clusters create කරන්න පුළුවන්.

kind cluster එකක් delete කරන්න:

    kind delete cluster --name <cluster-name>

k3d cluster එකක් delete කරන්න:

    k3d cluster delete <cluster-name>

kind clusters list කරන්න:

    kind get clusters

k3d clusters list කරන්න:

    k3d cluster list

## Port Conflicts

Lab එකක් fail වෙලා port already in use කියලා error එකක් ආවොත්, වෙන service එකක් තවම run වෙමින් තිබිය හැක.

Common ports:

    5000  MLflow
    8000  FastAPI
    9000  MinIO API
    9001  MinIO Console
    9090  Prometheus
    3000  Grafana

macOS හෝ Linux වල port එකක් check කරන්න:

    lsof -i :5000

ඊට පස්සේ ඒ port එක use කරන service එක stop කරන්න.

## Recommended Cleanup Flow

Lab එකක් අවසන් වූ පසු:

    1. Lab services stop කරන්න
    2. Lab-specific volumes remove කරන්න
    3. Generated artifacts remove කරන්න
    4. Containers stopped ද කියලා verify කරන්න
    5. Next lab එක cleanව start වෙනවාද බලන්න

## Cost Note

Local cleanup disk space save කරන්න සහ confusion අඩු කරන්න උදව් වෙනවා.

Cloud extension labs වල cleanup තවත් වැදගත්. Cloud resources run වෙලා තිබුණොත් cost එකක් එන්න පුළුවන්.

Cloud lab එකක තිබිය යුතු දේවල්:

    created resources
    cleanup commands
    verification commands
    cost warning

## Final Reminder

Cleanup optional දෙයක් නෙවෙයි.

හොඳ MLOps workflow එකක් repeatable, understandable, සහ reset කරන්න ලේසි වෙන්න ඕනේ.
