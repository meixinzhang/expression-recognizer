Facial Expression Recognition
==============================

We are exploring different models to accuratly identify facial expressions from photos. 

The expressions are limited to be finite classes, particularly, to the six basic emotions plus neutral
- Angry
- Discust
- Fear
- Happy
- Sad
- Surprised
- Neutral

This repo stores the scripts that implement KNN and CNN to extract facial expression from photos.
All of the models in this repo are trained, validated, and testing using images and category from the Kaggle Challenge, [Challenges in Representation Learning: Facial Expression Recognition Challenge](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge)
 - More relevant datasets can be found [here](./references/dataSource.md)


The full research paper can be found in the [reports folder](./reports).


Getting Started
------------

To get started using this repo

```sh
$ pip install -r requirements.txt --upgrade
```

The Models
------------

The prototypes used for this project can be found in the [notebooks directory](./notebooks).

Currently, the notebooks with complete models are 
- knn.ipynb
- cnn.ipynb

### Using the Models

Pretrained models (our best models) will appear in the [models directory](./models), these models may be uploaded and directly used at the end of each notebook listed above with Google Colab.

### Training the Models

To train the models, run the notebooks listed above in sequence on Jupyter or Google Colab. There are detailed instructions on how to load the data into the notebooks. Each built model is evaluated by their accuracy as well as their confusion matrix.


Useful Notes
-----------
 
### Setup Virtual Environment
```sh
cd ./example_repo
virtualenv example_repo_env
source ./example_repo_env/bin/activate
```

### Setup .env File for Python Decouple

Add your environmental variables to .env file, 

```sh
PYTHONPATH="/Users/usr/PATH_TO_REPO/"
```

use it like the following in your code:

```py
from decouple import config
config('PYTHONPATH')
```

Check [here](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html) for more information on python decouple.

 
### Database Setup for PostgreSQL
To setup Postgres and an engine for a Postgres database, refer to documentation [here](https://docs.sqlalchemy.org/en/13/core/engines.html).


Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
