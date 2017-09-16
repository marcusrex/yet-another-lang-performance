class BenchmarkCollection:
    name = ""
    __current = -1
    __benchmarks = []

    def __init__(self, name: str, benchmarks: list):
        self.name = name
        self.__benchmarks = benchmarks

    def __iter__(self):
        return iter(self.__benchmarks)
