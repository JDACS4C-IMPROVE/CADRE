import cadre
import candle
import argparse
import subprocess

def initialize_parameters(config_path):
    # Build benchmark object
    cadre_common = cadre.CADRE(cadre.file_path,
                                config_path,
                                'torch')
                                #prog='cadre_mlp',
                                #desc='MNIST example')

    # Initialize parameters
    gParameters = candle.finalize_parameters(cadre_common)

    return gParameters

def run(gParameters):
    print(gParameters)
    subprocess.run(['python3', 'run_cf_candle.py', '--model_label', 'cntx-attn-gdsc', '--max_iter', str(gParameters['max_iter']), '--dropout_rate', str(gParameters["dropout_rate"]), '--learning_rate', str(gParameters["learning_rate"]), '--batch_size', str(gParameters["batch_size"]) ])
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file", help="File with model parameters", type=str, default='CADRE_default.txt')
    args = parser.parse_args()

    params = initialize_parameters(args.config_file)
    run(params)
