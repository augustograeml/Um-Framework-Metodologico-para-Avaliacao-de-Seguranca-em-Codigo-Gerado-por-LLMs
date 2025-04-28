def main():
    from interpreter.lexer import Lexer
    from interpreter.parser import Parser
    from interpreter.evaluator import Evaluator

    while True:
        try:
            expression = input("Enter a mathematical expression (or 'exit' to quit): ")
            if expression.lower() == 'exit':
                break

            lexer = Lexer(expression)
            tokens = lexer.tokenize()

            parser = Parser(tokens)
            ast = parser.parse()

            evaluator = Evaluator(ast)
            result = evaluator.evaluate()

            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()