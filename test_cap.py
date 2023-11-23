import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_word(self):
        text = 'hello python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Hello python')
        # self.assertEqual(result, 'Hello Python') # true for title method

if __name__ == '__main__':
    unittest.main()

