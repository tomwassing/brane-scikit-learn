#!/usr/bin/env python3
import base64
from cgitb import reset
import os
import sys
import yaml
import io
import inspect
from sklearn.decomposition import PCA
from sklearn import datasets, preprocessing
import ast
import numpy as np
import json

def pca_fit_transform(data):
  # dynamically resolve arguments for PCA constructor
  args = dict()
  signature = inspect.signature(PCA.__init__)

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

  # exectue pca method
  pca = PCA(**args)
  return pca.fit_transform(data)

def normalize(data):
  return preprocessing.normalize(data)

def main(function_name):
  input_data = os.environ.get("INPUT")
  iris = os.environ.get("IRIS")

  # toggle to use iris dataset as test data
  if iris:
    iris = datasets.load_iris()
    input_data = json.dumps(iris.data.tolist())

  # reading input data
  raw_data = json.loads(input_data)
  data = np.array(raw_data)

  if function_name == "pca_fit_transform":
    result = pca_fit_transform(data)
  elif function_name == "normalize":
    result = normalize(data)
  else:
    print("Unknown function: %s" % function_name)
    sys.exit(1)

  raw_output = json.dumps(result.tolist())
  return yaml.dump({"output": raw_output})


if __name__ == "__main__":
    function_name = sys.argv[1]
    input_data = os.environ.get("INPUT")
    iris = os.environ.get("IRIS")
    main(function_name)