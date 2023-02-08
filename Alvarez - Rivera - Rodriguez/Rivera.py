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
    'VAR',
)

reserved = {
'if' : 'IF',
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

def t_VAR(t):
    r'\w+'
    t.type = reserved.get(t.value, 'VAR')
    return t

def t_error(t):
    print("Token desconocido:'%s'" % t.value)
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex()
data = open("_dataRivera.txt")
data = data.read()
lexer.input(data)

while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)
