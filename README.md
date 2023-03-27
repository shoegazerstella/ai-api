# AI API

This project uses [FastAPI](https://fastapi.tiangolo.com/) to serve AI models as APIs.

## Project Structure

To start a new project you just need to add your custom scripts to the repo.
Please respect the naming conventions and format, in order for your project to run smoothly.
Here's a simplified overview of the structure `sentiment`:

```bash
Dockerfiles/
    sentiment

workers/
    sentiment/
        worker.py
        requirements.txt

config_models/
    sentiment.py

handlers/
    sentiment.py
```

## Getting started with a new project 

Please refer to the project `sentiment` to have a reference template to work with.

* add your custom Dockerfile in `Dockerfiles/`
* add your custom worker in `workers/`, by creating a new directory
* add your model config in `config_models/`, by creating a new .py file
* add your custom handler in  `handlers/`

## Setup the API

Build and run the api

```bash
# build and enter the container
export AI_API_ENDPOINT_NAME=sentiment
sh build_and_run.sh $AI_API_ENDPOINT_NAME

# start the server
sh ./server/uvicorn.sh

# call it
curl http://127.0.0.1:8080

curl -X POST http://127.0.0.1:8080/sentiment \
    -H "Content-Type: application/json" \
    -d '{"input": "I am very happy today!"}' 
```

## API Documentation
FastAPI automagically generates a documentation for your API
```bash
http://127.0.0.1:8080/docs
```

## Add gunicorn
Refer to this repo [https://github.com/loretoparisi/dserve](https://github.com/loretoparisi/dserve) to add support for gunicorn.
