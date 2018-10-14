import os


PATH = os.path.abspath(os.path.dirname(__file__))


def data_path(*args):
    return os.path.join(PATH, *args)


def read_file(path: str):
    with open(path, 'r') as myfile:
        data = myfile.read()
    return data
