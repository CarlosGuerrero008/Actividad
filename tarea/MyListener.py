from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    """
    Listener que detecta estructuras del código y muestra información
    cuando sale de cada regla del parser.
    """
    
    def exitForLoop(self, ctx):
        """Se ejecuta al salir de un bucle for"""
        print(f"[Listener] Bucle for encontrado:")
        print(f"  Inicialización: {ctx.inicializacion().getText()}")
        print(f"  Condición: {ctx.condicion().getText()}")
        print(f"  Actualización: {ctx.actualizacion().getText()}")

    def exitInicializacion(self, ctx):
        """Detecta inicializaciones de variables (ej: i = 0)"""
        print(f"[Listener] Inicialización: {ctx.ID().getText()} = {ctx.expresion().getText()}")

    def exitCondicion(self, ctx):
        """Detecta condiciones (ej: i < 10)"""
        print(f"[Listener] Condición: {ctx.ID().getText()} {ctx.op.text} {ctx.INT().getText()}")

    def exitActualizacion(self, ctx):
        """Detecta actualizaciones (ej: i = i + 1)"""
        print(f"[Listener] Actualización: {ctx.ID().getText()} = {ctx.expresion().getText()}")

    def exitAssign(self, ctx):
        """Detecta asignaciones de variables (ej: x = 5)"""
        print(f"[Listener] Asignación: {ctx.ID().getText()} = {ctx.expresion().getText()}")