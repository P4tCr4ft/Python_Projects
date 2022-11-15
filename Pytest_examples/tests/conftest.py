import json
import os

from pytest import fixture

working_dir = os.getcwd()
data_path = working_dir + "/tests/test_data.json"


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
