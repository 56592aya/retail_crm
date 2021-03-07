# Project Title

[Projct Description goes here]

## How to get started

<!--[Nothing here] -->

### Create Environmet

I used conda to create the environment in a unix environment.

```console
$ conda init
$ conda create -n ENV_NAME python=3.8.5
$ conda activate ENV_NAME
```

### Install requirements

Requirements are already put in a separate `requirements.txt` file. To install them run the following:

```console
$ pip install -r requirements.txt
```

## Running

<!--Instructions to run the code and create results-->

## Project Content

[Any specific changes to the project goes here]

```console
.
├── app
│   ├── app.py
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── home.html
│       ├── layout.html
│       └── result.html
├── input
│   └── _data_empty_csv.csv
├── models
│   └── model_dump_defult.bin
├── notebooks
│   └── exploration.ipynb
└── src
    ├── config.py
    ├── create_folds.py
    ├── preprocessing.py
    ├── run.py
    ├── train.py
    └── utils.py
├── requirements.txt
├── README.md
```

`./app/`

- contains the information about deploying the proj as app

`./input/`

- contains the input files (raw and/or modified) used in the project

`./models/`

- contains the saved models

`./notebooks/`

- contains the notebooks for exploration and/or presentation purposes

`./src/`

- contains all the *.py codes used in the project

- `config.py`

  - consists of the environemtnal variables or global parameters used

- `create_folds.py`

  - creates the folds according to the data distribution for evaluation

- `preprocessing.py`

  - entails most of the preprocessing that goes into the raw data

- `train.py`

  - contains the tools to train the model

- `utils.py`

  - These are utility functions needed

`./requirements.txt`

- contains the libraries needed to be installed for running the programs smoothly

`./README.md`

- contains the instructions for running the programs smoothly

### app
To run the Flask app in the local browser, go to the app folder.

```shell
$ export FLASK_APP=app.y
$ python app.y
```

Then open your browser at `localhost/5000`


### References:
