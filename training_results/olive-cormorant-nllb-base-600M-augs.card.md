# Card: olive-cormorant-nllb-base-600M-augs

This is the training curves for the base-600M sized model with augmentation but without context encoding. The NLLB-3B decoder training run and both the normalized and unnormalized training NLLB-600M with context training runs for comparison. It is for research purposes only, the model itself performs poorly. Only the training curves matter as a basis of comparison.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 20aa43f8b26daab06d03e4b6ff00d35db4ca0949

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/20aa43f8b26daab06d03e4b6ff00d35db4ca0949/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/20aa43f8b26daab06d03e4b6ff00d35db4ca0949/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset. It performs poorly in inference.
