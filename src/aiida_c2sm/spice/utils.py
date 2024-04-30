import types

import yaml


def load_config(filename):
    with open(filename, 'r') as file:
        config_data = yaml.safe_load(file)
    return types.SimpleNamespace(**config_data)

