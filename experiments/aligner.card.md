# Card: aligner

## Dataset

### Purpose

Train a Tibetan aligner helper model. The dataset consists of the following fields:

- Source sentence in Tibetan.
- English word stem.
- Part-of-speech tag of the word stem in the translation sentence.
- Label whether this word stem appears in the translation of the source sentence with the indicated part-of-speech tag.

### Root datasets

_84000-parallel-sentences_

### Methodology

See the [aligner notebook in CompassionAI/garland](https://github.com/CompassionAI/garland/blob/main/notebooks/Aligner.ipynb).

### How to reproduce

Just run the cells in the [aligner notebook](https://github.com/CompassionAI/garland/blob/main/notebooks/Aligner.ipynb) from the CompassionAI/garland repo. The commit SHA for the current version is:

> f3a8dafdac28309f58c6065874b7e216769dd0b8

## Model

The details of the training protocol are in the training results card.

### Purpose

Helper model for alignment.

### Model description

Fine-tuned olive-cormorant-bart transformer with a sequence classification head. Fine-tuning happens after NMT training.

### Training data

Directly ingests the training data from the aligner dataset.

### Training protocol

See the training results below.

### Notable limitations (optional)

Due to resource constraints, currently this is a base-sized model of width 128.

## Training protocol

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

### Code links

Everything is in the CompassionAI/garland repo, commit SHA:

> f3a8dafdac28309f58c6065874b7e216769dd0b8

Configuration files are in [cai_garland/training/aligner.config](https://github.com/CompassionAI/garland/blob/main/cai_garland/training/aligner.config/config.yaml).

The training driver is [cai_garland/training/aligner.py](https://github.com/CompassionAI/garland/blob/main/cai_garland/training/aligner.py).

### Execution steps

Execute the training driver with no arguments.

### Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

### Champion selection

The champion is the checkpoint with the highest F1 score. The F1 score training curve is plotted in the Tensorboard logs.