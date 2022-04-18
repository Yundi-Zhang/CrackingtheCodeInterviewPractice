import unittest
from collections import defaultdict, Counter
import time
import string

# O(N) (also the time complexity of the collections.Counter())
def palindrome_permutation(text: str) -> bool:
    counter = Counter(text.lower())
    single_num = 0
    for char, num in counter.items():
        if char.isalpha():
            if num%2 != 0:
                single_num += 1
                if single_num > 1:
                    return False
    return True

# O(N)
def palindrome_permutation_no_Counter(text: str) -> bool:
    clean_char = [ c for c in text.lower() if c in string.ascii_lowercase]
    counter = {}
    for c in clean_char:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    
    return sum(count%2 for count in counter.values()) <= 1

# O(N)
def palindrome_permutation_bit_vector(text: str) -> bool:
    clean_char = [ c for c in text.lower() if c in string.ascii_lowercase]
    r = 0
    for c in clean_char:
        val = ord(c)
        mask = 1 << val
        if r & mask:
            r &= ~mask
        else:
            r |= mask
    
    return (r-1) & r == 0

class Test_Palindrome_Permutation(unittest.TestCase):
    test_cases = [
        ("Tact Coa", True),
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True)
    ]

    test_functions = [
        palindrome_permutation,
        palindrome_permutation_no_Counter,
        palindrome_permutation_bit_vector
    ]

    def test_palindrome_permutation(self):
        number_runs = 1000
        runtimes = defaultdict(float)
        for _ in range(number_runs):
            for case, res in self.test_cases:
                for fctn in self.test_functions:
                    start = time.perf_counter()
                    output = fctn(case)
                    self.assertEqual(output, res)
                    runtimes[fctn.__name__] += (time.perf_counter() - start) * 1000
            
        print(f"{number_runs} runs")
        for fctn, runtime in runtimes.items():
            print(f"{fctn}: {runtime: .1f}ms")

if __name__ == '__main__':
    unittest.main()