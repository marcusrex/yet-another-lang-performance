from benchmarks.benchmark import Benchmark


class PrimesBenchmark(Benchmark):

    primes_number = 10

    @staticmethod
    def __get_primes7(n: int):
        """
        standard optimized sieve algorithm to get a list of prime numbers
        --- this is the function to compare your functions against! ---
        """
        if n < 2:
            return []
        if n == 2:
            return [2]

        s = list(range(3, n + 1, 2))
        # n**0.5 simpler than math.sqr(n)
        mroot = n ** 0.5
        half = len(s)
        i = 0
        m = 3
        while m <= mroot:
            if s[i]:
                j = (m * m - 3) // 2  # int div
                s[j] = 0
                while j < half:
                    s[j] = 0
                    j += m
            i = i + 1
            m = 2 * i + 3
        return [2] + [x for x in s if x]

    def __init__(self, primes_number: int):
        self.primes_number = primes_number
        super().__init__("Bad Primes Benchmark")

    def _execute_impl(self):
        self.__get_primes7(self.primes_number)

    def get_hidden_result(self):
        return self.__get_primes7(self.primes_number)