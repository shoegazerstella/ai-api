AI_API_ENDPOINT_NAME=$AI_API_ENDPOINT_NAME

echo "Building \"$AI_API_ENDPOINT_NAME\" "

docker build -t ${AI_API_ENDPOINT_NAME} --build-arg AI_API_ENDPOINT_NAME=$AI_API_ENDPOINT_NAME -f Dockerfiles/${AI_API_ENDPOINT_NAME} .
docker run -it \
    -p 8080:8080 \
    ${AI_API_ENDPOINT_NAME} \
    bash