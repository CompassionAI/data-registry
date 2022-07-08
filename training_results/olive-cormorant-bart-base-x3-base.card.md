# Card: olive-cormorant-bart

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 9200da0000eec2df0e0a821f6d6264e3da2afd9e

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/9200da0000eec2df0e0a821f6d6264e3da2afd9e/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/9200da0000eec2df0e0a821f6d6264e3da2afd9e/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with largest BLEU on the _test_ (not validation) split of the dataset. The test split is further rebalanced to be 1:1 with and without registers, and subsampled to 20%.

## Additional comments

This is basically a test run of this model. Later we will set up the training protocol more carefully.
