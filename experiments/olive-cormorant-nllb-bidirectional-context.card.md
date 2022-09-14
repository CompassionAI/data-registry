# Card: olive-cormorant-nllb-bidirectional-context

## Purpose

A Tibetan-to-English encoder-decoder model, intended for machine translation of long text. This version is trained with context pooling and additional context in the source language added on the right (future text).

The training commit SHA for CompassionAI/garland is:

> f3fd78b5a2e58680a4aa1563feae4af345aea266

## Model description

- The source language encoder is a headless _albert-olive-cormorant_ transformer.
- The decoder is Facebook's BART, loaded from Hugging Face, with a causal LM head.
- The target language context encoding algorithm is:
  1. Start with previous target language tokens,
  2. Encode them with the BART encoder,
  3. Transform the BART encodings with a dense layer with GELU activation,
  4. Sum pool the transformed encodings,
  5. And inject this pooled embedding into the second token position.
- The source language context is added on the right, representing future source tokens to be translated. The context is separated from the text to be translated with a [MASK] token. All source context is fed to the encoder together with the to-be-translated source text.

There are cross-attention layers added to the decoder, see the [EncoderDecoderModel class](https://huggingface.co/docs/transformers/v4.20.1/en/model_doc/encoder-decoder#transformers.EncoderDecoderModel) in Hugging Face Transformers. The new layers are the cross-attention and the CausalLM head in the decoder. All new layers are initialized randomly.

The only currently available sizes are the base size of the encoder and the base size for the decoder.

## Training data

See the processed datasets _84000-parallel-sentences-raw-with-bidirectional-context_.

## CompassionAI comments

Adding source context doesn't seem to improve the overall performance of the translation model.
