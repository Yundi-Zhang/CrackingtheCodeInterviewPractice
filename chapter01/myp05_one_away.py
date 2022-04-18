import unittest, time
from collections import defaultdict

def one_away(str1: str, str2: str) -> bool:
    lst1, lst2 = list(str1), list(str2)
    # replace or the same
    if len(lst1) == len(lst2):
        return replace(lst1, lst2)
    # str1 inserts one character to str2
    if len(lst1) + 1 == len(lst2):
        return insert(lst1, lst2)
    # str1 removes one character to str2
    if len(lst1) == len(lst2) + 1:
        return insert(lst2, lst1)
    return False

def replace(lst1: list, lst2: list) -> bool:
    mark = False
    for c1, c2 in zip(lst1, lst2):
        if c1 != c2:
            if mark:
                return False
            mark = True
    return True

def insert(lst1: list, lst2: list) -> bool:
    """
    len(lst2) = len(lst1) + 1
    """
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return lst1[i:] == lst2[i+1:]
    return True

class Test_One_Away(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False)
    ]

    test_functions = [
        one_away
    ]

    def test_one_away(self):
        number_runs = 1000
        run_times = defaultdict(float)
        for _ in range(number_runs):
            for str1, str2, res in self.test_cases:
                for fctn in self.test_functions:
                    start = time.perf_counter()
                    out = fctn(str1, str2)
                    self.assertEqual(out, res)
                    run_times[fctn.__name__] += (time.perf_counter() - start) * 1000
        
        print(f"{number_runs} runs")
        for fctn, runtime in run_times.items():
            print(f"{fctn}: {runtime: .1f}ms")

if __name__ == '__main__':
    unittest.main()