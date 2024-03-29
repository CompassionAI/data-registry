# Card: nllb-600M

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 5278dcf686e941ab368b74ac40a875d66f71b175

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/5278dcf686e941ab368b74ac40a875d66f71b175/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/5278dcf686e941ab368b74ac40a875d66f71b175/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
