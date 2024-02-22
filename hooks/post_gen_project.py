import os
import platform
import subprocess

def run_unix_setup():
    if platform.system() in ['Linux', 'Darwin']:  # Darwin is for macOS
        subprocess.run(['./unix_setup.sh'], shell=True)
    else:
        print("This system is not Unix-based. Please manually setup your environment.")


def check_commands_installed(commands):
    for command in commands:
        try:
            devnull = open(os.devnull)
            subprocess.Popen([command], stdout=devnull, stderr=devnull).communicate()
        except OSError as e:
            print(f"{command} is not installed. Please install it and try again.")
            return False 
    return True


def python_setup_steps():
    ACTIVATE_ENV = subprocess.getoutput('which activate')
    PROJECT_NAME = '{{cookiecutter.repo_name}}'
    INSTALL_JUPYTER = '{{cookiecutter.use_jupyter_notebooks}}'  # true or false
    print(INSTALL_JUPYTER)

    # Run the create_environment Makefile command
    print("Creating environment...")
    subprocess.run(['make', 'create_environment'], shell=True)

    # activate the environment
    subprocess.run(['source', ACTIVATE_ENV, PROJECT_NAME], shell=True)

    print(">>> Install requirements using pip")
    subprocess.run(['make', 'reqs'], shell=True)

    # Install Jupyter Kernel if necessary
    if INSTALL_JUPYTER == "yes":
        print(">>> Installing Jupyter Kernel")
        subprocess.run(['pip', 'install', 'ipykernel'], shell=True)
        subprocess.run(['python', '-m', 'ipykernel', 'install', '--user', '--display-name', os.getcwd(), '--name', os.getcwd()], shell=True)

    # initialize git
    print(">>> Initializing git...")
    subprocess.run(['git', 'init'], shell=True)
    subprocess.run(['git', 'add', '.'], shell=True)
    subprocess.run(['git', 'commit', '-m', '"Initial commit"'], shell=True)



# # List of commands to check
# req_commands = ['source', 'make', 'python', 'pip', 'git']

# if check_commands_installed(req_commands):
#     python_setup_steps()
    
run_unix_setup()