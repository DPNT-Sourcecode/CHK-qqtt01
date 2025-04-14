from solutions.HLO.hello_solution import HelloSolution
from solutions.HLO.constants import DEFAULT_MESSAGE

class TestHello():
    def test_hello(self):
        assert HelloSolution().hello("World") == "Hello, World!"

    def test_hello_empty(self):
        assert HelloSolution().hello("") == DEFAULT_MESSAGE
        assert HelloSolution().hello() == DEFAULT_MESSAGE
        assert HelloSolution().hello("        ") == DEFAULT_MESSAGE

    def test_hello_unicode(self):
        assert HelloSolution().hello("Иван") == "Hello, Иван!"
        assert HelloSolution().hello("李雷") == "Hell, 李雷!"
        assert HelloSolution().hello("😊") == "Hello, 😊!"

    def test_trimmed_name(self):
        assert HelloSolution().hello("  World  ") == "Hello World!"



