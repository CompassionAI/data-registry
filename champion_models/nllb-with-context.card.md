# Card: nllb-with-context

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. This version is trained with context pooling.

The training commit SHA for CompassionAI/garland is:

> b5a03f6684df84dfa9e5f16a7ac28636c90c0eda

## Model description

- The source language encoder is the NLLB encoder, restricted to Tibetan.
- The decoder is NLLB decoder, loaded from Hugging Face, restricted to English with a causal LM head.
- The target language context encoding algorithm is:
  1. Start with previous target language tokens,
  2. Encode them with the BART encoder,
  3. Transform the BART encodings with a dense layer with GELU activation,
  4. Sum pool the transformed encodings,
  5. And inject this pooled embedding into the second token position.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed datasets _84000-parallel-sentences-raw-with-context_.

## CompassionAI comments

Adding source context doesn't seem to improve the overall performance of the translation model.
