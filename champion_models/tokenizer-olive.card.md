# Card: tokenizer-olive

## Purpose

A set of pre-trained Tibetan SentencePiece tokenizers, intended for use with token-based transformer models. They are intended to be used with the Transformers-based CAITokenizer class.

## Model description

These are all SentencePiece models, see here: <https://github.com/google/sentencepiece>.

## Training data

See the dictionary-tokenizer-training processed dataset.

## Training protocol

See the outer block of "manas/tokenizer/tokenizer.py" in the CompassionAI/manas repo. For example:

```python
import os

cai_base_bath = os.environ['CAI_DATA_BASE_PATH']
dict_tokenizer_training = os.path.join(cai_base_bath, "processed_datasets/dictionary-tokenizer-training")
olive_tokenizers = os.path.join(cai_base_bath, "champion_models/olive-tokenizers")

CAITokenizer.train(
    os.path.join(spm_tokenizer_training, "spm_train.txt"),
    os.path.join(spm_tokenizers, "olive_big"),
    model_type='bpe',
    vocab_size=10000)
```

## Notable limitations

Individual characters are included in the training data. This means you can tokenize absolutely any string of Tibetan text. Of course, this doesn't mean you will get reasonable results from downstream models this way.

Because of the dataset chosen for this set of tokenizers, the tokenizers don't always handle postfixed intrasyllabic particles well.

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
from cai_manas.tokenizer import CAITokenizer

cai_base_bath = os.environ['CAI_DATA_BASE_PATH']
olive_tokenizers = os.path.join(cai_base_bath, "champion_models/tokenizer-olive")

tokenizer = CAITokenizer.from_pretrained(os.path.join(olive_tokenizers, "olive_big"))
```
