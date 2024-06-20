"""
Util to change Django project name after moving from Django Puzzle Minimal App
to some real application name...

To run it successfully we need to run it inside ../src/<project-directory>/utils
and <project-directory> is already changed from 'minimalpuzzle' to final one
"""
import os
OLD_MINIMAL_PUZZLE_PROJECT_NAME = 'minimalpuzzle'
FILES_WE_CHANGE_PROJECT_NAME_IN = ['wsgi.py', 'settings.py', 'urls.py', 'asgi.py', 'manage.py']


def get_parent_directory(base_dir=None, parent_up_level=0):
    """Search directory relative to base_dir

    :param base_dir: direcotry we start to search in (None = current working directory)
    :param parent_up_level: how many levels up we search directory name
                            0=current directory, 1=level up, 2=2 evels up,...
    """
    # given directory or current working directory
    if base_dir is None:
        base_dir = os.getcwd()

    # Normalize base_dir
    current_dir = os.path.abspath(base_dir)

    # Walk up in directory structure
    for _ in range(parent_up_level):
        current_dir = os.path.dirname(current_dir)

    # Final requested direcotry level
    return current_dir


def get_parent_directory_name(base_dir=None, parent_up_level=0):
    """Search directory name relative to base_dir

    :param base_dir: direcotry we start to search in (None = current working directory)
    :param parent_up_level: how many levels up we search directory name
                            0=current directory, 1=level up, 2=2 evels up,...
    """
    # Získání jména adresáře na požadované úrovni
    current_dir = get_parent_directory(base_dir, parent_up_level)
    return os.path.basename(current_dir)


def replace_string_in_file(file_path, old_string, new_string):
    # Čtení obsahu souboru
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    # Nahrazení řetězce
    updated_contents = file_contents.replace(old_string, new_string)

    # Zápis zpět do souboru
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_contents)


# check utils direcotry as script direcotry
if __name__ == '__main__':
    if get_parent_directory_name() == 'utils':
        print("We are changing Django project direcotory name...")

        final_application_name = get_parent_directory_name(parent_up_level=1)

        # django project direcotry files - settings.py, asgi.py, wsgi.py, urls.py
        django_project_directory = get_parent_directory(parent_up_level=1)

        file_list = [file_name for file_name in os.listdir(django_project_directory)
                     if file_name in FILES_WE_CHANGE_PROJECT_NAME_IN]
        for each_file in file_list:
            replace_string_in_file(f"{django_project_directory}/{each_file}",
                                   OLD_MINIMAL_PUZZLE_PROJECT_NAME,
                                   final_application_name)

        # manage.py
        manage_file_directory = get_parent_directory(parent_up_level=2)
        if 'manage.py' in os.listdir(manage_file_directory):
            replace_string_in_file(f"{manage_file_directory}/manage.py",
                                   OLD_MINIMAL_PUZZLE_PROJECT_NAME,
                                   final_application_name)
        print('Done changing Django project name...')
    else:
        print("Run script change_django_project_name to change Django project name inside <project-directory>/utils")

