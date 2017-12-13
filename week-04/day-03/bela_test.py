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

if __name__ == '__main__':
    unittest.main()
