import tokenizer as tt
import parsercyk as cyk
from colorama import Fore, Style

print('Initiating...')

rules = [
        ('\n',                          'ENDLINE'),
        ('\'\'\'.*(\n.*)*\'\'\'',       'MULTILINECOMMENT'),
        ('\"\"\".*(\n.*)*\"\"\"',       'MULTILINECOMMENT'),
        ('\'.*\'',                      'STRING'),
        ('\".*\"',                      'STRING'),
        ('(\d+)?\.\d+',                 'FLOAT'),
        ('\d+',                         'INT'),
        ('from',                        'FROM'),
        ('import',                      'IMPORT'),
        ('as\s',                          'AS'),
        ('if',                          'IF'),
        ('else',                        'ELSE'),
        ('elif',                        'ELIF'),
        ('def',                         'DEF'),
        ('class',                       'CLASS'),
        ('return',                      'RETURN'),
        ('for\s',                         'FOR'),
        ('in',                          'IN'),
        ('range',                       'RANGE'),
        ('__\w+__',                     'MAGICMETHOD'),
        ('\->',                         'ARROW'),
        ('\.',                           'PERIOD'),
        ('(\+|\-|\*|\/)',               'OPERATOR'),
        ('is\s',                        'LOGICALOPERATOR'),
        ('or\s',                        'LOGICALOPERATOR'),
        ('and\s',                        'LOGICALOPERATOR'),
        ('not\s',                        'LOGICALOPERATOR'),
        ('\(',                          'LEFTP'),
        ('\)',                          'RIGHTP'),
        ('\[',                           'LEFTSB'),
        ('\]',                           'RIGHTSB'),
        ('\{',                          'LEFTCB'),
        ('\}',                          'RIGHTCB'),
        ('\>|\<',                       'COMPARATOR'),
        ('=',                           'EQUALS'),
        (':',                           'COLON'),
        (',',                           'COMMA'),      
        ('#',                           'CRASH'),
        ('\'\'\'',                      'TRIPLEQUOTE'),  
        ('\'',                          'QUOTE'),
        ('\"',                          'DOUBLEQUOTE'),
        ('True',                        'TRUE'),
        ('False',                       'FALSE'),
        ('None',                        'NONE'),
        ('break',                       'BREAK'),
        ('continue',                    'CONTINUE'),
        ('pass',                        'PASS'),
        ('raise',                       'RAISE'),
        ('with'                         ,'WITH'),
        ('[a-zA-Z_](\w+)*',             'IDENTIFIER'),
    ]

# inputtext = '''if((a > b) and ((b < c) or (c >=10))) :
#                                 a + b
#                             elif (a>b):
#                                 a + c
#                             else:
#                                 a + c'''
tokensarray = []

lx = tt.Lexer(rules)

filename = str(input('Masukan filename (dengan .txt) : '))

input = open(filename, 'r').read()
lx.input(input)

try:
    for tok in lx.tokens():
        tokensarray.append(tok.type)
        print(tok.type)
except tt.Error as err:
    print('Error at position %s' % err.position)

inputstring = ' '.join(tokensarray)
#print(inputstring)

CYK = cyk.Parser("grammar.txt", inputstring)
if input:
    CYK.parse()
    CYK.print_tree()
else:
    print('\n' + Fore.GREEN + 'Input Benar (Input kosong)')