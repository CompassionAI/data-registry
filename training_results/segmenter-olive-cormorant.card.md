# Card: segmenter-olive-cormorant

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

Everything is in the CompassionAI/garland repo, commit SHA:

> 6df0fe283058706915025597ccfe18ad2390ba75

Configuration files are in [cai_garland/training/segmenter.config](https://github.com/CompassionAI/garland/blob/main/cai_garland/training/segmenter.config/config.yaml).

The training driver is [cai_garland/training/segmenter.py](https://github.com/CompassionAI/garland/blob/main/cai_garland/training/segmenter.py).

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion is the checkpoint with the highest F1 score. The F1 score training curve is plotted in the Tensorboard logs.
