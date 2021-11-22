#!/bin/sh
#BATCH -N 1
#SBATCH --job-name=pubmed
#SBATCH -n 4
#SBATCH -c 10
#SBATCH --mem=5000
#SBATCH -o out.txt
#SBATCH -e out.txt
#SBATCH --partition=gpu
#SBATCH --gres=gpu:tesla-smx2:1

pip install git+git://github.com/afshinrahimi/pubmed_parser.git --upgrade
python parse.py
