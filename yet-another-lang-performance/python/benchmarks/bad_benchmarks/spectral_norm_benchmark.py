import math

from benchmarks.benchmark import Benchmark


class SpectralNormBenchmark(Benchmark):
    spectral_num = 100

    @staticmethod
    def eval_A(i, j):
        return 1.0 / ((i + j) * (i + j + 1) / 2 + i + 1)

    @staticmethod
    def eval_A_times_u(u):
        args = ((i, u) for i in range(len(u)))
        return list(map(SpectralNormBenchmark.part_A_times_u, args))

    @staticmethod
    def eval_At_times_u(u):
        args = ((i, u) for i in range(len(u)))
        return list(map(SpectralNormBenchmark.part_At_times_u, args))

    @staticmethod
    def eval_AtA_times_u(u):
        return SpectralNormBenchmark.eval_At_times_u(SpectralNormBenchmark.eval_A_times_u(u))

    @staticmethod
    def part_A_times_u(xxx_todo_changeme):
        (i, u) = xxx_todo_changeme
        partial_sum = 0
        for j, u_j in enumerate(u):
            partial_sum += SpectralNormBenchmark.eval_A(i, j) * u_j
        return partial_sum

    @staticmethod
    def part_At_times_u(xxx_todo_changeme1):
        (i, u) = xxx_todo_changeme1
        partial_sum = 0
        for j, u_j in enumerate(u):
            partial_sum += SpectralNormBenchmark.eval_A(j, i) * u_j
        return partial_sum

    @staticmethod
    def __get_spectral_norm(n):
        u = [1] * n

        v = SpectralNormBenchmark.eval_AtA_times_u(u)
        u = SpectralNormBenchmark.eval_AtA_times_u(v)

        vBv = vv = 0

        for ue, ve in zip(u, v):
            vBv += ue * ve
            vv += ve * ve

        return math.sqrt(vBv/vv)

    def __init__(self, spectral_num: int):
        self.spectral_num = spectral_num
        super().__init__("Bad Spectral Norm")

    def _execute_impl(self):
        self.__get_spectral_norm(self.spectral_num)

    def get_hidden_result(self):
        return self.__get_spectral_norm(self.spectral_num)
