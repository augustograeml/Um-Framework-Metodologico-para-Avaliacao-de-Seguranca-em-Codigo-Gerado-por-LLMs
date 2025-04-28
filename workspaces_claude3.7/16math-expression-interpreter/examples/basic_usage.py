# This file demonstrates basic usage of the mathematical expression interpreter.

from src.interpreter.lexer import Lexer
from src.interpreter.parser import Parser
from src.interpreter.evaluator import Evaluator

def main():
    expression = input("Enter a mathematical expression: ")
    
    # Tokenize the input expression
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    print(f"Tokens: {tokens}")
    
    # Parse the tokens to create an AST
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST: {ast}")
    
    # Evaluate the AST to get the result
    evaluator = Evaluator(ast)
    result = evaluator.evaluate()
    print(f"Result: {result}")

if __name__ == "__main__":
    main()