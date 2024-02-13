#!/bin/bash
ACTIVATE_ENV=$(which activate)
PROJECT_NAME={{cookiecutter.repo_name}}

# Run the create_environment Makefile command
echo "Creating environment..."
make create_environment

# activate the environment
source $ACTIVATE_ENV $PROJECT_NAME

echo ">>> Install requirements using pip"
pip install -r requirements.txt

# Pip freeze requirements
echo ">>> Freezing requirements"
pip freeze > requirements.txt

#initialize git
echo "Initializing git..."
git init
git add .
git commit -m "Initial commit"
