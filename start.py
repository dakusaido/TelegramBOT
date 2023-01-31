import os
import pkg_resources
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'
__requirements_path = ROOT_DIR + 'requirements.txt'


def create_venv(python_exe_path_, proj_path):
    command = ' -m venv '
    os.system(python_exe_path_ + command + proj_path + '.venv')


def import_requirements(proj_path):
    python_interpreter = proj_path + r'.venv\Scripts\python.exe'
    requirements_path = proj_path + r'requirements.txt'
    os.system(python_interpreter + ' -m pip install -r ' + requirements_path)


def check_path(path):
    pattern = re.compile(r'(C:\\.*Python\\Python\d+\\python\.exe)')

    return bool(re.match(pattern, path))


if __name__ == '__main__':
    project_path = ROOT_DIR
    python_interpreter = r'data\config\PythonInterpreterPath\pythonInterpPath.env'

    if not os.path.exists(project_path + python_interpreter):
        while True:
            python_exe_path = input(
                r'python.exe Path ' +
                r'(For example: C:\Users\...\AppData\Local\Programs\Python\Python311\python.exe) ("n" to close)> ')

            if python_exe_path == 'n':
                exit()

            if not check_path(python_exe_path):
                continue

            else:
                break

        print('Saving python exe path...')
        with open(project_path + python_interpreter, mode='w', encoding='utf-8') as file:
            file.write("PYTHONPATH = " + python_exe_path)
            print(f'Python exe path saved in {project_path + python_interpreter}')

    else:
        print('Reading python exe path...', end=' ')
        with open(project_path + python_interpreter, mode='r', encoding='utf-8') as file:
            python_exe_path = file.readline().split()[-1]

            if not check_path(python_exe_path):
                raise Exception(f"{python_exe_path} isn't correct path")

            print(f'done\nPython exe path read at {project_path + python_interpreter}')

    if not os.path.exists(project_path + '.venv'):
        print(f'Creating [venv] to {project_path}...', end=' ')
        create_venv(python_exe_path, project_path)
        print(f'done')

        print('Importing requirements...', end=' ')
        import_requirements(project_path)
        print('done')

    else:
        print('Checking packages...', end=' ')
        pkg_resources.require(open(__requirements_path, mode='r', encoding='utf-8').readlines())
        print('done')

    print(f'Starting main file at {project_path + r"app.py"}')

    try:
        os.system(project_path + r'.venv\Scripts\python.exe ' + project_path + r'app.py')

    except KeyboardInterrupt:
        pass
