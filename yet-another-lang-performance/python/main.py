# -*- coding: UTF-8 -*-
import itertools

from tabulate import tabulate

from benchmarks.alternative_benchmarks import rwh_primes_benchmark, rwh_primesfrom2to_benchmark
from benchmarks.bad_benchmarks import primes_benchmark
from benchmarks.benchmark_collection import BenchmarkCollection

MAX_PRIME = 10000000

bad_benchmarks = BenchmarkCollection("Bad benchmarks", [
    primes_benchmark.PrimesBenchmark(MAX_PRIME)
]
                                     )
alternative_benchmarks = BenchmarkCollection("Alternative benchmarks", [
    rwh_primes_benchmark.RwhPrimesBenchmark(MAX_PRIME),
    rwh_primesfrom2to_benchmark.RwhPrimesFrom2toBenchmark(MAX_PRIME),

]
                                             )


def print_results(results: list):
    print(tabulate(map(lambda r: r.as_list(), results),
                   headers=['Name', 'Avg. elapsed time (s)', 'Avg max used memory (MB)', "Runs number"]))


if __name__ == "__main__":
    benchmark_results = []

    for bench in itertools.chain(bad_benchmarks, alternative_benchmarks):
        benchmark_results.append(bench.execute())

    print_results(benchmark_results)
