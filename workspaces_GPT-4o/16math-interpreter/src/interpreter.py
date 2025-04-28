class Interpreter:
    def __init__(self, parser, evaluator):
        self.parser = parser
        self.evaluator = evaluator

    def interpret(self, expression: str) -> float:
        tokens = self.parser.parse(expression)
        result = self.evaluator.evaluate(tokens)
        return result