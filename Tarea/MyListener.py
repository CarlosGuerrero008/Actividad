from MiGramaticaParser import MiGramaticaParser
from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def __init__(self):
        self.indent = 0
    
    def print_indented(self, text):
        print("  " * self.indent + text)
    
    def enterPrograma(self, ctx):
        self.print_indented("Inicio del programa")
        self.indent += 1

    def exitPrograma(self, ctx):
        self.indent -= 1
        self.print_indented("Fin del programa")

    def enterAssignRule(self, ctx):
        self.print_indented(f"Asignación: {ctx.ID().getText()} = {ctx.expr().getText()}")

    def enterForLoopRule(self, ctx):
        self.print_indented("[CICLO FOR]")
        self.indent += 1
        self.print_indented(f"Inicialización: {ctx.getChild(2).getText()}")
        self.print_indented(f"Condición: {ctx.condicion().getText()}")
        self.print_indented(f"Actualización: {ctx.expresionIncremento().getText()}")
        self.print_indented("Cuerpo:")

    def exitForLoopRule(self, ctx):
        self.indent -= 1

    def enterCondicionRule(self, ctx):
        self.print_indented(f"Comparación: {ctx.expr(0).getText()} {ctx.op.text} {ctx.expr(1).getText()}")

    def enterIncrementoRule(self, ctx):
        self.print_indented(f"Incremento: {ctx.ID().getText()}++")

    def enterBloque(self, ctx):
        self.print_indented("{")
        self.indent += 1

    def exitBloque(self, ctx):
        self.indent -= 1
        self.print_indented("}")

    def enterIfElseRule(self, ctx):
        self.print_indented("[CONDICIONAL IF]")
        self.indent += 1
        self.print_indented(f"Condición: {ctx.condicion().getText()}")

    def exitIfElseRule(self, ctx):
        self.indent -= 1