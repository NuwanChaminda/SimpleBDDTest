import configparser
import os.path

location = os.path.abspath(os.path.dirname(__file__))

config_path = os.path.join(location, 'configarations.ini')
configarations = configparser.ConfigParser()
configarations.read(config_path)