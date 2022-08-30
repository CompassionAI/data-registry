# Card: olive-cormorant-bart-base-x2-base

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> d63e32980ab55c47fd7924502ddaa33368431d38

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/d63e32980ab55c47fd7924502ddaa33368431d38/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/d63e32980ab55c47fd7924502ddaa33368431d38/cai_garland/training/train_nmt.config) directory.

The commit SHA for the CompassionAI/manas repo, used for the tokenizer, is:

> 2610c08f390d4668f4dfef95115fb2b187ec3d53

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
