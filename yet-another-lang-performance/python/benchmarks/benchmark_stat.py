class BenchmarkStat:
    name = ""
    avg_elapsed_time = 0.0
    run_number = 0

    def __init__(self, name: str, elapsed_time: float, avg_max_memory_usage: float, runs_number: int):
        self.name = name
        self.avg_elapsed_time = elapsed_time
        self.avg_max_memory_usage = avg_max_memory_usage
        self.runs_number = runs_number

    def as_list(self) -> list:
        return [self.name, self.avg_elapsed_time, self.avg_max_memory_usage, self.runs_number]
