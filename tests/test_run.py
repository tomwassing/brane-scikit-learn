
import os
import sys
from run import main

def test_random_nparray():
    os.environ["INPUT"] = u""+open("tests/input.txt").read()
    assert main("fit_transform") == u""+open("tests/correct_random_output.txt").read()

def test_iris_dataset():
    os.environ["IRIS"] = "True"
    assert main("fit_transform") == u""+open("tests/iris_output.txt").read()

# todo compare sklearn against our own implementation

