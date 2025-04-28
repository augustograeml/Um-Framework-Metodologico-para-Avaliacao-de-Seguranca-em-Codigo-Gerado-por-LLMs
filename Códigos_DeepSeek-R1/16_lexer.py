class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.text else None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.position += 1
        if self.position > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.position]

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
                tokens.append(('PLUS', '+'))
                self.advance()
                continue
            if self.current_char == '-':
                tokens.append(('MINUS', '-'))
                self.advance()
                continue
            if self.current_char == '*':
                tokens.append(('MUL', '*'))
                self.advance()
                continue
            if self.current_char == '/':
                tokens.append(('DIV', '/'))
                self.advance()
                continue
            self.error()
        return tokens