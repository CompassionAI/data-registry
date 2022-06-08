# Card: part-of-speech-intrasyllabic-tags

## Purpose

Part-of-speech tagging via a fine-tuned monolingual transformer. Uses the concatenated intrasyllabic SOAS tags described in the processed dataset part-of-speech-intrasyllabic-words.

## Model description

Fine-tuned AlBERT-tibert transformer.

## Training data

Directly ingests the training data from part-of-speech-intrasyllabic-words. The only change is a random 90-10 test set split.

## Training protocol

Use the cai_manas/part_of_speech/pos_fine_tuning.py driver script in the CompassionAI/manas repo. The current run is reproduced as follows:

```bash
python -m cai_manas.part_of_speech.pos_fine_tuning \
    --tibert_pytorch_ckpt tibert-albert/base.bin \
    --output_dir ~/workspace/temp/pos-tagger \
    --train_dataset_name part-of-speech-intrasyllabic-words \
    --do_train \
    --use_mask_for_word_pieces \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --num_train_epochs 20 \
    --logging_steps 10 \
    --save_steps 50 \
    --save_total_limit 50 \
    --log_level debug \
    --evaluation_strategy steps
```

The champion is the checkpoint with the highest test set F1 score. In this run, this was the 1,050-th step.

## Notable limitations (optional)

Due to resource constraints, currently this is a base-sized model of width 128.

## CompassionAI comments (optional)

If possible, this model should be redone on an intersyllabic version of the training data. See the discussion in the dataset card for the processed dataset part-of-speech-intrasyllabic-words.
