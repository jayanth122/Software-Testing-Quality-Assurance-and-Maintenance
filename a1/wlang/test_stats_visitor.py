import unittest

from . import ast, stats_visitor


class TestStatsVisitor(unittest.TestCase):
    def test_one(self):
        prg1 = "x := 12; print_state"
        ast1 = ast.parse_string(prg1)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        # UNCOMMENT to run the test
        self.assertEqual(sv.get_num_stmts(), 2)
        self.assertEqual(sv.get_num_vars(), 1)

        pass

    def test_visit_AsgnStmt(self):

        prg="x := 5; y := 3; z := x + y"

        ast7 = ast.parse_string(prg)

        sv = stats_visitor.StatsVisitor() 

        sv.visit(ast7)

        self.assertEqual(sv.get_num_stmts(), 3)

        pass


    def test_if_statement(self):


        prg2 = "if x > 10 then x := x + 2 else x := x - 2; print_state"
        ast2 = ast.parse_string(prg2)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast2)

        self.assertEqual(sv.get_num_stmts(), 4)
        self.assertEqual(sv.get_num_vars(), 1)

        pass

    def test_while_loop(self):
        prg3 = "while x > 0 do x := x - 1; print_state"
        ast3 = ast.parse_string(prg3)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast3)
        self.assertEqual(sv.get_num_stmts(), 3)
        self.assertEqual(sv.get_num_vars(), 1)

        pass

    def test_assert_statement(self):
        prg4 = "assert x > 0"
        ast4 = ast.parse_string(prg4)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast4)
        self.assertEqual(sv.get_num_stmts(), 1)
        self.assertEqual(sv.get_num_vars(), 0)

        pass

    def test_assume_statement(self):
        prg5 = "assume x > 0"
        ast5 = ast.parse_string(prg5)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast5)
        self.assertEqual(sv.get_num_stmts(), 1)
        self.assertEqual(sv.get_num_vars(), 0)

        pass

    def test_havoc_statement(self):
        prg6 = "havoc x, y, z"
        ast6 = ast.parse_string(prg6)

        sv = stats_visitor.StatsVisitor()
        sv.visit(ast6)
        self.assertEqual(sv.get_num_stmts(), 1)
        self.assertEqual(sv.get_num_vars(), 3)

        pass
