# Card: olive-cormorant-nllb-pooled-context-base-600M

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> c7a9526b8416e4a2335689b529a682f516fdc63c

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/c7a9526b8416e4a2335689b529a682f516fdc63c/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/c7a9526b8416e4a2335689b529a682f516fdc63c/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
