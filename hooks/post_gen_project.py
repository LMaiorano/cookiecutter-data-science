import platform
import subprocess



def run_unix_setup():
    if platform.system() in ['Linux', 'Darwin']:  # Darwin is for macOS
        subprocess.run(['unix_setup.sh'], shell=True)
    else:
        print("This system is not Unix-based. Please manually setup your environment or use the provided Makefile.")

    
run_unix_setup()