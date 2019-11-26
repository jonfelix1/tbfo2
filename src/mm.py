import tokenizer as tt
import parsercyk as cyk

print('Initiating...')

rules = [
        ('\n',                          'ENDLINE'),
        ('\'\'\'.*(\n.*)*\'\'\'',       'MULTILINECOMMENT'),
        ('\"\"\".*(\n.*)*\"\"\"',       'MULTILINECOMMENT'),
        ('\'.*\'',                      'STRING'),
        ('\".*\"',                      'STRING'),
        ('\d+',                         'NUMBER'),
        ('from',                        'FROM'),
        ('import',                      'IMPORT'),
        ('as',                          'AS'),
        ('if',                          'IF'),
        ('else',                        'ELSE'),
        ('elif',                        'ELIF'),
        ('def',                         'DEF'),
        ('return',                      'RETURN'),
        ('for',                         'FOR'),
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
    print('Error at position %s' % err.pos)

inputstring = ' '.join(tokensarray)
#print(inputstring)

CYK = cyk.Parser("grammar.txt", inputstring)
CYK.parse()
CYK.print_tree()