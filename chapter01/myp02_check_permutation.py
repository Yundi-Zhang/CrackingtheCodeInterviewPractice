import unittest
import time
from collections import defaultdict, Counter

def check_permutation(string1 :str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    str1, str2 = sorted(string1), sorted(string2)
    return str1 == str2

def check_permutation_counter(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

def check_permutation_by_count(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    # when the lengths are the same, if the counts are the same, then two strings are the permutation of each other.
    counter = [0] * 128 # assume that the character set is ASCII (0 - 127)
    for char1 in str1:
        counter[ord(char1)] += 1
    for char2 in str2:
        if counter[ord(char2)] == 0:
            return False
        counter[ord(char2)] -= 1
    return True

class Test_Permutation(unittest.TestCase):
    test_cases = [
        ("asdfgh", "sadfgh", True),
        ("as", "as", True),
        ("c", "cd", False),
        ("@sdf*", "sdddf", False),
        ("AS", "as", False),
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False)
    ]

    test_functions = [
        check_permutation,
        check_permutation_counter,
        check_permutation_by_count
    ]

    def test_permutation(self):
        num_runs = 1000
        run_times = defaultdict(float)
        for _ in range(num_runs):
            for fctn in self.test_functions:
                for str1, str2, res in self.test_cases:
                    start = time.perf_counter()
                    output = fctn(str1, str2)
                    self.assertEqual(output, res)
                    run_times[fctn.__name__] += (
                        time.perf_counter() - start
                    ) * 1000                                        # 1000 is for the ms
        
        print(f"\n{num_runs} runs")
        for fctn_name, run_time in run_times.items():
            print(f"{fctn_name}: {run_time:.1f}ms")

if __name__ == '__main__':
    unittest.main()