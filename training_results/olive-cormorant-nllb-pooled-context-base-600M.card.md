# Card: olive-cormorant-nllb-pooled-context-base-600M

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 3bbdef3daca354e241bf2cb6c61598eea01b2561

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/3bbdef3daca354e241bf2cb6c61598eea01b2561/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/3bbdef3daca354e241bf2cb6c61598eea01b2561/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
