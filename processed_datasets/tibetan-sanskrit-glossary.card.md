# Card: tibetan-sanskrit-glossary

## Purpose

Converted 84,000 glossary for training augmentation and other translation-related use cases.

## Warnings

Not originally intended to kick start unsupervised machine translation training.

## Root datasets

tibetan-sanskrit-glossary

## Methodology

The dataset is a reformatted version of the 84,000 glossary. The modifications are:

 - Deduping is done by taking the first Tibetan version of the word.
 - The transliterated Sanskrit is pre-processed and post-processed in the same way as the datasets such as _84000-parallel-sentences-raw-with-context_.

## How to reproduce

Use commit SHA

> 2ff624634423723425fd633c34362745bcb812d8

and run [the preprocessing driver](https://github.com/CompassionAI/garland/blob/79930ce5f9e588502d6c862e3f0d573a43187862/cai_garland/data/parallel_dataset_prep.py) with the [root Hydra config file](https://github.com/CompassionAI/garland/blob/79930ce5f9e588502d6c862e3f0d573a43187862/cai_garland/data/dataset_prep.config/config.yaml) set to glossary only.