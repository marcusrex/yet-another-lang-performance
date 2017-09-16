import unittest

from benchmarks.alternative_benchmarks import numpy_spectral_norm
from benchmarks.bad_benchmarks import spectral_norm_benchmark

MAX_SPEC_NUM = 6


class TestSpectral(unittest.TestCase):
    def test_consistency(self):
        bad_alg_res = spectral_norm_benchmark.SpectralNormBenchmark(MAX_SPEC_NUM).get_hidden_result()
        good_alg_res = numpy_spectral_norm.NumpySpectralNorm(MAX_SPEC_NUM).get_hidden_result()
        self.assertAlmostEqual(bad_alg_res,good_alg_res)


if __name__ == '__main__':
    unittest.main()
