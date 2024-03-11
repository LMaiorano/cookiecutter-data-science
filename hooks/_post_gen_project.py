import platform

def run_setup():
    if platform.system() not in ['Linux', 'Darwin']:  # Darwin is for macOS
        print("This system is not Unix-based. Please manually setup your environment:")
        print("1. Created isolated development environment (using ie. Conda/Mamba, virtualenv, poetry, etc...)")
        print("2. Activate the environment, and perform the following steps:")
        print("\ta) Install the required packages using the provided requirements.txt file: 'pip install -r requirements.txt'")
        print("\tb) Initialize the git repository: 'git init && git add . && git commit -m 'Initial commit'")
        print("\tc) Install pre-commit hooks: 'pre-commit install --hook-type pre-commit --hook-type pre-push'")
    
run_setup()