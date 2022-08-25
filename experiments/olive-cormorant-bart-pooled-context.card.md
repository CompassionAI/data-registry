# Card: olive-cormorant-bart-pooled-context

The details of the training protocol are in the training results card.

## Model

### Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. This version is trained with context pooling.

### Model description

- The encoder is a headless _albert-olive-cormorant_ transformer. The "-xN" postfix for the encoder size indicates the number of Siamese registers.
- The decoder is Facebook's BART, loaded from Hugging Face, with a causal LM head.
- The context is the previous target language tokens:
  1. Encoded with the BART encoder,
  2. Transformed with a dense layer,
  3. Sum pooled,
  4. And injected into the second token position.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

### Training data

See the processed datasets _84000-parallel-sentences-raw-with-context_.

### CompassionAI comments

This is basically a test run of this model. In the future we will set up the training protocol more carefully.

## Training

### Code links

The base code is in the CompassionAI/garland repo, commit SHA:

> 19d4dfdd74c8fe7b99de5d8ea7821887e3f35dc5

The driver file is in [cai_garland/training/train_nmt.py](https://github.com/CompassionAI/garland/blob/19d4dfdd74c8fe7b99de5d8ea7821887e3f35dc5/cai_garland/training/train_nmt.py).

The config files are in the [cai_garland/training/train_nmt.config](https://github.com/CompassionAI/garland/blob/19d4dfdd74c8fe7b99de5d8ea7821887e3f35dc5/cai_garland/training/train_nmt.config) directory.

### Execution steps

Execute the training driver with no arguments.

### Hyperparameters

The hyperparameters are in the config files.

There was no sweeping.

### Champion selection

The champion model is taken to be the model with lowest loss on the test (which is called validation in training) split of the dataset.
