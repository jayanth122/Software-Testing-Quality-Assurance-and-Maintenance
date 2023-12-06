# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from . import ast


class UndefVisitor(ast.AstVisitor):
    """Computes all variables that are used before being defined"""

    def __init__(self):
        super(UndefVisitor, self).__init__()
        self.defined_vars = set()
        self.undefined_vars = set()
        pass


    def check(self, node):
        self.visit(node)

    def get_undefs(self):
        return self.undefined_vars
    
    def visit_IntConst(self, node, *args, **kwargs):
        # Handle the IntConst node here if needed
        pass


    def visit_StmtList(self, node, *args, **kwargs):
        for stmt in node.stmts:
            self.visit(stmt)

    def visit_IntVar(self, node, *args, **kwargs):
        if node.name not in self.defined_vars:
            self.undefined_vars.add(node.name)

    def visit_AsgnStmt(self, node, *args, **kwargs):
        self.defined_vars.add(node.lhs.name)
        self.visit(node.rhs)

    def visit_Exp(self, node, *args, **kwargs):
        for arg in node.args:
            self.visit(arg)

    def visit_HavocStmt(self, node, *args, **kwargs):
        for var in node.vars:
            self.defined_vars.add(var.name)

    def visit_AssertStmt(self, node, *args, **kwargs):
        self.visit(node.cond)

    def visit_AssumeStmt(self, node, *args, **kwargs):
        self.visit(node.cond)

    def visit_IfStmt(self, node, *args, **kwargs):
        self.visit(node.cond)
        self.visit(node.then_stmt)
        if node.has_else():
            self.visit(node.else_stmt)

    def visit_WhileStmt(self, node, *args, **kwargs):
        self.visit(node.cond)
        self.visit(node.body)