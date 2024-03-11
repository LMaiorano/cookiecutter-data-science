#!/bin/bash
ACTIVATE_ENV=$(which activate)
PROJECT_NAME={{cookiecutter.repo_name}}
INSTALL_JUPYTER={{cookiecutter.use_jupyter_notebooks}} #true or false
echo $INSTALL_JUPYTER

# Abort if directory already exists
if [ -d "$PROJECT_NAME" ]; then
    echo "Error: Directory $PROJECT_NAME already exists"
    exit 1
fi



# Run the create_environment Makefile command
echo "Creating environment..."
make create_environment

# activate the environment
# First line is absolutely necessary. Do not remove!! conda activate is buggy and this fixes it
source $(dirname "$CONDA_EXE")/../etc/profile.d/conda.sh # Or path to where your conda is
conda activate $PROJECT_NAME

# exit only if previous command successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate environment"
    exit 1
fi


# Install requirements
echo ">>> Install requirements using pip"
make requirements

# Install Jupyter Kernel if necessary
if [ "$INSTALL_JUPYTER" == "yes" ]; then
    echo ">>> Installing Jupyter Kernel"
    pip install ipykernel  
    python -m ipykernel install --user --display-name ${PWD} --name ${PWD##*/}
fi

# 


#initialize git
echo ">>> Initializing git..."
git init
git add .
git commit -m "Initial commit"


# Setup pre-commit hooks
echo ">>> Setting up pre-commit hooks"
pre-commit install --hook-type pre-commit --hook-type pre-push
