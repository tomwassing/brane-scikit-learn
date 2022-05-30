#!/usr/bin/env python3

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


def load_dataset(name):
    load_dataset_func = getattr(datasets, name)
    return load_dataset_func().data


def pca_fit_transform(data):
    args = get_dynamic_args(PCA.__init__)
    return PCA(**args).fit_transform(data)


def normalize(data):
    return preprocessing.normalize(data)


def simple_imputer(data):
    args = get_dynamic_args(SimpleImputer.__init__)
    return SimpleImputer(**args).fit_transform(data)


def main(function_name):
    # reading input data
    input_data = os.environ.get("INPUT")
    raw_data = json.loads(input_data)
    data = np.array(raw_data)

    if function_name.startswith("load_"):
        result = load_dataset(function_name)
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
    main(function_name)
