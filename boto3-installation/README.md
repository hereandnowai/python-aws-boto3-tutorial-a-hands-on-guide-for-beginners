# Boto3 installation

Folder contains sources for the [Boto3 installation](https://hands-on.cloud/course/boto3-installation) at [https://hands-on.cloud](https://hands-on.cloud).

Boto3 installation instructions:

```sh
export PROJECT_ROOT=$(git rev-parse --show-toplevel)

cd $PROJECT_ROOT

python3 -m venv $PROJECT_ROOT/.venv
source $PROJECT_ROOT/.venv/bin/activate
pip install --upgrade pip boto3
cd $PROJECT_ROOT/boto3-installation
python installation_test.py
```
