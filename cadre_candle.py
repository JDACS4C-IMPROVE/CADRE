import os
import cadre
import candle
import argparse
import subprocess
import pickle
import torch


from collabfilter import CF
from utils import fill_mask, bool_ext, load_dataset, split_dataset


def initialize_parameters(default_model='CADRE_default.txt'):
    # Build benchmark object
    cadre_common = cadre.CADRE(cadre.file_path,
                               default_model,
                               'torch',
                               prog='cadre_mlp',
                               desc='CADRE drug response prediction model')

    # Initialize parameters
    gParameters = candle.finalize_parameters(cadre_common)

    return gParameters


def load_data(args):
    print("Loading drug dataset...")
    train_set = pickle.load(open(args['train_set'], 'rb'))
    test_set = pickle.load(open(args['test_set'], 'rb'))
    ptw_ids = pickle.load(open(args['ptw_ids'], 'rb'))
    return train_set, test_set, ptw_ids


def run(args):
    print(args)

    args['use_cuda'] = args['use_cuda'] and torch.cuda.is_available()
    train_set, test_set, ptw_ids = load_data(args)

    # replace tgt in train_set
    train_set['tgt'], train_set['msk'] = fill_mask(
        train_set['tgt'], train_set['msk'])

    args['exp_size'] = train_set['exp_bin'].shape[1]
    args['mut_size'] = train_set['mut_bin'].shape[1]
    args['cnv_size'] = train_set['cnv_bin'].shape[1]
    args['drg_size'] = train_set['tgt'].shape[1]

    if args['omic'] == 'exp':
        args['omc_size'] = args['exp_size']
    elif args['omic'] == 'mut':
        args['omc_size'] = args['mut_size']
    elif args['omic'] == 'cnv':
        args['omc_size'] = args['cnv_size']

    args['train_size'] = len(train_set['tmr'])
    args['test_size'] = len(test_set['tmr'])

    print(args)

    model = CF(args)
    model.build(ptw_ids)

    if args['use_cuda']:
        model = model.cuda()

    logs = {'args': args, 'iter': [],
            'precision': [], 'recall': [],
            'f1score': [], 'accuracy': [], 'auc': [],
            'precision_train': [], 'recall_train': [],
            'f1score_train': [], 'accuracy_train': [], 'auc_train': [],
            'loss': [], 'ptw_ids': ptw_ids}

    if args['is_train']:
        print("Training...")
        logs = model.train(train_set, test_set,
                           batch_size=args['batch_size'],
                           test_batch_size=args['test_batch_size'],
                           max_iter=args['max_iter'],
                           test_inc_size=args['test_inc_size'],
                           logs=logs)

        labels, msks, preds, tmr, amtr = model.test(
            test_set, test_batch_size=args['test_batch_size'])
        labels_train, msks_train, preds_train, tmr_train, amtr_train = model.test_train(
            train_set, test_batch_size=args['test_batch_size'])

        logs["preds"] = preds
        logs["msks"] = msks
        logs["labels"] = labels
        logs['tmr'] = tmr
        logs['amtr'] = amtr

        logs['preds_train'] = preds_train
        logs['msks_train'] = msks_train
        logs['labels_train'] = labels_train
        logs['tmr_train'] = tmr_train
        logs['amtr_train'] = amtr_train

    else:
        print("LR finding...")
        logs = model.find_lr(train_set, test_set,
                             batch_size=args['batch_size'],
                             test_batch_size=args['test_batch_size'],
                             max_iter=args['max_iter'],
                             test_inc_size=args['test_inc_size'],
                             logs=logs)

    for trial in range(0, 100):
        if os.path.exists("data/output/cf-rep/logs"+str(trial)+".pkl"):
            continue
    print(trial)
    with open("data/output/cf/logs"+str(trial)+".pkl", "wb") as f:
        pickle.dump(logs, f, protocol=2)

    return None


def main():
    gParameters = initialize_parameters()
    run(gParameters)


if __name__ == "__main__":
    main()
    try:
        torch.cuda.empty_cache()
    except AttributeError:
        pass
