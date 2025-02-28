# Run OS check here, since this is executed in the root directory of a copy of the repository directory
import os
import platform
import shutil
import requests

def latest_python_versions():
    result = requests.get("https://endoflife.date/api/python.json")
    parsed_result = result.json()
    taipy_v = parsed_result[1]["latest"]
    latest_v =  parsed_result[0]["latest"]
    
    choices = [latest_v, taipy_v]
    
    # print(f"Possible Python versions: {choices}")

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



def create_cookiecutter_json():
    
    version_choices = latest_python_versions()
    
    # Read the cookiecutter.json file
    with open('cookiecutter.json', 'r') as file:
        data = file.readlines()
    
    # find line with python_version
    rec_idx = [i for i, line in enumerate(data) if "PRE-PROMPT-TAIPY" in line]
    lat_idx = [i for i, line in enumerate(data) if "PRE-PROMPT-LATEST" in line]
    
    # replace PRE-PROMPT-LATEST with version_choices[0]
    for i in rec_idx:
        data[i] = data[i].replace("PRE-PROMPT-TAIPY", version_choices[1])
    
    for i in lat_idx:
        data[i] = data[i].replace("PRE-PROMPT-LATEST", version_choices[0])
    

    # Write the cookiecutter.json file
    with open('cookiecutter.json', 'w') as file:
        file.writelines(data)

create_cookiecutter_json()