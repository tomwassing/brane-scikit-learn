#!/usr/bin/env python3

import os
import sys
import yaml
import io
import json
import matplotlib.pyplot as plt
import numpy as np

def main(command):

  # reading input data
  input_data = os.environ.get("INPUT")
  raw_data = json.loads(input_data)
  data = np.array(raw_data)

  plt.plot(data)

  if os.environ.get("SHOW", False):
    plt.show()

  if command == "plot_base64":
    temp_file = io.BytesIO()
    plt.savefig(temp_file)
    output = temp_file.getvalue()

    # write image encoded to stdout
    print(yaml.dump({"output": output}))
  elif command == "plot_file":
    file_path = os.environ.get("FILE_PATH", "/data/output.png")
    plt.savefig(file_path)
    print(yaml.dump({"output": file_path}))
  else :
    print("Unknown command")

if __name__ == "__main__":
  command = sys.argv[1]
  main(command)
