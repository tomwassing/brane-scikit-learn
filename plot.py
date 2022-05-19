#!/usr/bin/env python3
import base64
import os
import sys
import yaml
import io
import inspect
import ast
import numpy as np
import matplotlib.pyplot as plt


def main():
  command = sys.argv[1]
  input_data = os.environ.get("INPUT")

  # read in all data
  data = np.loadtxt(io.StringIO(input_data))
#   args = dict()

#   data = [1,2,3,4,5]

  plt.plot(data)
  plt.show()

  # write image encoded to stdout
  fake_file = io.BytesIO()
  plt.savefig(fake_file)
  print(yaml.dump({"output": fake_file.getvalue()}))

if __name__ == "__main__":
  main()