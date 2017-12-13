import unittest
from bela_work import Apple

class TestBelaWork(unittest.TestCase):


    def test_get_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "apple")


    def test_summa_empty_list(self):
        apple = Apple()
        test_list = []
        self.assertEqual(apple.summa(test_list), 0)


    def test_summa_one_number(self):
        apple = Apple()
        test_list = [2]
        self.assertEqual(apple.summa(test_list), 2)


    def test_summa_multiple_numbers(self):
        apple = Apple()
        test_list = [2, 4, 5]
        self.assertEqual(apple.summa(test_list), 11)


    def test_summa_null(self):
        apple = Apple()
        test_list = ["null"]
        self.assertEqual(apple.summa(test_list), "Enter a list of numbers")


    def test_anagram_empty_strings(self):
        apple = Apple()
        self.assertEqual(apple.anagram("", ""), True)
    

    def test_anagram_one_letter_strings(self):
        apple = Apple()
        self.assertFalse(apple.anagram("a", "b"))

    
    def test_anagram_multiple_letter_strings(self):
        apple = Apple()
        self.assertEqual(apple.anagram("abcde", "badec"), True)


    def test_count_letters_empty_string(self):
        apple = Apple()
        test_dict = {}
        self.assertEqual(apple.count_letters(""), test_dict)


    def test_count_letters_one_char_string(self):
        apple = Apple()
        test_dict = {"a":1}
        self.assertEqual(apple.count_letters("a"), test_dict)


    def test_count_letters_multiple_char_string(self):
        apple = Apple()
        test_dict = {"a": 1, "b": 1, "c": 1, "d": 1}
        self.assertEqual(apple.count_letters("abcd"), test_dict)


    def test_count_letters_multiple_char_string_returning_char(self):
        apple = Apple()
        test_dict = {"a": 2, "b": 3, "c": 1, "d": 4}
        self.assertEqual(apple.count_letters("bcdbddbada"), test_dict)
        

    def test_fibonacci_number_input(self):
        apple = Apple()
        self.assertEqual(apple.fibonacci(1), 1)


    def test_fibonacci_negative_number_input(self):
        apple = Apple()
        self.assertEqual(apple.fibonacci(-1), "Please enter a non-negative integer")
    

    def test_fibonacci_string_input(self):
        apple = Apple()
        self.assertEqual(apple.fibonacci("do oo o"), "Please enter a non-negative integer")

if __name__ == '__main__':
    unittest.main()
