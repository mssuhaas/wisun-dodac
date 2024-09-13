# Dodac Api to send wisun status from border router.
The deployment setup involves using Docker, Fast API a python library. Docker enables containerization, packaging applications and dependencies into isolated units. Fast APT enables the user to create API endpoints to expose data to other services.

## Table of contents
- [Dodac Api to send wisun status from border router.](#dodac-api-to-send-wisun-status-from-border-router)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Setup and Run](#setup-and-run)
    - [Configuration](#configuration)
  - [Maintainers](#maintainers)


## Introduction
The API endpoints uses the Wi-SUN DBus to get the border router connections.
- For API Documentation, visit the
  - [Swagger Docs](http://localhost:8000/swagger).
  - [Redoc Docs](http://localhost:8000/redoc).

## Requirements
This module requires the following modules:
- [Requirements File](requirements.txt) clearly states all the required python modules for the project.

## Setup and Run
Install as you would normally install a FastAPI project for more info visit [Fast API](https://fastapi.tiangolo.com/) documentation.
Gunicorn will be needed to be used in production which is already supported.
- Clone repository in the Wi-SUN Border Router. 
- Navigate to cloned repository in the Border Router.
- Follow the below steps [Configure](#configuration) to set it up

### Configuration
- Install Create Virtual Environment and install requirements from "requirements.txt" using
```bash 
pip install -r requirements.txt
```
<!-- - Create a ".env" file from "[.env.example](.env.example)" template. or Add your environment variables as in the example file -->
- Gunicorn is ASGI runtime to serve the API in production
- Deploy the application using gunicorn with the provided configuration file (gunicorn_conf.py) using the below command.
```sh
gunicorn -c gunicorn_conf.py &
```


## Maintainers

Current maintainers:
- Surya Suhaas Modadugu [(Surya Suhaas)](mailto:mssuhaas@gmail.com)

Original maintainer:
- Leo Jesvyn Francis [(leojfrancis)](mailto:leojfrancis.now@gmail.com)

