# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel
import argparse
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

import unittest
from unittest.mock import patch, MagicMock

from . import ast, int
from .int import Interpreter
from .int import State
from wlang.ast import parse_string

from wlang.ast import *
class RelExp(BExp):
    """A relational comparison expression"""


    def __init__(self, lhs, op, rhs):
        super(RelExp, self).__init__(op, [lhs, rhs])

    def __str__(self):
        return f"{self.arg(0)} {self.op} {self.arg(1)}"


class AExp(Exp):
    """An arithmetic expression"""

    def __init__(self, op, args):
        super(AExp, self).__init__(op, args)

    def __str__(self):
        if self.is_unary():
            return f"{self.op}{self.arg(0)}"
        else:
            return f"{self.arg(0)} {self.op} {self.arg(1)}"

class TestMissingStatements(unittest.TestCase):
    @patch('sys.argv', ['in_file', 'example_file.wl'])
    def test_parse_args_with_valid_arguments(self):
        args = int._parse_args()
        self.assertEqual(args.in_file, 'example_file.wl')

    def test_one(self):
        prg1 = "x := 10; print_state"
        # test parser
        ast1 = ast.parse_string(prg1)

        interp = int.Interpreter()
        st = int.State()
        st = interp.run(ast1, st)
        self.assertIsNotNone(st)
        # x is defined
        self.assertIn("x", st.env)
        # x is 10
        self.assertEquals(st.env["x"], 10)
        # no other variables in the state
        self.assertEquals(len(st.env), 1)


    def test_two(self):
        prg1 = "x := 10; print_state"
        prg2 = "x := 12; print_state2; y := 10"
        # test parser
        ast1 = ast.parse_string(prg1)
        ast2 = ast.parse_string(prg2)
        print(ast1)
        repr(ast1)
        print(type(self) == type(ast1))
        print(type(ast2) == type(ast1))
        print(ast1 == ast2)

        # test Ifstmt
        stmt1 = ast.IfStmt(True, 'print("Then")', 'print("Else")')
        stmt2 = ast.IfStmt(True, 'print("Then")', 'print("Else")')
        stmt3 = ast.IfStmt(False, 'print("Then")')
        print(stmt1 == stmt2)  # Output: True, because all attributes are equal
        print(stmt1 == stmt3)

        # test Whilestmt
        stmt1 = ast.WhileStmt(True, 'print("Body")', 'inv_condition_1')
        stmt2 = ast.WhileStmt(True, 'print("Body")', 'inv_condition_1')
        stmt3 = ast.WhileStmt(False, 'print("Different Body")', 'inv_condition_2')

        # Using == operator, which calls __eq__ method internally
        print(stmt1 == stmt2)  # Output: True, because all attributes are equal
        print(stmt1 == stmt3)




    def test_relational_expression(self):
        # Test cases for relational expressions (RelExp)
        rel_exp_1 = RelExp(IntVar("x"), "<", IntVar("y"))
        rel_exp_2 = RelExp(IntVar("a"), ">=", IntConst(0))

        self.assertEqual(str(rel_exp_1), "x < y")
        self.assertEqual(str(rel_exp_2), "a >= 0")

    def test_arithmetic_expression(self):
        # Test cases for arithmetic expressions (AExp)
        a_exp_1 = AExp("+", [IntVar("x"), IntVar("y")])
        a_exp_2 = AExp("-", [IntVar("a"), IntConst(5)])





        self.assertEqual(str(a_exp_1), "x + y")
        self.assertEqual(str(a_exp_2), "a - 5")


        #mul_node = Node("*", OperandNode(3), OperandNode(4))
        #div_node = Node("/", OperandNode(8), OperandNode(2))


        a_exp_3 = AExp("*", [IntVar("x"), IntVar("y")])
        a_exp_4 = AExp("/", [IntVar("a"), IntConst(5)])


        interpreter = int.Interpreter()


        state = int.State()
        state.env = {"x": 10, "y": 5, "a": 15}


        interpreter.visit_AExp(a_exp_3, state=state)
        interpreter.visit_AExp(a_exp_4, state=state)



        self.assertEqual(str(a_exp_3), "x * y")
        self.assertEqual(str(a_exp_4), "a / 5")





    def test_assignment_statement(self):
        # Test cases for assignment statements (AsgnStmt)
        asgn_stmt_1 = AsgnStmt(IntVar("x"), IntVar("y"))
        asgn_stmt_2 = AsgnStmt(IntVar("a"), AExp("*", [IntConst(2), IntVar("b")]))

        self.assertEqual(str(asgn_stmt_1), "x := y")
        self.assertEqual(str(asgn_stmt_2), "a := 2 * b")

    def test_assert_statement(self):
        # Test cases for assert statements (AssertStmt)
        assert_stmt_1 = AssertStmt(RelExp(IntVar("x"), "<", IntVar("y")))
        assert_stmt_2 = AssertStmt(BExp("and", [BoolConst(True), BoolConst(False)]))

        self.assertEqual(str(assert_stmt_1), "assert x < y")
        self.assertEqual(str(assert_stmt_2), "assert true and false")

    def test_assume_statement(self):
        # Test cases for assume statements (AssumeStmt)
        assume_stmt_1 = AssumeStmt(RelExp(IntVar("a"), ">=", IntConst(0)))
        assume_stmt_2 = AssumeStmt(BoolConst(False))

        self.assertEqual(str(assume_stmt_1), "assume a >= 0")
        self.assertEqual(str(assume_stmt_2), "assume false")

    def test_havoc_statement(self):
        # Test cases for havoc statements (HavocStmt)
        havoc_stmt_1 = HavocStmt([IntVar("x"), IntVar("y")])
        havoc_stmt_2 = HavocStmt([IntVar("a")])

        self.assertEqual(str(havoc_stmt_1), "havoc x, y")
        self.assertEqual(str(havoc_stmt_2), "havoc a")

    def test_if_statement(self):
        # Test cases for if statements (IfStmt)
        if_stmt_1 = IfStmt(
            RelExp(IntVar("x"), "<", IntVar("y")),
            AsgnStmt(IntVar("a"), IntConst(1)),
            AsgnStmt(IntVar("b"), IntConst(2))
        )
        if_stmt_2 = IfStmt(
            BoolConst(False),
            AsgnStmt(IntVar("x"), IntVar("y"))
        )

        self.assertEqual(str(if_stmt_1), "if x < y then\n  a := 1\nelse\n  b := 2")
        self.assertEqual(str(if_stmt_2), "if false then\n  x := y")

    def test_while_statement(self):
        # Test cases for while statements (WhileStmt)
        while_stmt_1 = WhileStmt(
            RelExp(IntVar("x"), "<", IntVar("y")),
            AsgnStmt(IntVar("x"), AExp("+", [IntVar("x"), IntConst(1)]))
        )
        while_stmt_2 = WhileStmt(
            BoolConst(True),
            HavocStmt([IntVar("a"), IntVar("b")])
        )

        self.assertEqual(str(while_stmt_1), "while x < y do\n  x := x + 1")
        self.assertEqual(str(while_stmt_2), "while true do\n  havoc a, b")

