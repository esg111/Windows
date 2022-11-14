import inspect
import unittest

from ch12.LanguageResources import I18N


class Calculator:
    def __init__(self):
        print('\nCalculator init')

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def __del__(self):
        print("Calculator delete")

class GuiUnitTests(unittest.TestCase):

    def test_TitleIsEnglish(self):
        i18n = I18N('en')
        self.assertEqual(i18n.title,
                         "Python Graphical User Interface")

    def test_TitleIsKorean(self):
        i18n = I18N('ko')
        self.assertEqual(i18n.title, "파이썬 그래픽 사용자 인터페이스")

class TestCase101(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()

    def test_plus(self):
        assert self.cal.add(3, 4) == 7
        print(f'{inspect.stack()[0][3]}() is pass')

    def test_multiply(self):
        assert \
            self.cal.multiply(3, 4) == 12
        print(f'{inspect.stack()[0][3]}() is pass')

    def tearDown(self):
        del self.cal
