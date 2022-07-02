# Card: olive-cormorant-bart

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 69c68713f25b468bc4d4e8c296a1b88c6d41de09

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/69c68713f25b468bc4d4e8c296a1b88c6d41de09/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/69c68713f25b468bc4d4e8c296a1b88c6d41de09/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the final model after 2.5 epochs. **NB**: the validation BLEU was almost 70 at this point and the learning rate was <3e-5.

## Additional comments

This is basically a test run of this model. Later we will set up the training protocol more carefully.
