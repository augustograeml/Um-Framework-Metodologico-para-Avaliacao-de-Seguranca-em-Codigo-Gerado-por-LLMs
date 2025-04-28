class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        return self.expression()

    def expression(self):
        node = self.term()
        while self.current_token() in ('+', '-'):
            token = self.current_token()
            self.advance()
            node = {'type': 'BinaryExpression', 'operator': token, 'left': node, 'right': self.term()}
        return node

    def term(self):
        node = self.factor()
        while self.current_token() in ('*', '/'):
            token = self.current_token()
            self.advance()
            node = {'type': 'BinaryExpression', 'operator': token, 'left': node, 'right': self.factor()}
        return node

    def factor(self):
        token = self.current_token()
        if token.isdigit():
            self.advance()
            return {'type': 'Literal', 'value': int(token)}
        elif token == '(':
            self.advance()
            node = self.expression()
            self.advance()  # Skip ')'
            return node
        raise Exception("Invalid syntax")

    def current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def advance(self):
        self.current_token_index += 1