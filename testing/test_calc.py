from unittest import TestCase, main
from main import Calc


class CalcTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        a = 4
        b = 2
        cls.c = Calc(a, b)
        print('Setup')

    def test_sum(self):
        expected_result = 6
        self.assertEqual(expected_result, self.c.sum())
        print('test_sum')

    def test_divide(self):
        expected_result = 2
        self.assertEqual(expected_result, self.c.divide())
        print('test_divide')

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.c
        print('teardown')


if __name__ == '__main__':
    main()