# Card: nllb-with-context-600M-small-tokenizer

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> b5a03f6684df84dfa9e5f16a7ac28636c90c0eda

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/b5a03f6684df84dfa9e5f16a7ac28636c90c0eda/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/b5a03f6684df84dfa9e5f16a7ac28636c90c0eda/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
