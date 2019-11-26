import re
import sys
import cyk_parser as cyk
import os.path
import argparse
import grammar_converter

class Token(object):
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.value, self.position)

    def __repr__(self):
        return '%s(%s) at %s' % (self.type, self.value, self.position)


class Error(Exception):
    def __init__(self, position):
        self.position = position


class Lexer(object):
    def __init__(self, rules, skip_ws=True):
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_ws = skip_ws
        self.re_ws_skip = re.compile('[^ \t\r\f\v]')

    def input(self, buffer):

        self.buffer = buffer
        self.position = 0

    def token(self):
        if self.position >= len(self.buffer):
            return None
        else:
            if self.skip_ws:
                match = self.re_ws_skip.search(self.buffer, self.position)

                if match:
                    self.position = match.start()
                else:
                    return None

            match = self.regex.match(self.buffer, self.position)
            if match:
                groupname = match.lastgroup
                tokenn_type = self.group_type[groupname]
                tokenn = Token(tokenn_type, match.group(groupname), self.position)
                self.position = match.end()
                return tokenn

            # if we're here, no rule matched
            raise LexerError(self.position)

    def tokens(self):
        while True:
            tokenn = self.token()
            if tokenn is None: 
                break
            yield tokenn