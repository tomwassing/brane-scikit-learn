
import os
import numpy as np
import json
import yaml

from run import main
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.impute import SimpleImputer
from sklearn import datasets


def read_output(output):
    yaml_output = yaml.safe_load(output)
    output_data = np.array(json.loads(yaml_output["output"]))
    return output_data


def test_random_nparray():
    test_data = np.random.rand(25, 25)
    os.environ["INPUT"] = json.dumps(test_data.tolist())
    os.environ["N_COMPONENTS"] = "2"

    output = read_output(main("pca_fit_transform"))
    expected_output = PCA(n_components=2).fit_transform(test_data)

    assert (output == expected_output).all()


def test_normalize():
    test_data = np.random.rand(25, 25)
    os.environ["INPUT"] = json.dumps(test_data.tolist())

    output = read_output(main("normalize"))
    expected_output = normalize(test_data)

    assert (output == expected_output).all()


def test_simple_imputer():
    test_data = np.random.rand(25, 25)

    # Add missing values
    random_index = np.random.choice(test_data.size, 10, replace=False)
    test_data.ravel()[random_index] = np.nan

    os.environ["INPUT"] = json.dumps(test_data.tolist())
    os.environ["STRATEGY"] = "most_frequent"

    output = read_output(main("simple_imputer"))
    expected_output = SimpleImputer(
        strategy="most_frequent").fit_transform(test_data)

    assert (output == expected_output).all()


def test_load_dataset():
    output = read_output(main("load_iris"))
    expected_output = datasets.load_iris().data

    assert (output == expected_output).all()
