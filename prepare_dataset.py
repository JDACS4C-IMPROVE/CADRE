import pickle
import pandas as pd
from utils import load_dataset, split_dataset


def prepare_dataset(input_dir, repository, train_out='data/input/train.pkl', test_out='data/input/test.pkl', ptw_out='data/input/ptw_ids.pkl'):
    dataset, ptw_ids = load_dataset(
        input_dir=input_dir, repository=repository, drug_id=-1)
    train_set, test_set = split_dataset(dataset, ratio=0.8)
    pickle.dump(train_set, open(train_out, 'wb'))
    pickle.dump(test_set, open(test_out, 'wb'))
    pickle.dump(ptw_ids, open(ptw_out, 'wb'))
    print(dataset.keys())


def pivot_gdsc(data_full, values_column):
    index = data_full['COSMIC_ID']
    index = [f'COSMIC.{idx}' for idx in index]
    columns = data_full['DRUG_ID']
    values = data_full[values_column]
    coordinates_df = pd.DataFrame([index, columns, values]).transpose()
    coordinates_df.columns = ['Index', 'Columns', 'Values']
    out_df = coordinates_df.pivot('Index', 'Columns', 'Values')
    return out_df


def get_gdsc_log_ic50(gdsc_input='data/input/GDSC_data_full.tsv', log_ic50_out='data/input/gdsc.csv'):
    data_full = pd.read_csv(gdsc_input, sep='\t')
    out_df = pivot_gdsc(data_full, 'LN_IC50')
    out_df.to_csv(log_ic50_out)


def get_gdsc_auc(gdsc_input='data/input/GDSC_data_full.tsv', auc_out='data/input/gdsc.csv'):
    data_full = pd.read_csv(gdsc_input, sep='\t')
    out_df = pivot_gdsc(data_full, 'AUC')
    out_df.to_csv(auc_out)


if __name__ == '__main__':
    # get_gdsc_log_ic50()
    get_gdsc_auc()
    prepare_dataset('data/input', 'gdsc')
