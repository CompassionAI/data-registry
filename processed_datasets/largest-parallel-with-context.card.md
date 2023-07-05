# Card: largest-parallel-with-context

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset is a concatenation of all parallel sentence datasets - the raw passthrough and the mined. It does include context embeddings for the English that precedes the parallel sentence fragment.

## Root datasets

_84000-parallel-sentences-raw-with-context_, _mined-parallel-sentences_

## Methodology

The dataset is generated in the same way as _84000-parallel-sentences-raw-with-context_ except that it also includes the mined sentences. The validation data does not include any mined sentences, they all go into training.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> 7c1d1a7a3da4d3b40e633387078f8783a1d0c12c

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/7c1d1a7a3da4d3b40e633387078f8783a1d0c12c/cai_garland/data/dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
