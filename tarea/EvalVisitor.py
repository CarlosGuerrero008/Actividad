from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.vars = {}
        self.max_iterations = 1000  # Límite de seguridad

    def visitPrograma(self, ctx):
        return self.visitChildren(ctx)

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.vars[var_name] = value
        print(f"[Visitor] Asignado: {var_name} = {value}")
        return value

    def visitForLoop(self, ctx):
        # 1. Ejecutar inicialización
        init_var = ctx.inicializacion().ID().getText()
        init_value = self.visit(ctx.inicializacion().expresion())
        self.vars[init_var] = init_value
        
        # 2. Preparar condición
        cond_var = ctx.condicion().ID().getText()
        cond_op = ctx.condicion().op.text
        cond_val = int(ctx.condicion().INT().getText())
        
        # 3. Contador de seguridad
        iteration = 0
        
        while iteration < self.max_iterations:
            # Verificar condición
            current_val = self.vars.get(cond_var, 0)
            condition_met = False
            
            if cond_op == '<': condition_met = current_val < cond_val
            elif cond_op == '>': condition_met = current_val > cond_val
            elif cond_op == '==': condition_met = current_val == cond_val
            elif cond_op == '!=': condition_met = current_val != cond_val
            
            if not condition_met:
                break
            
            print(f"[Visitor] Iteración {iteration}: {cond_var} = {current_val}")
            
            # Ejecutar cuerpo del bucle
            for stmt in ctx.sentencia():
                self.visit(stmt)
            
            # Ejecutar actualización
            update_var = ctx.actualizacion().ID().getText()
            update_value = self.visit(ctx.actualizacion().expresion())
            self.vars[update_var] = update_value
            
            iteration += 1
        else:
            print("[Error] Límite de iteraciones alcanzado")

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if ctx.op.text == '+':
            return left + right
        return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if ctx.op.text == '*':
            return left * right
        return left / right

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.vars:
            print(f"[Warning] Variable {var_name} no inicializada, usando 0")
            self.vars[var_name] = 0
        return self.vars[var_name]