# Card: olive-cormorant-bart

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> b59d85f0b06128795202b260fca5e67530d4e0cc

If possible, include the following links to Github:

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/b59d85f0b06128795202b260fca5e67530d4e0cc/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/b59d85f0b06128795202b260fca5e67530d4e0cc/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the final model after the first complete epoch. **NB**: the validation BLEU was ~62 at this point.

## Additional comments (optional)

This is basically a test run of this model. It doesn't currently seem worth to us to invest in translation models without registers, so we don't anticipate further investing in training this model better.
