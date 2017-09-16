import numpy

from benchmarks.benchmark import Benchmark


class RwhPrimesFrom2toBenchmark(Benchmark):
    primes_number = 10

    @staticmethod
    def __primesfrom2to(n):
        """ https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188"""
        """ Input n>=6, Returns a array of primes, 2 <= p < n """
        sieve = numpy.ones(int(n / 3 + (n % 6 == 2)), dtype=numpy.bool)
        for i in range(1, int(int(n ** 0.5) / 3 + 1)):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[int(k * k / 3)::int(2 * k)] = False
                sieve[int(k * (k - 2 * (i & 1) + 4) / 3)::int(2 * k)] = False
        return numpy.r_[2, 3, ((3 * numpy.array(numpy.nonzero(sieve))[0][1:] + 1) | 1)]

    def __init__(self, primes_number: int):
        self.primes_number = primes_number
        super().__init__("RWH primesfrom2")

    def get_hidden_result(self):
        return self.__primesfrom2to(self.primes_number).tolist()

    def _execute_impl(self):
        self.__primesfrom2to(self.primes_number)
