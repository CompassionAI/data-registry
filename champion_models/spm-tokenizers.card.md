# Card: spm-tokenizers

## Purpose

A set of pre-trained Tibetan tokenizers, intended for use with token-based transformer models. They are intended to be used with the Transformers-based TibertTokenizer class.

## Model description

These are all SentencePiece models, see here: <https://github.com/google/sentencepiece>.

## Training data

See the spm-tokenizer-training processed dataset.

## Training protocol

See the outer block of "manas/tokenizer/tokenizer.py" in the CompassionAI/manas repo. For example:

```python
import os

cai_base_bath = os.environ['CAI_DATA_BASE_PATH']
spm_tokenizer_training = os.path.join(cai_base_bath, "processed_datasets/spm-tokenizer-training")
spm_tokenizers = os.path.join(cai_base_bath, "champion_models/spm-tokenizers")

TibertTokenizer.train(
    os.path.join(spm_tokenizer_training, "spm_train.txt"),
    os.path.join(spm_tokenizers, "tibert_spm_bpe_big"),
    model_type='bpe',
    vocab_size=10000)
```

## Notable limitations

Individual characters are included in the training data. This means you can tokenize absolutely any string of Tibetan text. Of course, this doesn't mean you will get reasonable results from downstream models this way.

## CompassionAI comments

The wrapper tokenizer class can be toggled to use a strict intersyllabic tokenization:

```python
tibert_tkn.tsheg_pretokenization = True
```

The wrapper tokenizer class can also be toggled to use a stochastic tokenization, this may be useful during certain kinds of training as an augmentation:

```python
tibert_tkn.stochastic_tokenization = False
```

The models are organized by tokenizer vocabulary size. To load them from local disk, provide the name of the directory to _from_pretrained_ like so:

```python
import os
from cai_manas.tokenizer import TibertTokenizer

cai_base_bath = os.environ['CAI_DATA_BASE_PATH']
spm_tokenizers = os.path.join(cai_base_bath, "champion_models/spm-tokenizers")

tokenizer = TibertTokenizer.from_pretrained(os.path.join(spm_tokenizers, "tibert_spm_bpe_big"))
```
