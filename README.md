# Boilerplate Python API

![](https://img.shields.io/badge/docker-19.03.6-informational)
![](https://img.shields.io/badge/docker--compose-1.24.1-informational)

The base project has MySQL 8 configured by default, if you need another database, configure it in the `dockerfile-compose` file.

## Install project (Development Environment)

You need to have `docker` & `docker-compose` in your system.

In root project path, run:

```
docker-compose -f docker-compose.dev.yml up -d --build
```

## Virtual Environment

[pipenv & virtualenv doc](doc/virtual_environment.md)

## .env File

In root project has a _.env_ file, its reason is to load the python path for vscode and thus not have file import errors in it.

### Project ENV vars

The environment variables of the project are established in the file _django/project/.env_. Said file will be ignored in the VCS for security reasons.

> This file has configuration for the MySQL engine in development use

## Errors

To facilitate the export of errors and codes that the API can return, a command has been generated that can comfortably export the errors to a markdown file. For this we must keep the file _django/project_api/errors.py_.

El fichero generado es [doc/errors.md](doc/errors.md)

>

> With virtual environment activated or in docker_container

```
python django/manage.py export_errors
```

## Internalization

> With virtual environment activated or in docker_container

```
python django/manage.py compilemessages
```

## Testing

### Dependencies (BDD Test) [Gecko Driver]

1. Go to the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases). Find the latest version of the driver for your platform and download it. For example:

   `wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`

1. Extract the file with:

   `tar -xvzf geckodriver*`

1. Make it executable:

   `chmod +x geckodriver`

1. Add the driver to your PATH so other tools can find it:

   `export PATH=$PATH:/path-to-extracted-file/.`

### Unit test with py.test

> With virtual environment activated and located in _django_ folder:

```
pytest django/project_api/test/ -sv
```

> The flags -s allows the capture of stdout and -v increases the verbosity of the results. For executing only some tests from a file:

```
pytest django/project_api/test/test_to_execute.py -sv
```

Generate html report:

```
pytest --cov-report html --cov-config=django/project_api/.coveragerc --cov=django/project_api django/project_api/test/
```

> The configuration file is indicated with --cov-config flag and ".coveragerc" file contains the path where the html report will be generated. The --cov flag indicates the directory where is located the functionality to test and the last element of the command is the root of the testing directory.

## SonarQube

This project uses sonar-scanner to analyze the code. Please change the name that appears on the first line to avoid overwriting data on the server.

[SonarQube Opinno](https://sonarqube.opinno.io/about)

[Sonar Scanner DOC](doc/install_sonar_scanner.md)
