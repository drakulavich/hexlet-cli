import os


RESOURCES_PATH = os.path.abspath(os.path.dirname(__file__))


def resource_path(name: str):
    return os.path.join(RESOURCES_PATH, name)
