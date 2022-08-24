# data-registry
Registry for models and datasets, managed by dvc

## How to use

## The rules

Raw datasets are the base datasets that are not derived. This is a versioned DVC cache backed by an S3 remote. Whenever updating these, please use

```bash
cd data-registry/raw_datasets
dvc add ${updated_dataset}
dvc push
```

to correctly version them.

The other subdirectories are synced with an S3 bucket but not versioned. This is because, in my opinion, they don't need to be, and versioning them is just a giant waste of HDD and S3 space. This is only my opinion.

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