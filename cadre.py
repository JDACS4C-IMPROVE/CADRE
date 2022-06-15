import candle
import os


file_path = os.path.dirname(os.path.realpath(__file__))
required = None
additional_definitions = None


def downoad_data():
    candle.get_file('lincs1000.tsv', 'https://ftp.mcs.anl.gov/pub/candle/public/benchmarks/P1B1/lincs1000.tsv', datadir='./data')
    candle.get_file(fname='P3B1_data.tar.gz', origin='https://ftp.mcs.anl.gov/pub/candle/public/benchmarks/P3B1/P3B1_data.tar.gz', unpack=True, datadir='./data')

    candle.get_file('P1B1-train.csv', 'https://ftp.mcs.anl.gov/pub/candle/public/benchmarks/P1B1/P1B1.train.csv', datadir='./data')
    candle.get_file('P1B1-dev.csv', 'https://ftp.mcs.anl.gov/pub/candle/public/benchmarks/P1B1/P1B1.dev.train.csv', datadir='./data')

class CADRE(candle.Benchmark):
    required = None

    def set_locals(self):
        if required is not None:
            self.required = set(required)
        if additional_definitions is not None:
            self.additional_definitions = additional_definitions




