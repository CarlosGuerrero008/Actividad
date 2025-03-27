from MiGramaticaParser import MiGramaticaParser
from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}
        # Definimos constantes para los operadores
        self.GT = 1
        self.LT = 2
        self.EQ = 3
        self.NEQ = 4
        self.GTE = 5
        self.LTE = 6
        self.ADD = 7
        self.SUB = 8
        self.MUL = 9
        self.DIV = 10

    # Programa
    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)

    # Asignación
    def visitAssignRule(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        print(f"Asignación: {var_name} = {value}")
        return value

    # For loop
    def visitForLoopRule(self, ctx):
        print("[CICLO FOR]")
        # Inicialización
        if ctx.getChild(2):  # init
            self.visit(ctx.getChild(2))
        
        # Bucle
        while True:
            # Condición
            if ctx.condicion():
                cond = self.visit(ctx.condicion())
                if not cond:
                    break
            
            # Cuerpo
            self.visit(ctx.cuerpo)
            
            # Actualización
            if ctx.expresionIncremento():
                self.visit(ctx.expresionIncremento())

    # Operaciones matemáticas
    def visitMulDivRule(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        else:
            return left / right

    def visitAddSubRule(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        else:
            return left - right

    # Valores
    def visitIntRule(self, ctx):
        return int(ctx.INT().getText())

    def visitVariableRule(self, ctx):
        var_name = ctx.ID().getText()
        return self.variables.get(var_name, 0)

    # Condiciones
    def visitCondicionRule(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        
        print(f"Comparando: {left} {op} {right}")
        
        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right

    # Incrementos
    def visitIncrementoRule(self, ctx):
        var_name = ctx.ID().getText()
        self.variables[var_name] = self.variables.get(var_name, 0) + 1
        print(f"Incremento: {var_name} = {self.variables[var_name]}")
        return self.variables[var_name]

    def visitDecrementoRule(self, ctx):
        var_name = ctx.ID().getText()
        self.variables[var_name] = self.variables.get(var_name, 0) - 1
        print(f"Decremento: {var_name} = {self.variables[var_name]}")
        return self.variables[var_name]

    # Bloques
    def visitBloque(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)