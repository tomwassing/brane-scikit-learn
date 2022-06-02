
<!-- Add a image to the readme -->
<img src="img/logo-braneskit.png" alt="SciKit logo" width="200"/>
<h1>Welcome to the Brane Scikit-learn package 👋</h1>

[![example workflow](https://github.com/tomwassing/brane-scikit-learn/actions/workflows/test.yml/badge.svg)](https://github.com/tomwassing/brane-scikit-learn/actions/workflows/test.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6607108.svg)](https://doi.org/10.5281/zenodo.6607108)

This repository contains a package for BRANE that runs multiple functions from the SciKit libary.
## Install

```sh
brane import tomwassing/brane-scikit-learn
```

## Requirements
- Scikit-learn
- Yaml
- numpy

## Usage

| Variable Name                                                                              | Input (Data)                                                                               | Output (Data)    | Description                                                                                               |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------|
|  `pca_fit_transform`                                                                         | Input (string)<br />  N_components (string)                                                       |  Output (string) | Performs PCA on the provided data and returns the transformed data.                                       |
| `normalize`                                                                                  | Input (string)                                                                             | Output (string)  | Scales input vectors individually to unit form                                                            |
|   `simple_inputer`                                                                           |  Input (string) <br /> strategy (string) <br /> fill_value (string)                                      |   Output (string)  | Function provides ways of dealing with various  missing values, uses the  strategy specified by the user. |
| `load_boston` <br /> `load_iris` <br /> `load_diabetes` <br /> `load_digits` <br /> `load_linnerud` <br /> `load_wine` <br /> `load_breast_cancer` | load_boston <br /> load_iris <br /> load_diabetes <br /> load_digits <br />  load_linnerud <br /> load_wine <br /> load_breast_cancer |    Output (string) |   Provides acces to the various stable datasets  provided by scikit-learn.                                |



## Run tests

```sh
python3 -m pytest
```

## Authors

👤 **Jurre J. Brandsen, Sander J. Misdorp, Tom J. Wassing**

* Github: [@JurreBrandsen1709](https://github.com/JurreBrandsen1709)
* Github: [@TomWassing](https://github.com/tomwassing)
* Github: [@SanderJan2](https://github.com/SanderJan2)

## Show your support

Give a ⭐️ if this project helped you!
