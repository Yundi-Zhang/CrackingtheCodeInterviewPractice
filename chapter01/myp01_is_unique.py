import unittest
import time
from collections import defaultdict

### my functions
def is_unique_set(string):
    if len(string) > 128:
        return False
    return len(set(string)) == len(string)

def is_unique_char(string):
    if len(string) > 128:
        return False   
    char_check = [False] * 128
    for char in string:
        # set the value at the unicode of character to True
        if char_check[ord(char)]:
            return False
        else:
            char_check[ord(char)] = True
    return True

def is_unique_dictionary(string: str) -> bool:
    if len(string) > 128:
        return False
    char_check = {}
    for char in string:
        if char in char_check:
            return False
        char_check[char] = 1
    return True

def is_unique_using_set(string: str) -> bool:
    if len(string) > 128:
        return False
    char_check = set()
    for char in string:
        if char in char_check:
            return False
        char_check.add(char)
    return True

def is_unique_chars_sorting(string: str) -> bool:
    char_sorted = sorted(string)
    N = len(char_sorted)
    for i in range(N-1):
        if char_sorted[i] == char_sorted[i+1]:
            return False
    return True

def is_unique_bit(string: str) -> bool:
    checker = 0
    for char in string:
        val = ord(char)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True

### unit test
class test_IsUnique(unittest.TestCase):
    test_cases = [
        ("string", True),
        ("ppp", False),
        ("abjdielsma", False),
        ("mynaeis jo@()#$%p", True)
    ]

    test_functions = [
        is_unique_set,
        is_unique_char,
        is_unique_dictionary,
        is_unique_using_set,
        is_unique_chars_sorting,
        is_unique_bit
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
        # print(function_runtimes)
        for function_name, run_time in function_runtimes.items():
            print(f"{function_name}: {run_time:.1f}ms")
        

if __name__ == '__main__':
    unittest.main()