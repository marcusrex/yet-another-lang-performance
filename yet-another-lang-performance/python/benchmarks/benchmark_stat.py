class BenchmarkStat:
    name = ""
    elapsed_time = 0.0
    run_number = 0

    def __init__(self, name: str, elapsed_time: float, runs_number: int):
        self.name = name
        self.elapsed_time = elapsed_time
        self.runs_number = runs_number

    def as_list(self) -> list:
        return [self.name, self.elapsed_time, self.runs_number]
