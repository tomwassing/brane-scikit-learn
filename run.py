#!/usr/bin/env python3
import base64
from cgitb import reset
import os
import sys
import yaml
import io
import inspect
from sklearn.decomposition import PCA
from sklearn import datasets
import ast
import numpy as np


if __name__ == "__main__":
  command = sys.argv[1]
  input_data = os.environ["INPUT"]
  n_components = os.environ.get("N_COMPONENTS")

# if command == "iris":
  iris = datasets.load_iris()
  fake_file = io.StringIO()
  np.savetxt(fake_file, iris.data)
  input_data = fake_file.getvalue()

  input_data = iris.data

#   # print(yaml.dump({"output": fake_file.getvalue()}))
# else:
#   # TODO: replace with INPUT
#   iris = datasets.load_iris()
#   fake_file = io.StringIO()
#   np.savetxt(fake_file, iris.data)
#   fake_file2 = io.StringIO(fake_file.getvalue())
#   data = np.loadtxt(fake_file2)

  # print(data)

  args = dict()
  signature = inspect.signature(PCA.__init__)

  for param in signature.parameters:
      if param == "self":
        continue
      value = os.environ.get(param.upper())
      if value is not None:
        try:
          args[param] = ast.literal_eval(value)
        except:
          args[param] = value
  # print(args)
  # print(**args)

  pca = PCA(**args)
  print(input_data)
  method = getattr(pca, command)
  result = method(input_data)

  fake_file = io.StringIO()
  np.savetxt(fake_file, result)
  # print(result)

  print(yaml.dump({"output": fake_file.getvalue()}))