# Run OS check here, since this is executed in the root directory of a copy of the repository directory
import os
import platform
import shutil
import requests

def latest_python_version():
    result = requests.get("https://endoflife.date/api/python.json")
    parsed_result = result.json()
    reccomended_v = parsed_result[2]["latest"] # two versions back
    latest_v =  parsed_result[0]["latest"]
    
    choices = [reccomended_v, latest_v]
    
    print(f"Possible Python versions: {choices}")

    # print(f"Latest Python version: {version_string}")
    return choices


def select_platform_post_hook():
    if platform.system() in ['Linux', 'Darwin']:  # Darwin is for macOS
        os.rename('hooks/_post_gen_project.sh', 'hooks/post_gen_project.sh')

        if shutil.which('make') is None:
            print("'make' command is not available")
            print("Please install 'make' before continuing")
            
            # abort the cookiecutter
            exit(1)
            
        
    else:
        os.rename('hooks/_post_gen_project.py', 'hooks/post_gen_project.py')

    
select_platform_post_hook()

latest_python_version()

