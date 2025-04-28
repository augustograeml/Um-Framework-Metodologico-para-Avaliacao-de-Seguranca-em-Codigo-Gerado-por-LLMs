class Parser:
    def parse(self, expression: str) -> list:
        tokens = []
        current_number = ''
        
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ''
                if char in '+-*/()':
                    tokens.append(char)
        
        if current_number:
            tokens.append(float(current_number))
        
        return tokens