# Generated from MiGramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,3,0,25,8,0,4,0,27,8,
        0,11,0,12,0,28,1,0,1,0,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,
        2,3,2,43,8,2,1,2,1,2,3,2,47,8,2,1,2,1,2,3,2,51,8,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,3,5,66,8,5,5,5,68,8,5,10,5,
        12,5,71,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,82,8,6,1,7,1,
        7,1,7,1,7,1,7,3,7,89,8,7,1,8,1,8,1,8,1,8,3,8,95,8,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,104,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,
        10,113,8,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,121,8,10,10,10,12,
        10,124,9,10,1,10,0,1,20,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,0,6,
        8,1,0,13,18,1,0,21,22,1,0,23,24,134,0,26,1,0,0,0,2,36,1,0,0,0,4,
        38,1,0,0,0,6,55,1,0,0,0,8,60,1,0,0,0,10,62,1,0,0,0,12,74,1,0,0,0,
        14,88,1,0,0,0,16,90,1,0,0,0,18,103,1,0,0,0,20,112,1,0,0,0,22,24,
        3,2,1,0,23,25,5,1,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,
        26,22,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,30,1,
        0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,37,3,12,6,0,33,37,3,16,8,0,34,
        37,3,4,2,0,35,37,3,10,5,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,
        0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,5,2,0,0,39,42,5,3,0,0,40,43,
        3,16,8,0,41,43,3,6,3,0,42,40,1,0,0,0,42,41,1,0,0,0,42,43,1,0,0,0,
        43,44,1,0,0,0,44,46,5,1,0,0,45,47,3,14,7,0,46,45,1,0,0,0,46,47,1,
        0,0,0,47,48,1,0,0,0,48,50,5,1,0,0,49,51,3,18,9,0,50,49,1,0,0,0,50,
        51,1,0,0,0,51,52,1,0,0,0,52,53,5,4,0,0,53,54,3,2,1,0,54,5,1,0,0,
        0,55,56,3,8,4,0,56,57,5,25,0,0,57,58,5,5,0,0,58,59,3,20,10,0,59,
        7,1,0,0,0,60,61,7,0,0,0,61,9,1,0,0,0,62,69,5,9,0,0,63,65,3,2,1,0,
        64,66,5,1,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,63,1,
        0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,
        69,1,0,0,0,72,73,5,10,0,0,73,11,1,0,0,0,74,75,5,11,0,0,75,76,5,3,
        0,0,76,77,3,14,7,0,77,78,5,4,0,0,78,81,3,2,1,0,79,80,5,12,0,0,80,
        82,3,2,1,0,81,79,1,0,0,0,81,82,1,0,0,0,82,13,1,0,0,0,83,84,3,20,
        10,0,84,85,7,1,0,0,85,86,3,20,10,0,86,89,1,0,0,0,87,89,3,20,10,0,
        88,83,1,0,0,0,88,87,1,0,0,0,89,15,1,0,0,0,90,91,5,25,0,0,91,92,5,
        5,0,0,92,94,3,20,10,0,93,95,5,1,0,0,94,93,1,0,0,0,94,95,1,0,0,0,
        95,17,1,0,0,0,96,97,5,25,0,0,97,104,5,19,0,0,98,99,5,25,0,0,99,104,
        5,20,0,0,100,101,5,25,0,0,101,102,5,5,0,0,102,104,3,20,10,0,103,
        96,1,0,0,0,103,98,1,0,0,0,103,100,1,0,0,0,104,19,1,0,0,0,105,106,
        6,10,-1,0,106,113,5,26,0,0,107,113,5,25,0,0,108,109,5,3,0,0,109,
        110,3,20,10,0,110,111,5,4,0,0,111,113,1,0,0,0,112,105,1,0,0,0,112,
        107,1,0,0,0,112,108,1,0,0,0,113,122,1,0,0,0,114,115,10,5,0,0,115,
        116,7,2,0,0,116,121,3,20,10,6,117,118,10,4,0,0,118,119,7,3,0,0,119,
        121,3,20,10,5,120,114,1,0,0,0,120,117,1,0,0,0,121,124,1,0,0,0,122,
        120,1,0,0,0,122,123,1,0,0,0,123,21,1,0,0,0,124,122,1,0,0,0,15,24,
        28,36,42,46,50,65,69,81,88,94,103,112,120,122
    ]

