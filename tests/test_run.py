
import os
import numpy as np
import json 
import yaml

from run import main
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

def test_random_nparray():
    test_data = np.random.rand(10, 10)
    os.environ["INPUT"] = json.dumps(test_data.tolist())
    os.environ["N_COMPONENTS"] = "2"

    output = main("pca_fit_transform")
    yaml_output = yaml.safe_load(output)
    output_data = np.array(json.loads(yaml_output["output"]))
    expected_output = PCA(n_components=2).fit_transform(test_data)

    assert (output_data == expected_output).all()

def test_normalize():
    test_data = np.random.rand(10, 10)
    os.environ["INPUT"] = json.dumps(test_data.tolist())

    output = main("normalize")
    yaml_output = yaml.safe_load(output)
    output_data = np.array(json.loads(yaml_output["output"]))
    expected_output = normalize(test_data)

    assert (output_data == expected_output).all()

