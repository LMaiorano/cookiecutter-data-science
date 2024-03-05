# Run OS check here, since this is executed in the root directory of a copy of the repository directory
import os
import platform



def select_platform_post_hook():
    if platform.system() in ['Linux', 'Darwin']:  # Darwin is for macOS
        os.rename('hooks/_post_gen_project.sh', 'hooks/post_gen_project.sh')
        # TODO: Check that make command is available
        
    else:
        os.rename('hooks/_post_gen_project.py', 'hooks/post_gen_project.py')

    
select_platform_post_hook()


#  TODO: Add pre-commit hooks that run black, isort, and flake8, and freeze the requirements.txt file