from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

def main():
    """Prueba el visitor ejecutando el código"""
    # 1. Leer entrada del usuario
    input_stream = InputStream(input('? '))
    
    # 2. Procesamiento con ANTLR
    lexer = MiGramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(stream)
    tree = parser.programa()  # Obtener el árbol de parsing
    
    # 3. Recorrer el árbol con nuestro visitor
    print("\n=== Ejecución con Visitor ===")
    visitor = EvalVisitor()
    visitor.visit(tree)
    
    # Mostrar estado final de variables
    print("\nVariables finales:", visitor.vars)

if __name__ == '__main__':
    main()