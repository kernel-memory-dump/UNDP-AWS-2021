DOCKER_USERNAME="kernelmemorydump2"
DOCKER_PASSWORD="j5rwLX,~K-9~JW_"
# exit when any command fails
set -e

docker login --username=$DOCKER_USERNAME --password=$DOCKER_PASSWORD

docker build -t undp-angular .
docker tag undp-angular:$1 kernelmemorydump2/undp-angular-example:$1
docker push kernelmemorydump2/undp-angular-example:$1
