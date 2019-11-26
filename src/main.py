# Tubes TBFO2
# import tokenizer
import gistfile1
import cyk_parser as cyk
import grammar_converter

print('Initiating...')

rules = [
        ('\d+',                         'NUMBER'),
        ('from',                        'FROM'),
        ('import',                      'IMPORT'),
        ('as',                          'AS'),
        ('if',                          'IF'),
        ('else',                        'ELSE'),
        ('elif',                        'ELIF'),
        ('__\w+__',                     'STATEMENT'),
        ('\+|\-|\*|\/|and|or|not|is',   'OPERATOR'),
        ('[a-zA-Z_](\w+)*',             'IDENTIFIER'),
        ('\(',                          'LEFTP'),
        ('\)',                          'RIGHTP'),
        ('\>|\<',                       'COMPARATOR'),
        ('=',                           'EQUALS'),
        (':',                           'COLON'),
        ('\'',                          'QUOTE'),
        ('\"',                          'DOUBLEQUOTE'),
        ('True',                        'TRUE'),
        ('False',                       'FALSE'),
        ('None',                        'NONE'),
        ('break',                       'BREAK'),
        ('continue',                    'CONTINUE'),
        ('pass',                        'PASS'),
        ('\w+',                         'ALPHANUM')
    ]

# inputtext = '''if((a > b) and ((b < c) or (c >=10))) :
#                                 a + b
#                             elif (a>b):
#                                 a + c
#                             else:
#                                 a + c'''
tokensarray = []

lx = gistfile1.Lexer(rules)


try:
    for tok in lx.tokens():
        tokensarray.append(tok.type)
        print(tok.type)
except gistfile1.LexerError as err:
    print('LexerError at position %s' % err.pos)

inputstring = ' '.join(tokensarray)
print(inputstring)

CYK = cyk.Parser("grammar.txt", inputstring)
CYK.parse()
CYK.print_tree()


filename = str(input('Masukan filename (dengan .txt) : '))

input = open(filename, 'r').read()
lx.input(input)

print(input[6])