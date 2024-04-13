import check50

import ast
from collections import defaultdict

@check50.check()
def exists():
    """doodle.py exists."""
    check50.exists("doodle.py")
    check50.exists("art.png")

@check50.check(exists)
def test_art_exists():
    """art.png file is produced"""
    check50.run("python3 doodle.py 1 art.png").exit(0)
    check50.exists("art.png")

@check50.check(exists)
def test_reject_not_number():
    """reject 1st parameter number not {1,2,3}"""
    status = check50.run("python3 doodle.py 4 art.png").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject number outside set {1,2,3}")

@check50.check(exists)
def test_reject_non_numeric():
    """reject 1st parameter is not a number"""
    status = check50.run("python3 doodle.py abcd art.png").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non numeric 1st parameter")

@check50.check(exists)
def test_reject_empty():
    """reject no command line parameters"""
    status = check50.run("python3 doodle.py").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject no parameters given")
        
@check50.check(exists)
def testif():
    """check for at least one if statement"""
    with open("doodle.py") as source:
        tree = ast.parse(source.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
        if not analyzer.has_if():
            raise check50.Failure("no if statement found")
            
@check50.check(exists)
def testfor():
    """check for at least one for loop """
    with open("doodle.py") as source:
        tree = ast.parse(source.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
        if not analyzer.has_for():
            raise check50.Failure("no for loop found")

@check50.check(exists)
def testwhile():
    """check for at least one while loop"""
    with open("doodle.py") as source:
        tree = ast.parse(source.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
        if not analyzer.has_while():
            raise check50.Failure("no while loop found")

@check50.check(exists)
def testdefs():
    """check for at least 3 user-defined functions"""
    with open("doodle.py") as source:
        tree = ast.parse(source.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
        if not analyzer.has_while():
            raise check50.Failure("need a least 3 function defs: one per shape")

@check50.check(exists)
def testdefs():
    """check for at least 3 calls to user-defined functions"""
    with open("doodle.py") as source:
        tree = ast.parse(source.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
        if not analyzer.has_call():
            raise check50.Failure("need to call your 3 user-defined functions at least once")
            
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
