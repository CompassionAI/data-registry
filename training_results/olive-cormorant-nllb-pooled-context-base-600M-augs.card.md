# Card: olive-cormorant-nllb-pooled-context-base-600M-augs

This is the training curves for the base-600M sized model with augmentation and both with and without context encoding normalization, with the NLLB-3B decoder training run for comparison. It is for research purposes only, the model itself performs poorly. Only the training curves matter as a basis of comparison.

## Code links

### Unnormalized

The base code is in the CompassionAI/garland repo, commit SHA:

> 7424b460fcfd8c92f8fcfddd62a7fb427e3c1eed

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/7424b460fcfd8c92f8fcfddd62a7fb427e3c1eed/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/7424b460fcfd8c92f8fcfddd62a7fb427e3c1eed/cai_garland/training/train_nmt.config) directory.

### Normalized

The base code is in the CompassionAI/garland repo, commit SHA:

> a342c2865b25182f40c7fd13faa3d33928876add

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/a342c2865b25182f40c7fd13faa3d33928876add/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/a342c2865b25182f40c7fd13faa3d33928876add/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset. It performs poorly in inference.
