import check50

import ast
from collections import defaultdict
import argparse

@check50.check()
def exists():
    """timmy.py exists."""
    check50.exists("timmy.py")

@check50.check(exists)
def test_mural_exists():
    """test if mural.png file is produced"""
    check50.run("python3 timmy.py").exit(0)
    check50.exists("mural.png")

@check50.check(exists)
def testif():
    """check for at least one if statement"""
    with open("timmy.py") as source:
       tree = ast.parse(source.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
      if not analyzer.has_for():
        raise check50.Failure("no for loop found")

@check50.check(exists)
def test1():
    """handles a height of 1 correctly"""
    out = check50.run("python3 mario.py").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(exists)
def test2():
    """handles a height of 2 correctly"""
    out = check50.run("python3 mario.py").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(exists)
def test23():
    """handles a height of 8 correctly"""
    out = check50.run("python3 mario.py").stdin("8").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(exists)
def test24():
    """rejects a height of 9, and then accepts a height of 2"""
    (check50.run("python3 mario.py").stdin("9").reject()
            .stdin("2").stdout(open("2.txt")).exit(0))

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    check50.run("python3 mario.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("python3 mario.py").stdin("").reject()

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = defaultdict(list)

    def visit_list_helper(self, node, key: str):
        '''Process nodes where the value is a list of Nodes.'''
        for alias in node.names:
            self.stats[key].append(alias.name)
        self.generic_visit(node)
    
    def visit_helper(self, node, key: str):
        '''Process nodes where the value is a single Node like If, For, While.'''
        self.stats[key].append(key)
        self.generic_visit(node)

    def visit_Import(self, node):
        self.visit_list_helper(node, "import")

    def visit_ImportFrom(self, node):
        self.visit_list_helper(node, "from")
    
    def visit_If(self, node):
        self.visit_helper(node, 'if')

    def visit_While(self, node):
        self.visit_helper(node, 'while')

    def visit_For(self, node):
        self.visit_helper(node, 'for')

    def visit_FunctionDef(self, node):
        self.stats['def'].append(node.name)
        self.generic_visit(node)
    
    def visit_Call(self, node):
      match type(node.func):
         case ast.Name:
               self.stats['call'].append(node.func.id)
         case ast.Attribute:
               if isinstance(node.func.value, ast.Name):
                  self.stats['call'].append(f'{node.func.value.id}.{node.func.attr}')
               else:
                  self.stats['call'].append(node.func.attr)
         case _:
               self.stats['call'].append(node)
      self.generic_visit(node)
       def has_for(self):
        return len(self.stats['for']) > 0
    
    def has_while(self):
        return len(self.stats['while']) > 0
    
    def has_if(self):
        return len(self.stats['if']) > 0
    
    def has_func(self):
        return len(self.stats['def']) >= 3
    
    def has_call(self):
        return len(self.stats['call']) >= 3
    
    def check_expect(self, target:str):
        match target:
            case 'for':
                if self.has_for():
                    return "for loop found"
            case 'while':
                if self.has_while():
                    return "while loop found"
            case 'if':
                if self.has_if():
                    return "if statement found"
            case 'def':
                if self.has_func():
                    return "at least 3 functions found"
            case 'call':
                if self.has_call():
                    return "at least 3 function calls to your different functions found"
            case _:
                return "check for {target} invalid."
def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "Did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "Are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)
