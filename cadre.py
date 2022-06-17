import torch
import candle
import os


file_path = os.path.dirname(os.path.realpath(__file__))
required = None
additional_definitions = None


class CADRE(candle.Benchmark):
    required = None

    def set_locals(self):
        if required is not None:
            self.required = set(required)
        if additional_definitions is not None:
            self.additional_definitions = additional_definitions
