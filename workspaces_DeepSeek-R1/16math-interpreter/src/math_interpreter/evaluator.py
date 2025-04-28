class Evaluator:
    def __init__(self, ast):
        self.ast = ast

    def evaluate(self):
        return self._evaluate_node(self.ast)

    def _evaluate_node(self, node):
        if isinstance(node, int):
            return node
        elif isinstance(node, dict):
            operator = node['operator']
            left = self._evaluate_node(node['left'])
            right = self._evaluate_node(node['right'])
            return self._apply_operator(operator, left, right)
        raise ValueError("Invalid AST node")

    def _apply_operator(self, operator, left, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        raise ValueError(f"Unknown operator: {operator}")