# Generated from MiGramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiGramaticaParser import MiGramaticaParser
else:
    from MiGramaticaParser import MiGramaticaParser

# This class defines a complete generic visitor for a parse tree produced by MiGramaticaParser.

class MiGramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiGramaticaParser#programa.
    def visitPrograma(self, ctx:MiGramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#sentencia.
    def visitSentencia(self, ctx:MiGramaticaParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ForLoopRule.
    def visitForLoopRule(self, ctx:MiGramaticaParser.ForLoopRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#DeclaracionRule.
    def visitDeclaracionRule(self, ctx:MiGramaticaParser.DeclaracionRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#tipo.
    def visitTipo(self, ctx:MiGramaticaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#bloque.
    def visitBloque(self, ctx:MiGramaticaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#IfElseRule.
    def visitIfElseRule(self, ctx:MiGramaticaParser.IfElseRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#CondicionRule.
    def visitCondicionRule(self, ctx:MiGramaticaParser.CondicionRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#SoloExpresion.
    def visitSoloExpresion(self, ctx:MiGramaticaParser.SoloExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#AssignRule.
    def visitAssignRule(self, ctx:MiGramaticaParser.AssignRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#IncrementoRule.
    def visitIncrementoRule(self, ctx:MiGramaticaParser.IncrementoRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#DecrementoRule.
    def visitDecrementoRule(self, ctx:MiGramaticaParser.DecrementoRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#AsignacionIncrRule.
    def visitAsignacionIncrRule(self, ctx:MiGramaticaParser.AsignacionIncrRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#AddSubRule.
    def visitAddSubRule(self, ctx:MiGramaticaParser.AddSubRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#ParensRule.
    def visitParensRule(self, ctx:MiGramaticaParser.ParensRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#VariableRule.
    def visitVariableRule(self, ctx:MiGramaticaParser.VariableRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#IntRule.
    def visitIntRule(self, ctx:MiGramaticaParser.IntRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiGramaticaParser#MulDivRule.
    def visitMulDivRule(self, ctx:MiGramaticaParser.MulDivRuleContext):
        return self.visitChildren(ctx)



del MiGramaticaParser