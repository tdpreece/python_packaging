import unittest
import greeter


class TestGreeter(unittest.TestCase):
    def test_greeting_is_given(self):
        self.assertEqual("Hello", greeter.greet())
