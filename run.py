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


def main():
  command = sys.argv[1]
  input_data = os.environ.get("INPUT")
  iris = os.environ.get("IRIS")

  # toggle to use iris dataset as test data
  if iris:
    iris = datasets.load_iris()
    fake_file = io.StringIO()
    np.savetxt(fake_file, iris.data)
    input_data = fake_file.getvalue()

  data = np.loadtxt(io.StringIO(input_data))
  args = dict()
  signature = inspect.signature(PCA.__init__)

  # dynamically resolve arguments for PCA constructor
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
  method = getattr(pca, command)
  result = method(data)

  # redirect result to stdout
  fake_file = io.StringIO()
  np.savetxt(fake_file, result)
  # print(len(result))
  print(yaml.dump({"output": fake_file.getvalue()}))

if __name__ == "__main__":
  main()