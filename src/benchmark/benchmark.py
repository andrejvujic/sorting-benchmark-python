import os
import pickle
import time
from random import randint


def execution_time_logging(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()

        print(f"{(end_time - start_time) * 1000} ms")
        return result
    return wrapper


class Benchmark:
    def __init__(self, funcs):
        self.funcs = funcs
        self.arr = None

    def load_arr_from_pf(self, path):
        if not os.path.exists(path):
            raise RuntimeError("The provided path doesn't exist!")

        with open(path, "rb") as f:
            self.arr = pickle.load(f)

        return self

    def generate_arr(self, arr_length, lower_bound, upper_bound):
        if not upper_bound or not lower_bound or not arr_length:
            raise RuntimeError(
                "Invalid generate_arr method call! Missing arguments.")

        self.arr = Benchmark.randomize_arr(
            arr_length, lower_bound=lower_bound, upper_bound=upper_bound
        )

        return self

    @staticmethod
    def randomize_arr(length, lower_bound, upper_bound):
        return [randint(lower_bound, upper_bound) for _ in range(0, length)]

    def run(self):
        print(
            f"[Benchmark] RUNNING with arr_length={len(self.arr)}",
            end="\n\n"
        )

        for func in self.funcs:
            self.run_benchmark_on_func(func)

        print(
            f"\n[Benchmark] COMPLETED.", end="\n\n\n"
        )

    def run_benchmark_on_func(self, func):
        print(f"{func.__name__}:", end=" ")
        arr = list(self.arr)

        @execution_time_logging
        def _run(arr):
            func(arr)

        _run(arr)
