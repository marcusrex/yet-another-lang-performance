import time

from benchmarks.benchmark_stat import BenchmarkStat
from benchmarks.constants import RETRY_NUMBER


class Benchmark:
    name = ""

    def __init__(self, name: str):
        self.name = name

    def _execute_impl(self):
        raise NotImplemented()

    def execute(self) -> BenchmarkStat:
        times = []
        for _ in range(RETRY_NUMBER):
            start = time.perf_counter()
            self._execute_impl()
            end = time.perf_counter()
            times.append(end - start)
        return BenchmarkStat(self.name, sum(times) / RETRY_NUMBER, RETRY_NUMBER)
