from unittest import TestCase, main
from tdd_practice_001 import (
    increment_string,
    count_letters,
    sum_consecutives,
    count_unique,
)


class TestIcrementString(TestCase):

    def test_append_one(self):
        string1 = ""
        string2 = "abcd"
        self.assertEqual(increment_string(string1), "1")
        self.assertEqual(increment_string(string2), "abcd1")

    def test_add_one(self):
        string1 = "abcde123"
        string2 = "0123"
        self.assertEqual(increment_string(string1), "abcde124")
        self.assertEqual(increment_string(string2), "0124")

    def test_none(self): ...


class TestCountLetters(TestCase):

    def test_count_empty(self):
        """count letter in an empty string"""
        self.assertDictEqual(count_letters(""), {})

    def test_count_letters(self):
        string = "karabo"
        string1 = "string is None, "
        self.assertDictEqual(
            count_letters(string), {"k": 1, "a": 2, "r": 1, "b": 1, "o": 1}
        )
        self.assertDictEqual(
            count_letters(string1),
            {
                "s": 2,
                "t": 1,
                "r": 1,
                "n": 3,
                "g": 1,
                "i": 2,
                "o": 1,
                "e": 1,
                " ": 3,
                ",": 1,
            },
        )

    def test_type_return(self):
        "Testing if it return a dictionary"
        self.assertIsInstance(count_letters(""), dict)


class TestSumConsecutives(TestCase):

    def test_empty_list(self):
        self.assertListEqual(sum_consecutives([]), [])

    def test_returned_type(self):
        "Testing if it return a list"
        self.assertIsInstance((sum_consecutives([])), list)

    def test_mixed_list(self):
        with self.assertRaises(ValueError):
            sum_consecutives([1, 23.23, "gmail"])

    def test_num_list(self):
        self.assertListEqual(sum_consecutives([2, 3, 5, 6]), [5, 8, 11])
        self.assertListEqual(sum_consecutives([0.5, 1]), [1.5])


class TestCountUnique(TestCase): ...


if __name__ == "__main__":
    main(verbosity=2)
