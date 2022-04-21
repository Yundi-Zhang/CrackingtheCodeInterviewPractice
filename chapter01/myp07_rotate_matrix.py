import unittest, time
from collections import defaultdict

def rotate_matrix(matrix):
    N = len(matrix)
    rotated = [[0] * N for _ in range(N)]
    for m in range(N):
        for n in range(N):
            rotated[n][N-1-m] = matrix[m][n]
    return rotated

def rotate_matrix_pythonic(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]

class Test_Rotate_Matrix(unittest.TestCase):
    
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    test_functions = [
        rotate_matrix,
        rotate_matrix_pythonic
    ]

    def test_rotate_matrix(self):
        number_runs = 1000
        run_times = defaultdict(float)
        for _ in range(number_runs):
            for case, res in self.test_cases:
                for fctn in self.test_functions:
                    start = time.perf_counter()
                    out = fctn(case)
                    self.assertEqual(out, res)
                    run_times[fctn.__name__] += (time.perf_counter() - start) * 1000
        
        print(f"{number_runs} runs")
        for fctn, runtime in run_times.items():
            print(f"{fctn}: {runtime: .1f}ms")

if __name__ == '__main__':
    unittest.main()