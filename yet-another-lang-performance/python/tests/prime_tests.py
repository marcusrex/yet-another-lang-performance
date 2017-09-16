import unittest

from benchmarks.alternative_benchmarks import rwh_primes_benchmark, rwh_primesfrom2to_benchmark
from benchmarks.bad_benchmarks import primes_benchmark

MAX_PRIME = 10000000


class TestPrimes(unittest.TestCase):
    def test_consistency(self):
        bad_primes_bench_hidden_results = primes_benchmark.PrimesBenchmark(MAX_PRIME).get_hidden_result()
        rwh_primes_bench_hidden_results = rwh_primes_benchmark.RwhPrimesBenchmark(MAX_PRIME).get_hidden_result()
        rwh_primesfrom2_bench_hidden_results = rwh_primesfrom2to_benchmark.RwhPrimesFrom2toBenchmark(
            MAX_PRIME).get_hidden_result()

        self.assertListEqual(bad_primes_bench_hidden_results, rwh_primes_bench_hidden_results)
        self.assertListEqual(bad_primes_bench_hidden_results, rwh_primesfrom2_bench_hidden_results)
