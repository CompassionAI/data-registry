# Card: OpenPecha-kangyur

## Summary

The Derge edition of the Kangyur with proofread corrections. Documentation of the comments is [here](https://github.com/OpenPecha/P000001/blob/master/docs/README.md).

## Source

From the releases in the [OpenPecha Derge Kangyur GitHub repo](https://github.com/OpenPecha/P000001). We use the paginated release. The current version is at <https://github.com/OpenPecha-Data/P000001/releases/download/v32/kagyur_derge_parpu_pages_P000001.zip>.

## Ingestion tools

Use the KangyurLoader class in the CompassionAI/common repo, in the file _/cai_common/data/open_pecha_loaders.py_.

Code sample:

```python
# You need a local Dask cluster for all CompassionAI datasets
from dask.distributed import Client, LocalCluster
dask_cluster = LocalCluster(n_workers=10, threads_per_worker=1)
dask_client = Client(dask_cluster)

# Data location comes from the CAI_DATA_BASE_PATH environment variable
from cai_common.data import KangyurLoader
kangyur_df = KangyurLoader().dataframe
```

## CompassionAI comments

This is a newer version of the original dataset we used to train our monolingual AlBERT. The original dataset is no longer available, it had many proofreading annotations that have been incorporated into this dataset upstream. The original dataset is archived in our data registry under _raw_datasets/OpenPecha-kangyur-old_.
