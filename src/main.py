# Tubes TBFO2
# import tokenizer
import gistfile1
import cyk_parser as cyk
import grammar_converter

print('Initiating...')

rules = [
        ('\n',                          'ENDLINE'),
        ('\d+',                         'NUMBER'),
        ('from',                        'FROM'),
        ('import',                      'IMPORT'),
        ('as',                          'AS'),
        ('if',                          'IF'),
        ('else',                        'ELSE'),
        ('elif',                        'ELIF'),
        ('def',                         'DEF'),
        ('__\w+__',                     'MAGICMETHOD'),
        ('\->',                         'ARROW'),
        ('\.',                           'PERIOD'),
        ('(\+|\-|\*|\/)',               'OPERATOR'),
        ('is\s',                        'LOGICALOPERATOR'),
        ('or\s',                        'LOGICALOPERATOR'),
        ('and\s',                        'LOGICALOPERATOR'),
        ('not\s',                        'LOGICALOPERATOR'),
        ('[a-zA-Z_](\w+)*',             'IDENTIFIER'),
        ('\(',                          'LEFTP'),
        ('\)',                          'RIGHTP'),
        ('\[',                           'LEFTSB'),
        ('\]',                           'RIGHTSB'),
        ('\>|\<',                       'COMPARATOR'),
        ('=',                           'EQUALS'),
        (':',                           'COLON'),
        (',',                           'COMMA'),        
        ('\'',                          'QUOTE'),
        ('\"',                          'DOUBLEQUOTE'),
        ('return',                      'RETURN'),
        ('True',                        'TRUE'),
        ('False',                       'FALSE'),
        ('None',                        'NONE'),
        ('break',                       'BREAK'),
        ('continue',                    'CONTINUE'),
        ('pass',                        'PASS'),
    ]

# inputtext = '''if((a > b) and ((b < c) or (c >=10))) :
#                                 a + b
#                             elif (a>b):
#                                 a + c
#                             else:
#                                 a + c'''
tokensarray = []

lx = gistfile1.Lexer(rules)

filename = str(input('Masukan filename (dengan .txt) : '))

input = open(filename, 'r').read()
lx.input(input)

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




print(input[6])