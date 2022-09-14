# Card: segmenter-olive-cormorant

## Model

### Purpose

Segmentation of long text into segments to be fed to the translation model.

### Model description

Fine-tuned AlBERT-olive-cormorant transformer with a sequence classification head.

### Training data

Directly ingests the training data from segmenter-dataset.

### Training protocol

See the training results below.

### Notable limitations (optional)

Due to resource constraints, currently this is a base-sized model of width 128.

## Training results

### Code links

Everything is in the CompassionAI/garland repo, commit SHA:

> 13309592ed85495f2e8552b86cca8df19f6ce3ae

Configuration files are in [cai_garland/training/segmenter.config](https://github.com/CompassionAI/garland/blob/main/cai_garland/training/segmenter.config/config.yaml).

The training driver is [cai_garland/training/segmenter.py](https://github.com/CompassionAI/garland/blob/main/cai_garland/training/segmenter.py).

### Execution steps

Execute the training driver with no arguments.

### Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

### Champion selection

The champion is the checkpoint with the highest F1 score. The F1 score training curve is plotted in the Tensorboard logs.
