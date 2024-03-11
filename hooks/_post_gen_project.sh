#!/bin/bash
ACTIVATE_ENV=$(which activate)
PROJECT_NAME={{cookiecutter.repo_name}}
INSTALL_JUPYTER={{cookiecutter.use_jupyter_notebooks}} #true or false
echo $INSTALL_JUPYTER

# Run the create_environment Makefile command
echo "Creating environment..."
make create_environment

# activate the environment
source $ACTIVATE_ENV $PROJECT_NAME
# exit only if previous command successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate environment"
    exit 1
fi


echo ">>> Install requirements using pip"
pip install -r requirements.txt

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
