# -*- coding: UTF-8 -*-
from tabulate import tabulate

from benchmarks.bad_benchmarks import primes_benchmark
from benchmarks.benchmark_collection import BenchmarkCollection

MAX_PRIME = 10000000

bad_benchmarks = BenchmarkCollection("Bad benchmarks",
                                     [
                                         primes_benchmark.PrimesBenchmark(MAX_PRIME)
                                     ]
                                     )


def print_results(results: list):
    print(tabulate(map(lambda r: r.as_list(), results), headers=['Name', 'Avg. elapsed time (s)', "Runs number"]))


if __name__ == "__main__":
    benchmark_results = []

    for bench in bad_benchmarks:
        benchmark_results.append(bench.execute())

    print_results(benchmark_results)
