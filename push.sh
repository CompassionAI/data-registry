#!/bin/bash
NOCOLOR='\033[0m'
GREEN='\033[0;32m'

echo -e "${GREEN}Linting${NOCOLOR}"
if ! ./lint.py; then
    exit 100
fi

NOCOLOR='\033[0m' GREEN='\033[0;32m' echo -e "${GREEN}Pushing DVC cache${NOCOLOR}"
cd ./raw_datasets/
# dvc push
cd ..
echo -e "${GREEN}Pushing champion models${NOCOLOR}"
# aws s3 sync ./champion_models/ s3://compassionai/data-registry/champion_models/
echo -e "${GREEN}Pushing processed datasets${NOCOLOR}"
# aws s3 sync ./processed_datasets/ s3://compassionai/data-registry/processed_datasets/
echo -e "${GREEN}Pushing training results${NOCOLOR}"
# aws s3 sync ./training_results/ s3://compassionai/data-registry/training_results/