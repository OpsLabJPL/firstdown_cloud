from unittest import TestCase

from hello import Hello


class TestHello(TestCase):
    def test_hello(self):
        hello = Hello()
        self.assertEqual(hello.hello(), "Hello, world!")
