from solutions.HLO.hello_solution import HelloSolution


class TestHello():
    def test_hello(self):
        assert HelloSolution().hello("World") == "Hello World!"

    def test_hello_empty(self):
        assert HelloSolution().hello("") == "Hi there!"

