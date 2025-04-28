class Evaluator:
    def evaluate(self, tokens: list) -> float:
        def apply_operator(operators, values):
            right = values.pop()
            left = values.pop()
            operator = operators.pop()
            if operator == '+':
                values.append(left + right)
            elif operator == '-':
                values.append(left - right)
            elif operator == '*':
                values.append(left * right)
            elif operator == '/':
                values.append(left / right)

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        operators = []
        values = []
        
        for token in tokens:
            if isinstance(token, (int, float)):
                values.append(token)
            elif token in precedence:
                while (operators and operators[-1] in precedence and
                       precedence[operators[-1]] >= precedence[token]):
                    apply_operator(operators, values)
                operators.append(token)
        
        while operators:
            apply_operator(operators, values)

        return values[0] if values else 0.0