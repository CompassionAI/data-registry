# Card: olive-cormorant-bart-pooled-context

The details of the training protocol are in the training results card.

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. This version is trained with context pooling.

## Model description

- The source language encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's BART, loaded from Hugging Face, with a causal LM head.
- The context encoding algorithm is:
  1. Start with previous target language tokens,
  2. Encode them with the BART encoder,
  3. Transform the BART encodings with a dense layer with GELU activation,
  4. Sum pool the transformed encodings,
  5. And inject this pooled embedding into the second token position.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder, as well as a Bart encoder layer on top of a frozen Bart encoder for the context. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed datasets _84000-parallel-sentences-raw-with-context_.

## CompassionAI comments

This is basically a test run of this model. In the future we will set up the training protocol more carefully.
