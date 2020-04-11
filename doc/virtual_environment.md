# Virtual Environment

## pipenv

> It's recommended use _pipenv_ instead of _virtualenv_

It's needed to have installed, python 2.7+ and pip.

1. Install

   ![](https://img.shields.io/badge/python-2.7|>=3.5-informational)
   ![](https://img.shields.io/badge/pip-20.0-informational)

   ```
   pip install pipenv
   ```

1. Use

   1. Generate

      ```
      pipenv --python <version>
      ```

   1. Activate

      ```
      pipenv shell
      ```

   1. Deactivate

      ```
      exit
      ```

   1. Installing PIP Project Dependencies

      > With Pipfile

      ```
      pip install
      ```

      > With requeriment.txt

      ```
      pip install -r requirements.txt
      ```

      ```

      ```

   1. More info -> [HERE](https://github.com/pypa/pipenv)

## virtualenv

1. Install

   ```
      apt-get update
      apt-get install virtualenv
   ```

1. Use

   1. Generate

      ```
      virtualenv venv
      ```

      Optional you can use a specific interpreter

      ```
      virtualenv --python=/usr/bin/python3 venv
      ```

   1. Activate

      ```
      source venv/bin/activate
      ```

   1. Deactivate

      ```
      deactivate
      ```

   1. Installing PIP Project Dependencies

      > With virtualenv activated

      ```
      pip install -r requirements.txt
      ```
