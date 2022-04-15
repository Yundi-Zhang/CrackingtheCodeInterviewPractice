import unittest
import time
from collections import defaultdict

def urlify_pythonic(text: str, length: int) -> str:
    return text[:length].replace(" ", "%20")

def urlify_algo(text: str, length: int) -> str:
    """
    Replaces the white spaces with "%20" and removes trailing spaces.
    """
    cropped_txt = text[:length]
    replaced_txt = str()
    for char in cropped_txt:
        if char == " ":
            replaced_txt += "%20"
        else:
            replaced_txt += char
    return replaced_txt

class Test_urlify(unittest.TestCase):
    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
        (" a b ", 4): "%20a%20b"
    }

    test_functions = [
        urlify_pythonic,
        urlify_algo
    ]

    def test_urlify(self):
        number_runs = 1000
        runtimes = defaultdict(float)
        for _ in range(number_runs):
            for fctn in self.test_functions:
                for args, output in self.test_cases.items():
                    start = time.perf_counter()
                    res = fctn(*args)
                    self.assertEqual(res, output)
                    runtimes[fctn.__name__] += (time.perf_counter() - start) * 1000
        
        print(f"{number_runs} runs")
        for fctn_name, run_time in runtimes.items():
            print(f"{fctn_name}: {run_time: .1f}ms")

if __name__ == '__main__':
    unittest.main()