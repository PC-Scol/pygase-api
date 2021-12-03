from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path
from os import environ

project_path = Path(__file__).resolve().parent.parent

configuration = ConfigParser(interpolation=ExtendedInterpolation())
configuration.read(project_path.joinpath('conf.ini'))

if not configuration['AUTH']['username']:
    configuration['AUTH']['username'] = environ.get('PEGASE_USER', '')

if not configuration['AUTH']['password']:
    configuration['AUTH']['password'] = environ.get('PEGASE_PASSWORD', '')
