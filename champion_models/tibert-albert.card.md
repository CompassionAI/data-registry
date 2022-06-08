# Card: tibert-albert

## Purpose

A monolingual transformer model for classical literary Tibetan.

## Model description

The functional form of the transformer is identical to AlBERT. We use the tibert_spm_bpe_big tokenizer. Only the base size model of width 128 is currently available.

## Training data

We start with the processed dataset kangyur-tengyur-bert-like-marker-docs. We then tokenize it and convert to TFRecords using the original Google Research AlBERT code, except that we remove the SOP task and add some offsets and stochastic tokenization.

See the code in the CompassionAI/manas repo at _pretraining/albert/build_pretraining_data_no_sop.sh_ and the description in TIBERT_PRETRAIN.md in the same directory, under the section "Run the preprocessing".

## Training protocol

We follow the original AlBERT training protocol except that we remove the SOP task, similar to what FaceBook did with RoBERTa.

See the code in the CompassionAI/manas repo at _pretraining/albert/albert/run_pretraining_no_sop.py_ and the description in TIBERT_PRETRAIN.md in the same directory, under the section "Run the training".

Note that you will almost certainly need a TPU for this. The base version of this model was trained for ~1m epochs on a v2-8 TPU pod and cost about $500.

## Notable limitations

The training data includes a range of offsets and stochastic tokenization when split into sequences of length 128. It is unclear how much this matters, we did not have the resources to do any ablation studies.

The model was trained for ~1m epochs. It is not clear whether the training should have stopped earlier. Typically, pre-training doesn't need to stop early, however it is unclear whether this is still true with smaller datasets.

## CompassionAI comments

The idea behind using AlBERT was that the model has a lot fewer parameters and so may do better on a smaller dataset. It is not clear whether this is true, subsequent work by the NLP community suggests this may not be true. Additional testing with other architectures would be a good idea.

Once we have clean part-of-speech and NER tasks prepared, we should test the performance of intermediate checkpoints to identify the early stopping protocol, if any.
