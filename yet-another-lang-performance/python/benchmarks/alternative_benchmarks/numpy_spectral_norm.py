import numpy

from benchmarks.benchmark import Benchmark


class NumpySpectralNorm(Benchmark):
    spectral_num = 100

    @staticmethod
    def __spectralnorm(n):
        u = numpy.matrix(numpy.ones(n))
        j = numpy.arange(n)
        eval_func = lambda i: 1.0 / ((i + j) * (i + j + 1) / 2 + i + 1)
        M = numpy.matrix([eval_func(i) for i in numpy.arange(n)])
        MT = M.T
        v = (u * MT) * M
        u = (v * MT) * M
        return (numpy.squeeze(numpy.asarray((sum(u*v.T)/sum(v*v.T)))))**0.5

    @staticmethod
    def __get_spectral_norm(n):
        return NumpySpectralNorm.__spectralnorm(n)

    def __init__(self, spectral_num: int):
        self.spectral_num = spectral_num
        super().__init__("Numpy spectral benchmark")

    def get_hidden_result(self):
        return self.__get_spectral_norm(self.spectral_num)

    def _execute_impl(self):
        self.__get_spectral_norm(self.spectral_num)
