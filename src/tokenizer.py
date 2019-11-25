import re
import sys

#Kalo belom familiar, __init__ buat inisiasi object (mirip struct di C), __str__ itu jika object di print

class Token(object):

    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position #Buat ntar kalo code error

    def __str__(self): #Jika object di print
        return '%s(%s) at %s' %(self.type, self.value, self.position)

class Error(Exception):

    def __init__(self, pos, errType=0):
        self.pos = pos
        self.errType = errType

class Parser(object):

    def __init__(self, rules, skip_space=True):

        i = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % i
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            i += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_space = skip_space
        self.re_s_skip = re.compile(r'\S')

    def input(self, buffer, position=0):
        self.buffer = buffer
        self.position = position

    def token(self):
        if self.position >= len(self.buffer):
            return None
        else:
            if self.skip_space:
                m = self.re_s_skip.search(self.buffer, self.position)

                if m:
                    self.position = m.start()
                else:
                    return None

            m = self.regex.match(self.buffer, self.position)

            if m:
                groupname = m.lastgroup
                token_type = self.group_type[groupname]
                token = Token(token_type, m.group(groupname), self.position)
                self.pos = m.end()
                return token

            raise Error(self.position)

    def tokens(self):
        stop = False
        while(not(stop)):
            tokenn = self.token()
            if tokenn is None:
                stop = True
            yield tokenn


