#!/bin/bash
ACTIVATE_ENV=$(which activate)
PROJECT_NAME={{cookiecutter.repo_name}}
INSTALL_JUPYTER={{ cookiecutter.use_jupyter_notebooks }} #true or false

# Run the create_environment Makefile command
echo "Creating environment..."
make create_environment

# activate the environment
source $ACTIVATE_ENV $PROJECT_NAME

echo ">>> Install requirements using pip"
make reqs

# Install Jupyter Kernel if necessary
if [ "$INSTALL_JUPYTER" == "true" ]; then
    echo ">>> Installing Jupyter Kernel"
    pip install ipykernel  
    python -m ipykernel install --user --display-name ${PWD} --name ${PWD##*/}
fi

#initialize git
echo "Initializing git..."
git init
git add .
git commit -m "Initial commit"
