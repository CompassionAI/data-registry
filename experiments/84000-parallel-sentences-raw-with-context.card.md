# Card: 84000-parallel-sentences-raw-with-context

## Purpose

Train a classical Tibetan to English translation model that follows the style established by 84,000. This dataset is a raw passthrough, with pre- and post-processing but no shuffling or concatenation, or augmentation with the dictionary. It does include context embeddings for the English that precedes the parallel sentence fragment.

## Root datasets

_84000-parallel-sentences_

## Methodology

The dataset is a processed version of the raw 84,000 parallel sentences. See the [root Hydra config file](https://github.com/CompassionAI/garland/blob/79930ce5f9e588502d6c862e3f0d573a43187862/cai_garland/data/parallel_dataset_prep.config/config.yaml) and the corresponding functions in [the preprocessing driver](https://github.com/CompassionAI/garland/blob/79930ce5f9e588502d6c862e3f0d573a43187862/cai_garland/data/parallel_dataset_prep.py) for the details.

The context embeddings consist of the BART encoder embeddings of the last 50 words preceding the English translation of the current sentence fragment in a full text of any of the published 84,000 translations. If multiple translations match, one is selected at random.

## How to reproduce

Just run "cai_garland.data.parallel_dataset_prep" with no arguments from the CompassionAI/garland repo. The commit SHA for the current version is:

> 79930ce5f9e588502d6c862e3f0d573a43187862

The preprocessing code is Hydra configured. The config files are can be found [in GitHub](https://github.com/CompassionAI/garland/tree/79930ce5f9e588502d6c862e3f0d573a43187862/cai_garland/data/parallel_dataset_prep.config).

## Comments

There is a lot of Sanskrit in this dataset. We don't currently have a good way to convert it to English.
