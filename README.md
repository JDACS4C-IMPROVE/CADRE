# Resources:
+ README.md: this file.
+ data: GDSC dataset, gen2vec embeddings

###  source codes:
+ prepare_datasets.py: create data for CADRE input
+ utils.py: dataset wrappers and utility functions
+ run_cf_candle.py: point of access to model training and testing
+ cadre_candle.py: main run file. Takes in path to configuration file as an optional parameter.
+ collabfilter.py: implementation of collaborative filtering.
+ bases.py: primitives for collaboration filtering
+ cadre.py: extension of CANDLE Benchmark class
+ CADRE_default.txt: default model parameters

## Dependencies
+ [Torch](https://pytorch.org/)
+ [Pandas](https://pandas.pydata.org/)
+ [Numpy](https://numpy.org/)
+ [Scipy](https://docs.scipy.org/doc/)

# Step-by-step running

## 1. Create dataset
TDB

## 2. Run model
python3 cadre_candle.py --config_file CADRE_default.txt
