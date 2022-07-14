# Card: olive-cormorant-bart-base-base

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 5d1ec0c7f444aa820912d74c5ccc6d709890d03a

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/5d1ec0c7f444aa820912d74c5ccc6d709890d03a/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/5d1ec0c7f444aa820912d74c5ccc6d709890d03a/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the final model at the end of 9 epochs. **NB**: the validation BLEU was in the mid-30s and still rising at this point. However, the validation loss is clearly increasing at this point.

## Additional comments

This is basically a test run of this model. It doesn't currently seem worth to us to invest in short encoders without registers for translation, so we don't anticipate further investing in training this model better.
