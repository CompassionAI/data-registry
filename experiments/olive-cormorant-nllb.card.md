# Card: olive-cormorant-nllb

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text.

## Model description

- The encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's NLLB-200 decoder (the 600M size), loaded from Hugging Face, with a causal LM head.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed datasets _84000-parallel-sentences-no-registers_.

## CompassionAI comments

This is basically a test run of this model. In the future we will set up the training protocol more carefully.
