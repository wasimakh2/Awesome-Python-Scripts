import unittest

from framed_text import generate_framed_text


class TestFramedText(unittest.TestCase):
    def test_generate_framed_text_empty_input(self):
        # Test case for empty input lines of text
        input_lines = []
        expected_output = ""
        self.assertEqual(generate_framed_text(input_lines), expected_output)

    def test_generate_framed_text_single_line(self):
        # Test case for single-line input text
        input_lines = ["Hello, World!"]
        expected_output = "+--------------+\n| Hello, World! |\n+--------------+"
        self.assertEqual(generate_framed_text(input_lines), expected_output)

    def test_generate_framed_text_multi_line(self):
        # Test case for multi-line input text
        input_lines = ["Hello", "World"]
        expected_output = "+-------+\n| Hello |\n| World |\n+-------+"
        self.assertEqual(generate_framed_text(input_lines), expected_output)

    def test_generate_framed_text_special_characters(self):
        # Test case for special characters in the input text
        input_lines = ["!@#$%^&*()"]
        expected_output = "+-------------+\n| !@#$%^&*() |\n+-------------+"
        self.assertEqual(generate_framed_text(input_lines), expected_output)

    def test_generate_framed_text_long_input_lines(self):
        # Test case for long input lines of text
        input_lines = ["This is a long line of text that exceeds the maximum width of the frame"]
        expected_output = "+----------------------------------------------------+\n| This is a long line of text that exceeds the maximum |\n| width of the frame                                  |\n+----------------------------------------------------+"
        self.assertEqual(generate_framed_text(input_lines), expected_output)

if __name__ == "__main__":
    unittest.main()
