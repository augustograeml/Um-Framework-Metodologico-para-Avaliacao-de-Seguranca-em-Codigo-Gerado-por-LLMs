def main():
    from math_interpreter.lexer import Lexer
    from math_interpreter.parser import Parser
    from math_interpreter.evaluator import Evaluator

    while True:
        try:
            user_input = input("Enter a mathematical expression (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            lexer = Lexer(user_input)
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