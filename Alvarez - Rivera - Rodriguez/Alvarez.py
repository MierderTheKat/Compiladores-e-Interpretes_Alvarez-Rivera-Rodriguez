import ply.lex as lex

tokens = (
    'COMPARACION',
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'PUNTOS',
    'MENORIGUAL',
    'MAYORIGUAL'
)

reserved = {
'for' : 'FOR'
}

tokens = list(tokens) + list(reserved.values())

t_MAYORQ = r'>'
t_MENORQ = r'<'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUAL = r'='
t_COMPARACION = r'=='
t_PUNTOS = r':'

def t_error(t):
    print("Token desconocido:'%s'" % t.value)
    t.lexer.skip(1)

def t_VAR(t):
    r'\w+'
    t.type = reserved.get(t.value, 'VAR')
    return t

t_ignore = ' \t\n'

lexer = lex.lex()
data = open("_dataAlvarez.txt")
data = data.read()
lexer.input(data)

while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)
