from colorama import Fore, Style
Rules_Dictinary = {}


def read_grammar(gfile):

    with open(gfile) as a:
        lines = a.readlines()
    return [x.replace("->", "").split() for x in lines]


def add_rule(rule):
    global Rules_Dictinary

    if (rule[0] not in Rules_Dictinary):
        Rules_Dictinary[rule[0]] = []
    Rules_Dictinary[rule[0]].append(rule[1:])


def convert_grammar(grammar):

    global Rules_Dictinary
    unit_productions, result = [], []
    res_append = result.append
    idx = 0

    for rule in grammar:
        new_rules = []
        if((len(rule) == 2) and (rule[1][0] != "'")):
            unit_productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(idx)}"
                    new_rules += [f"{rule[0]}{str(idx)}", item[0]]
                idx += 1
            while len(rule) > 3:
                new_rules += [f"{rule[0]}{str(idx)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(idx)}"] + rule[3:]
                idx += 1

        add_rule(rule)
        res_append(rule)
        if new_rules:
            res_append(new_rules)

    while(unit_productions):
        rule = unit_productions.pop()
        if rule[1] in Rules_Dictinary:
            for item in Rules_Dictinary[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    res_append(new_rule)
                else:
                    unit_productions.append(new_rule)
                add_rule(new_rule)
            # print(Rules_Dictinary)
    return result


def make_tree(node):
    # Primitif Pohon biner
    if (node.right == None):
        return f"[{node.symbol} '{node.left}']"
    else:
        return f"[{node.symbol} {make_tree(node.left)} {make_tree(node.right)}]"

class Node(object):
    # Daun pohon biner struktur data
    def __init__(self, symbol, left, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right
    
    def __str__ (self):
        return self.symbol

    def __repr__(self):
        return self.symbol


class Parser(object):

    def __init__(self, grammar, sentence):
        # Grammar langsung baca dari file
        self.parse_table = None
        self.prods = {}
        self.grammar = convert_grammar(read_grammar(grammar))
        self.__call__(sentence)

    def __call__(self, sentence):
        self.input = sentence.split()

    def parse(self):

        self.parse_table = [[[] for x in range(len(self.input) - y)] for y in range(len(self.input))]

        for i, word in enumerate(self.input):
            for rules in self.grammar:
                if f"'{word}'" == rules[1]:
                    self.parse_table[0][i].append(Node(rules[0], word))
        
        for ww in range(2, len(self.input) + 1):
            for start in range(0, len(self.input) - ww + 1):
                for left_size in range(1, ww):
                    right_size = ww - left_size

                    left_cell = self.parse_table[left_size - 1][start]
                    right_cell = self.parse_table[right_size - 1][start + left_size]

                    for rules in self.grammar:
                        left_nodes = [n for n in left_cell if n.symbol == rules[1]]
                        if left_nodes:
                            right_nodes = [n for n in right_cell if n.symbol == rules[2]]
                            self.parse_table[ww - 1][start].extend([Node(rules[0], left, right) for left in left_nodes for right in right_nodes])

    def print_tree(self):
        start_symbol = self.grammar[0][0]
        final_nodes = [a for a in self.parse_table[-1][0] if (a.symbol == start_symbol)]
        if final_nodes:
            print('\n' + Fore.GREEN + 'Input Benar')
            print(Style.RESET_ALL)
            print("Possible parse(s):")
            trees = [make_tree(node) for node in final_nodes]
            for tree in trees:
                print(tree)

        else:
            print('\n' + Fore.RED + 'Syntax Error')
            print(Style.RESET_ALL)

