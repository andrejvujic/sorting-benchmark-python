I did a small benchmark on the performance of my hand-written <code>merge_sort</code>, <code>selection_sort</code> and <code>bubble_sort</code> algorithms in comparison to Python's built-in <code>sorted</code> function which uses <a href="https://en.m.wikipedia.org/wiki/Timsort">Timsort</a> under the hood.

## Benchmark results
<table>
<tr>
    <td>Elements</td>
    <td>100</td>
    <td>1,000</td>
    <td>10,000</td>
    <td>100,000</td>
    <td>1,000,000</td>
<tr>
<tr>
    <td><code>sorted</code></td>
    <td>9 µs</td>
    <td>68 µs</td>
    <td>1 ms</td>
    <td>11 ms</td>
    <td>127 ms</td>
</tr>
<tr>
    <td><code>merge_sort</code></td>
    <td>0.12 ms</td>
    <td>1.24 ms</td>
    <td>15 ms</td>
    <td>181 ms</td>
    <td>2.1 s</td>
</tr>
<tr>
    <td><code>selection_sort</code></td>
    <td>0.1 ms</td>
    <td>11 ms</td>
    <td>1.1 s</td>
    <td>1 m 50 s</td>
    <td>∞</td>
</tr>
<tr>
    <td><code>bubble_sort</code></td>
    <td>0.2 ms</td>
    <td>24 ms</td>
    <td>2.6 s</td>
    <td>4 m 35 s</td>
    <td>∞</td>
</tr>
</table>
