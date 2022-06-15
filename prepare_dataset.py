import pickle
from utils import load_dataset, split_dataset

def prepare_dataset(input_dir, repository, train_out='data/input/train.pkl', test_out='data/input/test.pkl', ptw_out='data/input/ptw_ids.pkl'):
    dataset, ptw_ids = load_dataset(input_dir=input_dir, repository=repository, drug_id=-1)
    train_set, test_set = split_dataset(dataset, ratio=0.8)
    pickle.dump(train_set, open(train_out, 'wb'))
    pickle.dump(test_set, open(test_out, 'wb'))
    pickle.dump(ptw_ids, open(ptw_out, 'wb'))
    print(dataset.keys())

if __name__ == '__main__':
    prepare_dataset('data/input', 'gdsc')
