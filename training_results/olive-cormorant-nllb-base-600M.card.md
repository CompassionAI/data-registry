# Card: olive-cormorant-nllb-base-600M

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 63df0999fcfd418d966f020a32078ba33f2cd3f4

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/63df0999fcfd418d966f020a32078ba33f2cd3f4/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/63df0999fcfd418d966f020a32078ba33f2cd3f4/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.

## Additional comments

This is basically a test run of this model. It doesn't currently seem worth to us to invest in short encoders without some mechanism for injecting prior context from the target language, so we don't anticipate further investing in training this model better. It mostly serves as a baseline.
