# Card: olive-cormorant-bart

The details of the training protocol are in the training results card.

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. The Tibetan side does _not_ have any registers here.

## Model description

- The encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's BART, loaded from Hugging Face, with a causal LM head.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed dataset _84000-parallel-sentences-no-registers_.

## CompassionAI comments

This is basically a test run of this model. It doesn't currently seem worth to us to invest in translation models without registers, so we don't anticipate further investing in training this model better.
