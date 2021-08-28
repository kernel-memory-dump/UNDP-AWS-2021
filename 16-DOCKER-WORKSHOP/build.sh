DOCKER_USERNAME="kernelmemorydump2"
DOCKER_PASSWORD=""
# exit when any command fails
set -e

docker login --username=$DOCKER_USERNAME --password=$DOCKER_PASSWORD

docker build -t undp-angular:$1 .
docker tag undp-angular:$1 kernelmemorydump2/undp-angular-example:$1
docker push kernelmemorydump2/undp-angular-example:$1
