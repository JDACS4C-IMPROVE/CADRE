import torch
import candle
import os


file_path = os.path.dirname(os.path.realpath(__file__))
required = None
additional_definitions = [
    {
        "name": "attention_head",
        "type": int,
        "help": "number of attention heads",
    },
    {
        "name": "attention_size",
        "type": int,
        "help": "size of attention parameter beta_j",
    },
    {
        "name": "drug_id",
        "type": int,
        "help": "the index of drug to be predicted in STL, -1 if MTL",
    },
    {
        "name": "embedding_dim",
        "type": int,
        "help": "embedding dimension",
    },
    {
        "name": "hidden_dim_enc",
        "type": int,
        "help": "dimension of hidden layer in encoder",
    },
    {
        "name": "init_gene_emb",
        "type": bool,
        "help": "whether to use pretrained gene embedding or not",
    },
    {
        "name": "max_iter",
        "type": int,
        "help": "maximum number of training iterations",
    },
    {
        "name": "omic",
        "type": str,
        "help": "type of omics data, can be exp, mut, cnv, met, mul",
    },
    {
        "name": "ptw_ids",
        "type": str,
        "help": "Obscure mandatory parameter",
    },
    {
        "name": "repository",
        "type": str,
        "help": "data to be analyzed, can be gdsc",
    },
    {
        "name": "test_batch_size",
        "type": int,
        "help": "test batch size",
    },
    {
        "name": "test_inc_size",
        "type": int,
        "help": "increment interval size between log outputs",
    },
    {
        "name": "use_attention",
        "type": bool,
        "help": "whether to use attention mechanism or not",
    },
    {
        "name": "use_cntx_attn",
        "type": bool,
        "help": "whether to use contextual attention or not",
    },
    {
        "name": "use_cuda",
        "type": bool,
        "help": "whether to use GPU or not",
    },
    {
        "name": "use_hid_lyr",
        "type": bool,
        "help": "whether to use hidden layer in the encoder or not",
    },
    {
        "name": "use_relu",
        "type": bool,
        "help": "whether to use relu or not",
    },
    {
        "name": "weight_decay",
        "type": float,
        "help": "coefficient of l2 regularizer",
    }
]


class CADRE(candle.Benchmark):
    required = None

    def set_locals(self):
        if required is not None:
            self.required = set(required)
        if additional_definitions is not None:
            self.additional_definitions = additional_definitions