class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'for'", "'('", "')'", "'='", "'int'", 
                     "'float'", "'var'", "'{'", "'}'", "'if'", "'else'", 
                     "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", "'++'", 
                     "'--'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_forStmt = 2
    RULE_declaracion = 3
    RULE_tipo = 4
    RULE_bloque = 5
    RULE_ifElseStmt = 6
    RULE_condicion = 7
    RULE_asignacion = 8
    RULE_expresionIncremento = 9
    RULE_expr = 10

    ruleNames =  [ "programa", "sentencia", "forStmt", "declaracion", "tipo", 
                   "bloque", "ifElseStmt", "condicion", "asignacion", "expresionIncremento", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    ID=25
    INT=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiGramaticaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiGramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.sentencia()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 23
                    self.match(MiGramaticaParser.T__0)


                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33556996) != 0)):
                    break

            self.state = 30
            self.match(MiGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElseStmt(self):
            return self.getTypedRuleContext(MiGramaticaParser.IfElseStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiGramaticaParser.ForStmtContext,0)


        def bloque(self):
            return self.getTypedRuleContext(MiGramaticaParser.BloqueContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MiGramaticaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.ifElseStmt()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.asignacion()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.forStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.bloque()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForLoopRuleContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ForStmtContext
            super().__init__(parser)
            self.cuerpo = None # SentenciaContext
            self.copyFrom(ctx)

        def sentencia(self):
            return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,0)

        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)

        def declaracion(self):
            return self.getTypedRuleContext(MiGramaticaParser.DeclaracionContext,0)

        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)

        def expresionIncremento(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionIncrementoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoopRule" ):
                listener.enterForLoopRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoopRule" ):
                listener.exitForLoopRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoopRule" ):
                return visitor.visitForLoopRule(self)
            else:
                return visitor.visitChildren(self)



    def forStmt(self):

        localctx = MiGramaticaParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            localctx = MiGramaticaParser.ForLoopRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MiGramaticaParser.T__1)
            self.state = 39
            self.match(MiGramaticaParser.T__2)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 40
                self.asignacion()
                pass
            elif token in [6, 7, 8]:
                self.state = 41
                self.declaracion()
                pass
            elif token in [1]:
                pass
            else:
                pass
            self.state = 44
            self.match(MiGramaticaParser.T__0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 100663304) != 0):
                self.state = 45
                self.condicion()


            self.state = 48
            self.match(MiGramaticaParser.T__0)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 49
                self.expresionIncremento()


            self.state = 52
            self.match(MiGramaticaParser.T__3)
            self.state = 53
            localctx.cuerpo = self.sentencia()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_declaracion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionRuleContext(DeclaracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.DeclaracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipo(self):
            return self.getTypedRuleContext(MiGramaticaParser.TipoContext,0)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionRule" ):
                listener.enterDeclaracionRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionRule" ):
                listener.exitDeclaracionRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionRule" ):
                return visitor.visitDeclaracionRule(self)
            else:
                return visitor.visitChildren(self)



    def declaracion(self):

        localctx = MiGramaticaParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        try:
            localctx = MiGramaticaParser.DeclaracionRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.tipo()
            self.state = 56
            self.match(MiGramaticaParser.ID)
            self.state = 57
            self.match(MiGramaticaParser.T__4)
            self.state = 58
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = MiGramaticaParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = MiGramaticaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MiGramaticaParser.T__8)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33556996) != 0):
                self.state = 63
                self.sentencia()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 64
                    self.match(MiGramaticaParser.T__0)


                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(MiGramaticaParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_ifElseStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseRuleContext(IfElseStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.IfElseStmtContext
            super().__init__(parser)
            self.thenPart = None # SentenciaContext
            self.elsePart = None # SentenciaContext
            self.copyFrom(ctx)

        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseRule" ):
                listener.enterIfElseRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseRule" ):
                listener.exitIfElseRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseRule" ):
                return visitor.visitIfElseRule(self)
            else:
                return visitor.visitChildren(self)



    def ifElseStmt(self):

        localctx = MiGramaticaParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifElseStmt)
        try:
            localctx = MiGramaticaParser.IfElseRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(MiGramaticaParser.T__10)
            self.state = 75
            self.match(MiGramaticaParser.T__2)
            self.state = 76
            self.condicion()
            self.state = 77
            self.match(MiGramaticaParser.T__3)
            self.state = 78
            localctx.thenPart = self.sentencia()
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(MiGramaticaParser.T__11)
                self.state = 80
                localctx.elsePart = self.sentencia()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionRuleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionRule" ):
                listener.enterCondicionRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionRule" ):
                listener.exitCondicionRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicionRule" ):
                return visitor.visitCondicionRule(self)
            else:
                return visitor.visitChildren(self)


    class SoloExpresionContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoloExpresion" ):
                listener.enterSoloExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoloExpresion" ):
                listener.exitSoloExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoloExpresion" ):
                return visitor.visitSoloExpresion(self)
            else:
                return visitor.visitChildren(self)



    def condicion(self):

        localctx = MiGramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = MiGramaticaParser.CondicionRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.expr(0)
                self.state = 84
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 85
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = MiGramaticaParser.SoloExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignRuleContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignRule" ):
                listener.enterAssignRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignRule" ):
                listener.exitAssignRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignRule" ):
                return visitor.visitAssignRule(self)
            else:
                return visitor.visitChildren(self)



    def asignacion(self):

        localctx = MiGramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_asignacion)
        try:
            localctx = MiGramaticaParser.AssignRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MiGramaticaParser.ID)
            self.state = 91
            self.match(MiGramaticaParser.T__4)
            self.state = 92
            self.expr(0)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(MiGramaticaParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionIncrementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expresionIncremento

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IncrementoRuleContext(ExpresionIncrementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionIncrementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrementoRule" ):
                listener.enterIncrementoRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrementoRule" ):
                listener.exitIncrementoRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrementoRule" ):
                return visitor.visitIncrementoRule(self)
            else:
                return visitor.visitChildren(self)


    class DecrementoRuleContext(ExpresionIncrementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionIncrementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecrementoRule" ):
                listener.enterDecrementoRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecrementoRule" ):
                listener.exitDecrementoRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecrementoRule" ):
                return visitor.visitDecrementoRule(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionIncrRuleContext(ExpresionIncrementoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionIncrementoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionIncrRule" ):
                listener.enterAsignacionIncrRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionIncrRule" ):
                listener.exitAsignacionIncrRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionIncrRule" ):
                return visitor.visitAsignacionIncrRule(self)
            else:
                return visitor.visitChildren(self)



    def expresionIncremento(self):

        localctx = MiGramaticaParser.ExpresionIncrementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expresionIncremento)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = MiGramaticaParser.IncrementoRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(MiGramaticaParser.ID)
                self.state = 97
                self.match(MiGramaticaParser.T__18)
                pass

            elif la_ == 2:
                localctx = MiGramaticaParser.DecrementoRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(MiGramaticaParser.ID)
                self.state = 99
                self.match(MiGramaticaParser.T__19)
                pass

            elif la_ == 3:
                localctx = MiGramaticaParser.AsignacionIncrRuleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(MiGramaticaParser.ID)
                self.state = 101
                self.match(MiGramaticaParser.T__4)
                self.state = 102
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubRuleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubRule" ):
                listener.enterAddSubRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubRule" ):
                listener.exitAddSubRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubRule" ):
                return visitor.visitAddSubRule(self)
            else:
                return visitor.visitChildren(self)


    class ParensRuleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensRule" ):
                listener.enterParensRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensRule" ):
                listener.exitParensRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensRule" ):
                return visitor.visitParensRule(self)
            else:
                return visitor.visitChildren(self)


    class VariableRuleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableRule" ):
                listener.enterVariableRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableRule" ):
                listener.exitVariableRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableRule" ):
                return visitor.visitVariableRule(self)
            else:
                return visitor.visitChildren(self)


    class IntRuleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntRule" ):
                listener.enterIntRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntRule" ):
                listener.exitIntRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntRule" ):
                return visitor.visitIntRule(self)
            else:
                return visitor.visitChildren(self)


    class MulDivRuleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivRule" ):
                listener.enterMulDivRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivRule" ):
                listener.exitMulDivRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivRule" ):
                return visitor.visitMulDivRule(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = MiGramaticaParser.IntRuleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 106
                self.match(MiGramaticaParser.INT)
                pass
            elif token in [25]:
                localctx = MiGramaticaParser.VariableRuleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(MiGramaticaParser.ID)
                pass
            elif token in [3]:
                localctx = MiGramaticaParser.ParensRuleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(MiGramaticaParser.T__2)
                self.state = 109
                self.expr(0)
                self.state = 110
                self.match(MiGramaticaParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MiGramaticaParser.MulDivRuleContext(self, MiGramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 114
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 115
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiGramaticaParser.AddSubRuleContext(self, MiGramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 117
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 118
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 119
                        self.expr(5)
                        pass

             
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




