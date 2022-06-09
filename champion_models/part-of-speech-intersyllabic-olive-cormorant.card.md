# Card: part-of-speech-intersyllabic-olive-cormorant

## Purpose

Part-of-speech tagging via a fine-tuned monolingual transformer. Uses the concatenated intrasyllabic SOAS tags described in the processed dataset part-of-speech-intersyllabic-olive.

## Model description

Fine-tuned AlBERT-olive-cormorant transformer.

## Training data

Directly ingests the training data from part-of-speech-intersyllabic-olive. The only change is a random 90-10 test set split.

## Training protocol

Use the cai_manas/part_of_speech/pos_fine_tuning.py driver script in the CompassionAI/manas repo. The current run is reproduced as follows:

```bash
python -m cai_manas.part_of_speech.pos_fine_tuning \
    --tibert_pytorch_ckpt albert-olive-cormorant/base.bin \
    --output_dir ~/workspace/temp/pos-tagger \
    --train_dataset_name part-of-speech-intersyllabic-olive \
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
