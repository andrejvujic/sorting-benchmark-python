from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.merge_sort import merge_sort
from src.algorithms.selection_sort import selection_sort
from src.benchmark.benchmark import Benchmark
from src.benchmark.benchmark_group import BenchmarkGroup

BenchmarkGroup(
    benchmarks=[
        Benchmark(
            funcs=[sorted, merge_sort, selection_sort, bubble_sort],
        ).generate_arr(arr_length=100, lower_bound=-10_000, upper_bound=10_000),
        Benchmark(
            funcs=[sorted, merge_sort, selection_sort, bubble_sort],
        ).generate_arr(arr_length=1000, lower_bound=-10_000, upper_bound=10_000),
        Benchmark(
            funcs=[sorted, merge_sort, selection_sort, bubble_sort],
        ).generate_arr(arr_length=10_000, lower_bound=-10_000, upper_bound=10_000),
        Benchmark(
            funcs=[sorted, merge_sort, selection_sort, bubble_sort],
        ).generate_arr(arr_length=100_000, lower_bound=-10_000, upper_bound=10_000),
        Benchmark(
            funcs=[sorted, merge_sort, selection_sort, bubble_sort],
        ).generate_arr(arr_length=1_000_000, lower_bound=-10_000, upper_bound=10_000)
    ]
).run()
