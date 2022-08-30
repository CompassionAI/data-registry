# Card: part-of-speech-olive-cormorant

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

Everything is in the CompassionAI/manas repo, commit SHA:

> 243c2e9cf40e44d872b3e52de3388aa6a5804be2

Configuration files are in [cai_manas/part_of_speech/pos_fine_tuning.config](https://github.com/CompassionAI/manas/tree/243c2e9cf40e44d872b3e52de3388aa6a5804be2/cai_manas/part_of_speech/pos_fine_tuning.config).

The training driver is [cai_manas/part_of_speech/pos_fine_tuning.py](https://github.com/CompassionAI/manas/blob/243c2e9cf40e44d872b3e52de3388aa6a5804be2/cai_manas/part_of_speech/pos_fine_tuning.py).

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion is the checkpoint with the highest F1 score. The F1 score training curve is plotted in the Tensorboard logs.