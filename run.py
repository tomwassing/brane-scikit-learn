#!/usr/bin/env python3

##############################################################################
#
# Run
#   This file is the entry point for running the application.
#
# Maintainers:
#   - Jurre J. Brandsen (11808918)
#   - Sander J. Misdorp (12151785)
#   - Tom J. Wassing (12386716)
##############################################################################
import os
import sys
import yaml
import inspect
import ast
import numpy as np
import json

from sklearn.decomposition import PCA
from sklearn import datasets, preprocessing
from sklearn.impute import SimpleImputer


def get_dynamic_args(func):
    '''
    Get the arguments of a function as a dictionary.
    This is used to dynamically set the arguments of a function.

    Args:
        func: The function to get the arguments of.
    Returns:
        A dictionary containing the arguments of the function.
    '''
    args = dict()
    signature = inspect.signature(func)

    for param in signature.parameters:
        # ignore self from constructor
        if param == "self":
            continue

        # try to parse the value from the environment with correct type
        value = os.environ.get(param.upper())
        if value is not None:
            try:
                args[param] = ast.literal_eval(value)
            except:
                args[param] = value

    return args


def load_dataset(name, attr):
    '''
    Load a dataset from sklearn.datasets.

    Args:
        name: The name of the dataset to load.
        attr: The attribute of the dataset to load.
    Returns:
        The loaded dataset.
    '''
    load_dataset_func = getattr(datasets, name)
    dataset = load_dataset_func()
    return getattr(dataset, attr)


def pca_fit_transform(data):
    '''
    Perform PCA on the data.

    Args:
        data: The data to perform PCA on.
    Returns:
        The transformed data.
    '''
    args = get_dynamic_args(PCA.__init__)
    return PCA(**args).fit_transform(data)


def normalize(data):
    '''
    Normalize the data.

    Args:
        data: The data to normalize.
    Returns:
        The normalized data.
    '''
    return preprocessing.normalize(data)


def simple_imputer(data):
    '''
    Perform SimpleImputer on the data.

    Args:
        data: The data to perform SimpleImputer on.
    Returns:
        The transformed data.
    '''
    args = get_dynamic_args(SimpleImputer.__init__)
    return SimpleImputer(**args).fit_transform(data)


def main(function_name):
    '''
    Main function.

    Args:
        function_name: The name of the function to run.
    Returns:
        The output of the function.
    '''

    # reading input data
    input_data = os.environ.get("INPUT")
    data = None

    if input_data:
        raw_data = json.loads(input_data)
        data = np.array(raw_data)

    if function_name.startswith("load_"):
        data = os.getenv("DATA", "data")
        result = load_dataset(function_name, data)
    elif function_name == "pca_fit_transform":
        result = pca_fit_transform(data)
    elif function_name == "normalize":
        result = normalize(data)
    elif function_name == "simple_imputer":
        result = simple_imputer(data)
    else:
        print("Unknown function: %s" % function_name)
        sys.exit(1)

    raw_output = json.dumps(result.tolist())
    return yaml.dump({"output": raw_output})


if __name__ == "__main__":
    function_name = sys.argv[1]
    input_data = os.environ.get("INPUT")
    output = main(function_name)
    print(output)
