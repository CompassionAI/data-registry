# Card: part-of-speech-intersyllabic-olive-cormorant

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

Everything is in the CompassionAI/manas repo, commit SHA:

> 22215f397d305be31a09284470dd2f2148d187e4

Configuration files are in [cai_manas/part_of_speech/pos_fine_tuning.config](https://github.com/CompassionAI/manas/tree/22215f397d305be31a09284470dd2f2148d187e4/cai_manas/part_of_speech/pos_fine_tuning.config).

The training driver is [cai_manas/part_of_speech/pos_fine_tuning.py](https://github.com/CompassionAI/manas/blob/22215f397d305be31a09284470dd2f2148d187e4/cai_manas/part_of_speech/pos_fine_tuning.py).

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion is the checkpoint with the highest F1 score. The F1 score training curve is plotted in the Tensorboard logs.

For this run, this is the checkpoint for the 1,050-th step.
