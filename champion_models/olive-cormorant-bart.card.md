# Card: olive-cormorant-bart

The details of the training protocol are in the training results card.

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. The Tibetan "base-base" version does not have any registers, while "base-x3-base" has 3 registers.

## Model description

- The encoder is a headless _albert-olive-cormorant_ transformer. The "-xN" postfix for the encoder size indicates the number of Siamese registers.
- The decoder is Facebook's BART, loaded from Hugging Face, with a causal LM head.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed datasets _84000-parallel-sentences-raw_ and _84000-parallel-sentences-3-registers-only_.

## CompassionAI comments

This is basically a test run of this model. In the future we will set up the training protocol more carefully.

It doesn't currently seem worth to us to invest in short encoders models without registers, at least for translation. So, we don't anticipate further investing in training the model without registers better.
