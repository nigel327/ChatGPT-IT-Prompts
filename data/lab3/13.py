import unittest

def compute(a, b):
    if type(a) not in [int, float]:
        raise TypeError("Input must be a number.")
    return abs(a)

class TestCompute(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(compute(1, None), 1)
        self.assertEqual(compute(1.2, None), 1.2)
        self.assertEqual(compute(0.99, None), 0.99)
    
    def test_negative_numbers(self):
        self.assertEqual(compute(-1, None), 1)
        self.assertEqual(compute(-1.2, None), 1.2)
        self.assertEqual(compute(-0.99, None), 0.99)
    
    def test_zero(self):
        self.assertEqual(compute(0, None), 0)
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            compute(None, None)
        with self.assertRaises(TypeError):
            compute([], None)
        with self.assertRaises(TypeError):
            compute({}, None)

if __name__ == '__main__':
    unittest.main()
