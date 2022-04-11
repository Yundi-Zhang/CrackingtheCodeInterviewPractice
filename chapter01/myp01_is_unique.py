import unittest
import time
from collections import defaultdict

def is_unique(string):
    if len(string) > 128:
        return False

    return len(set(string)) == len(string)

class test_IsUnique(unittest.TestCase):
    test_cases = [
        ("string", True),
        ("ppp", False),
        ("abjdielsma", False)
    ]

    test_functions = [
        is_unique
    ]

    def test_is_unique(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for test_string, desired_output in self.test_cases:
                for test_function in self.test_functions:
                    start_time = time.perf_counter()
                    test_output = test_function(test_string)
                    self.assertEqual(test_output, desired_output)
                    function_runtimes[test_function.__name__] += (
                        time.perf_counter() - start_time
                    ) * 1000
        
        print(f"\n{num_runs} runs")
        print(function_runtimes)
        for function_name, run_time in function_runtimes.items():
            print(f"{function_name}: {run_time:.1f}ms")
        

if __name__ == '__main__':
    unittest.main()