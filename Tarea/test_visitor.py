from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

input_stream = InputStream(input('? '))
lexer = MiGramaticaLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = MiGramaticaParser(tokens)
tree = parser.programa()

visitor = EvalVisitor()
visitor.visit(tree)

print("\nVariables finales:", visitor.variables)