class TestInt(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def test_assignment(self):
        prg = "x := 10; y := 5; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        final_state = self.interpreter.run(ast_tree, initial_state)

        self.assertIn("x", final_state.env)
        self.assertIn("y", final_state.env)
        self.assertEqual(final_state.env["x"], 10)
        self.assertEqual(final_state.env["y"], 5)

    def test_conditionals_true_branch(self):
        prg = "x := 10; if x <= 10 then y := 5 else y := 0; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        final_state = self.interpreter.run(ast_tree, initial_state)

        self.assertIn("x", final_state.env)
        self.assertIn("y", final_state.env)
        self.assertEqual(final_state.env["x"], 10)
        self.assertEqual(final_state.env["y"], 5)

    def test_conditionals_false_branch(self):
        prg = "x := 10; if x > 10 then y := 5 else y := 0; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        final_state = self.interpreter.run(ast_tree, initial_state)

        self.assertIn("x", final_state.env)
        self.assertIn("y", final_state.env)
        self.assertEqual(final_state.env["x"], 10)
        self.assertEqual(final_state.env["y"], 0)

    def test_while_loop(self):
        prg = "x := 5; while x > 0 do x := x - 1; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        final_state = self.interpreter.run(ast_tree, initial_state)

        self.assertIn("x", final_state.env)
        self.assertEqual(final_state.env["x"], 0)

    def test_assumption_holds(self):
        prg = "x := 10; assume x > 5; y := x - 5; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        final_state = self.interpreter.run(ast_tree, initial_state)

        self.assertIn("x", final_state.env)
        self.assertIn("y", final_state.env)
        self.assertEqual(final_state.env["x"], 10)
        self.assertEqual(final_state.env["y"], 5)

    def test_assumption_fails(self):
        prg = "x := 3; assume x > 5; y := x - 5; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        with self.assertRaises(AssertionError):
            self.interpreter.run(ast_tree, initial_state)

    def test_havoc(self):
        prg = "havoc x, y; print_state"
        ast_tree = ast.parse_string(prg)
        initial_state = State()

        final_state = self.interpreter.run(ast_tree, initial_state)

        self.assertIn("x", final_state.env)
        self.assertIn("y", final_state.env)

if __name__ == '__main__':
    unittest.main()
