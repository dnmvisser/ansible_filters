#!/bin/sh

# Set up venv
python3 -m venv venv
. venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt

# Install collections into the venv itself
ANSIBLE_COLLECTIONS_PATH=$(python3 -c "import site; print(site.getsitepackages()[0])") \
  ansible-galaxy collection install -r galaxy.yml
