import platform
import subprocess



def run_unix_setup():
    if platform.system() not in ['Linux', 'Darwin']:  # Darwin is for macOS
        print("This system is not Unix-based. Please manually setup your environment or use the provided Makefile.")

    
run_unix_setup()