class Benchmark:
    name = ""

    def __init__(self, name: str):
        self.name = name

    def execute(self):
        raise NotImplemented()
