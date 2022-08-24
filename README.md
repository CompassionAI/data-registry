# data-registry
Registry for models and datasets, managed by dvc

## How to use

### First setup

First make sure that all your permissions are set up correctly and that the command

```bash
aws s3 ls s3://compassionai/data-registry/
>                           PRE champion_models/
>                           PRE processed_datasets/
>                           PRE raw_datasets_dvc_cache/
>                           PRE training_results/
```

works correctly. You should then be able to simply run _pull.sh_:

```bash
cd data-registry
./pull.sh
```

### Subsequent use

To push everything use

```bash
cd data-registry
./push.sh
```

This will DVC push the raw datasets and S3 sync the rest. Note that you first need to DVC add all the changes in the raw datasets you may have made.

To pull everything use

```bash
cd data-registry
./pull.sh
```

To reset a raw dataset, use

```bash
cd data-registry/raw_datasets
dvc checkout ${dataset_to_reset}
```

To reset some other datum, simply delete its directory and run _pull.sh_.

## The rules

Raw datasets are the base datasets that are not derived. This is a versioned DVC cache backed by an S3 remote. Whenever updating these, please use

```bash
cd data-registry/raw_datasets
dvc add ${updated_dataset}
dvc push
```

to correctly version them.

The other subdirectories are synced with an S3 bucket but not versioned. This is because, in my opinion, they don't need to be, and versioning them is just a giant waste of HDD and S3 space. This is only my opinion.

Every entry should have a corresponding card Markdown file. Take a look at other cards of the same type as examples. Every subdirectory also has a card template, it is called _template.card.md_.