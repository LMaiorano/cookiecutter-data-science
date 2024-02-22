import os
import platform
import subprocess
from pathlib import Path


unix_sh_path = str(Path(Path(__file__).parent, 'unix_setup.sh'))

def run_unix_setup():
    if platform.system() in ['Linux', 'Darwin']:  # Darwin is for macOS
        subprocess.run([unix_sh_path], shell=True)
    else:
        print("This system is not Unix-based. Please manually setup your environment or use the provided Makefile.")

    
run_unix_setup()