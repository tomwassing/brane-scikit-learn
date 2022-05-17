#!/usr/bin/env python3
import base64
from cgitb import reset
import os
import sys
import yaml
import io
from sklearn.decomposition import PCA
from sklearn import datasets

import numpy as np

def decode(s: str) -> str:
  s = s.replace("\n", "")
  b = base64.b64decode(s)
  return b.decode("UTF-8")

def encode(s: str) -> str:
  b = s.encode("UTF-8")
  b = base64.b64encode(b)
  return b.decode("UTF-8")

if __name__ == "__main__":
  command = sys.argv[1]
  argument = os.environ["INPUT"]

  if command == "iris":
    iris = datasets.load_iris()
    fake_file = io.StringIO()
    np.savetxt(fake_file, iris.data)
    # print(yaml.dump({"output": fake_file.getvalue()}))
  else:
    # TODO: replace with INPUT
    iris = datasets.load_iris()
    fake_file = io.StringIO()
    np.savetxt(fake_file, iris.data)
    fake_file2 = io.StringIO(fake_file.getvalue())
    data = np.loadtxt(fake_file2)

    # print(data)

    pca  = PCA(n_components=2)
    method = getattr(pca, command)
    result = method(data)

    fake_file = io.StringIO()
    np.savetxt(fake_file, result)
    # print(result)

    print(yaml.dump({"output": fake_file.getvalue()}))