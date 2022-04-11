import unittest

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

    def test_is_unique(self):
        for test_string, desired_output in self.test_cases:
            test_output = is_unique(test_string)
            self.assertEqual(test_output, desired_output)

if __name__ == '__main__':
    unittest.main()