import unittest, time
from collections import defaultdict

def string_compression(string: str) -> str:
    if string == '':
        return string

    char_lst = [string[0]]
    num_lst =[1]
    N = len(string)
    for i in range(1, N):
        if string[i] != char_lst[-1]:
            char_lst.append(string[i])
            num_lst.append(1)
        else:
            num_lst[-1] += 1
    
    if len(char_lst) * 2 >= N:
        return string
    else:
        cps_lst = ""
        for i in range(len(char_lst)):
            cps_lst += char_lst[i]
            cps_lst += str(num_lst[i])
        return cps_lst

def update_str_compre(string: str) -> str:
    counter = 0
    cps_lst = []
    
    for i in range(len(string)):
        if i != 0 and string[i-1] != string[i]:
            cps_lst.append(string[i-1] + str(counter))
            counter = 0
        counter += 1

    if counter:
        cps_lst.append(string[-1] + str(counter))
    
    return min(string, "".join(cps_lst), key=len)

class Test_String_Compression(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aaaabbbbccccsskia", "a4b4c4s2k1i1a1"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    test_functions = [
        string_compression,
        update_str_compre
    ]

    def test_one_away(self):
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