# Card: olive-cormorant-nllb-pooled-context-cased

The details of the training protocol are in the training results card.

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. This version is cased and trained with context pooling.

## Model description

- The encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's NLLB-200 decoder, loaded from Hugging Face, with a causal LM head.
- The context encoding algorithm is:
  1. Start with previous target language tokens,
  2. Encode them with the BART encoder,
  3. Transform the BART encodings with another, randomly initialized BART encoder layer,
  4. Pool the transformed encodings by taking the encoding of the BOS token, as in BERT,
  5. And inject this pooled embedding into the second decoder input token position.

The only currently available sizes are the base size of the encoder and the 600M distillation of the decoder.

The casing is fixed during sequencing by comparing against the TEI translations in English.

## Training data

_84000-parallel-sentences-raw-with-context-cased_.

# Card: olive-cormorant-nllb-pooled-context-cased-base-600M

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 124995800d94773c9557029ca37cf50d2da9df89

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/124995800d94773c9557029ca37cf50d2da9df89/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/124995800d94773c9557029ca37cf50d2da9df89/cai_garland/training/train_nmt.config) directory.

## Execution steps

Execute the training driver with no arguments.

## Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

## Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
