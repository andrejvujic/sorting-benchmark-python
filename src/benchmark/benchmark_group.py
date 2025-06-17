class BenchmarkGroup:
    def __init__(self, benchmarks):
        self.benchmarks = benchmarks

    def run(self):
        for b in self.benchmarks:
            b.run()
