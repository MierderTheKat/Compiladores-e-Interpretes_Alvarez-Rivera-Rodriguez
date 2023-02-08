import ply.lex as lex

tokens = (
    'COMPARACION',
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'PUNTOS',
    'MENORIGUAL',
    'MAYORIGUAL',
    'PABRE',
    'PCIERRA',
    'CABRE',
    'CCIERRA',
    'VAR',
    'PUNTOYCOMA',
    'SUMATORIA',
    'SUMA',
    'COMILLA',
    'PUNTO',
)

reserved = {
'Mon' : 'FOR',
'juan' : 'INT',
'DNRT' : 'IF',
'tilled' : 'BREAK',
'println' : 'SYSTEM',
}

tokens = list(reserved.values()) +  list(tokens)

t_MAYORQ = r'>'
t_MENORQ = r'<'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUAL = r'='
t_COMPARACION = r'=='
t_PUNTOS = r':'
t_PABRE = r'\('
t_PCIERRA = r'\)'
t_CABRE = r'{'
t_CCIERRA = r'}'
t_PUNTOYCOMA = r';'
t_SUMATORIA = r'\+\+'
t_SUMA = r'\+'
t_COMILLA = r'\"'
t_PUNTO = r'\.'

def t_VAR(t):
    r'\w+'
    t.type = reserved.get(t.value, 'VAR')
    return t

def t_error(t):
    print("Token desconocido:'%s'" % t.value)
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex()
data = open("_dataRodriguez.txt")
data = data.read()
lexer.input(data)

while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)
