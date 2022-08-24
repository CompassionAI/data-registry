#!/bin/bash
NOCOLOR='\033[0m'
GREEN='\033[0;32m'

NOCOLOR='\033[0m' GREEN='\033[0;32m' echo -e "${GREEN}Pulling DVC cache${NOCOLOR}"
cd ./raw_datasets/
dvc pull
cd ..
echo -e "${GREEN}Pulling champion models${NOCOLOR}"
aws s3 sync s3://compassionai/data-registry/champion_models/ ./champion_models/
echo -e "${GREEN}Pulling processed datasets${NOCOLOR}"
aws s3 sync s3://compassionai/data-registry/processed_datasets/ ./processed_datasets/
echo -e "${GREEN}Pulling training results${NOCOLOR}"
aws s3 sync s3://compassionai/data-registry/training_results/ ./training_results/