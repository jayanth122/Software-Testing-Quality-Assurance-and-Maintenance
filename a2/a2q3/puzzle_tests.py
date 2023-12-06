import unittest

from a2q3.magic_square import solve_magic_square

class PuzzleTests(unittest.TestCase):

    def setUp(self):
        """Reset Z3 context between tests"""
        import z3
        z3._main_ctx = None

    def tearDown(self):
        """Reset Z3 context after test"""
        import z3
        z3._main_ctx = None

    def test_1(self):
        res = solve_magic_square(3, 1, 1, 5)
        self.assertIsNotNone(res)
        self.assertEqual(sum([res[0][j] for j in range(3)]), 15)
        self.assertEqual(sum([res[1][j] for j in range(3)]), 15)
        self.assertEqual(sum([res[2][j] for j in range(3)]), 15)
        self.assertEqual(sum([res[i][0] for i in range(3)]), 15)
        self.assertEqual(sum([res[i][1] for i in range(3)]), 15)
        self.assertEqual(sum([res[i][2] for i in range(3)]), 15)
        self.assertEqual(sum([res[i][i] for i in range(3)]), 15)
        self.assertEqual(sum([res[i][3 - i - 1] for i in range(3)]), 15)

        print("Test 1 Result:")
        self.print_square(res)

    def test_2(self):
        n = 3
        r = 2
        c = 0
        val = 8
        res = solve_magic_square(n, r, c, val)
        self.assertIsNotNone(res)

        print("Test 2 Result:")
        self.print_square(res)

    def test_3(self):
        n = 3
        r = 1
        c = 1
        val = 7
        res = solve_magic_square(n, r, c, val)
        self.assertIsNone(res)

        print("Test 3 Result: No solution!")

    def print_square(self, square):
        '''
        Prints a magic square as a square on the console
        '''
        n = len(square)
        assert n > 0
        for i in range(n):
            assert len(square[i]) == n

        for i in range(n):
            line = []
            for j in range(n):
                line.append(str(square[i][j]))
            print('\t'.join(line))

if __name__ == '__main__':
    unittest.main()
