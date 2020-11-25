import os
import tempfile


def get_user_home() -> str:
    """ return the user home path, support windows and linux """
    if os.name == 'nt':
        return os.environ['USERPROFILE']
    else:
        return os.environ['HOME']


def get_project_root() -> str:
    """ return project root """
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def get_data_root() -> str:
    """ return the data root path """
    return os.path.join(get_project_root(), 'data')


def get_system_temp_root() -> str:
    """ return system temp root path """
    root = tempfile.gettempdir()
    return root


if __name__ == '__main__':
    print(f'user home dir is {get_user_home()}')
    print(f'data root dir is {get_data_root()}')
