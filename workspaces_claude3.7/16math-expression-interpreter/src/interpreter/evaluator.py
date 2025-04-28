class Evaluator:
    def __init__(self, ast):
        self.ast = ast

    def evaluate(self):
        return self._evaluate_node(self.ast)

    def _evaluate_node(self, node):
        if isinstance(node, int):
            return node
        elif isinstance(node, float):
            return node
        elif isinstance(node, str):
            raise ValueError(f"Unexpected node type: {node}")
        elif isinstance(node, dict):
            operator = node['operator']
            left = self._evaluate_node(node['left'])
            right = self._evaluate_node(node['right'])

            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                return left / right
            else:
                raise ValueError(f"Unknown operator: {operator}")
        else:
            raise ValueError(f"Invalid node: {node}")