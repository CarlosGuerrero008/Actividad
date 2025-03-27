from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener

def main():
    """Prueba el listener mostrando la estructura del código"""
    # 1. Leer entrada del usuario
   
    input_stream = InputStream(input('? '))
    
    # 2. Procesamiento con ANTLR
    lexer = MiGramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(stream)
    tree = parser.programa()  # Obtener el árbol de parsing
    
    # 3. Recorrer el árbol con nuestro listener
    print("\n=== Resultados del Listener ===")
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()