#!/bin/sh
AI_API_ENDPOINT_NAME=$AI_API_ENDPOINT_NAME

uvicorn handlers.${AI_API_ENDPOINT_NAME}:app --host 0.0.0.0 --port 8080 --workers 1