# Card: albert-olive-cormorant

The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Code links

The base code is in the CompassionAI/manas repo, commit SHA:

> 224fd00156960fdabaf3fda618ce882979726c29

The AlBERT code is in the CompassionAI/albert fork, commit SHA:

> 87d7f7f3c82848a90818cdd68f88388c055d8733

The data preparation is in [pretraining/albert/build_pretraining_data_no_sop.sh](https://github.com/CompassionAI/manas/blob/224fd00156960fdabaf3fda618ce882979726c29/pretraining/albert/build_pretraining_data_no_sop.sh).

The driver is in [pretraining/albert/albert/run_pretraining_no_sop.py](https://github.com/CompassionAI/albert/blob/87d7f7f3c82848a90818cdd68f88388c055d8733/run_pretraining_no_sop.py).

There are no config files but the training command is documented in [pretraining/albert/TIBERT_PRETRAIN.md](https://github.com/CompassionAI/manas/blob/224fd00156960fdabaf3fda618ce882979726c29/pretraining/albert/TIBERT_PRETRAIN.md).

## Execution steps (optional)

See [pretraining/albert/TIBERT_PRETRAIN.md](https://github.com/CompassionAI/manas/blob/224fd00156960fdabaf3fda618ce882979726c29/pretraining/albert/TIBERT_PRETRAIN.md) for the exact steps.

The model configuration can be downloaded like so:

```bash
mkdir /tmp/albert_base && cd /tmp/albert_base
wget https://storage.googleapis.com/albert_models/albert_base_v2.tar.gz
tar -xf albert_base_v2.tar.gz
```

The training can be executed as follows:

```bash
python -m albert.run_pretraining_no_sop \
    --input_file=gs://compassion-ai/bert-like-endogenous-docs-tfrecords-128/*.tf_record \
    --output_dir=gs://compassion-ai/training-results/tibert-base-128-no-sop/ \
    --albert_config_file=/tmp/albert_base/albert_config.json \
    --do_train \
    --train_batch_size=1024 \
    --max_seq_length=128 \
    --max_predictions_per_seq=20 \
    --optimizer=lamb \
    --learning_rate=.00176 \
    --num_warmup_steps=3125 \
    --num_train_steps=1000000 \
    --save_checkpoints_steps=1000 \
    --keep_checkpoint_max=100 \
    --use_tpu=true \
    --tpu_name=tibert-tpu \
    --tpu_zone=us-central1-a \
    --num_tpu_cores=8
```

## Hyperparameters

The model that's trained is the base size of AlBERT version 2. The length of the model is 128 tokens. The SOP task has been removed, with the full input sequence dedicated to the MLM task.

The optimization configuration is in the execution code. The relevant parameters are:

```bash
--train_batch_size=1024
--max_predictions_per_seq=20
--optimizer=lamb
--learning_rate=.00176
--num_warmup_steps=3125
--num_train_steps=1000000
--save_checkpoints_steps=1000
```

There was no sweeping.

## Champion selection

The champion is the checkpoint with the lowest training loss.

## Additional comments

What's recorded in this file is the non-SOP version of the model. The actual model was trained with SOP until about ~800k steps. The dataset and training code was then replaced with the non-SOP version, and training continued from this point. This is because we realized late that we should remove the SOP task but didn't have the resources to simply re-run the training.

This is unlikely to make any difference, since this essentially fine-tunes the model on the MLM task and the number of steps taken after the task replacement is very large.
