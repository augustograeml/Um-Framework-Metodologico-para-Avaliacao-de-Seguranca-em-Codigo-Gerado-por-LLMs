class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.position = 0
        self.current_char = self.expression[self.position] if self.expression else None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.position += 1
        if self.position > len(self.expression) - 1:
            self.current_char = None
        else:
            self.current_char = self.expression[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def variable(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return ('VARIABLE', result)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return ('NUMBER', int(result))

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isalpha():
                tokens.append(self.variable())
                continue
            if self.current_char.isdigit():
                tokens.append(self.number())
                continue
            if self.current_char == '+':
                tokens.append(('PLUS', self.current_char))
                self.advance()
                continue
            if self.current_char == '-':
                tokens.append(('MINUS', self.current_char))
                self.advance()
                continue
            if self.current_char == '*':
                tokens.append(('MUL', self.current_char))
                self.advance()
                continue
            if self.current_char == '/':
                tokens.append(('DIV', self.current_char))
                self.advance()
                continue
            self.error()
        return tokens