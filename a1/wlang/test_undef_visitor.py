import unittest

from . import ast, undef_visitor


class TestUndefVisitor(unittest.TestCase):
    def test1(self):
        prg1 = "x := 12; y := x + z"
        ast1 = ast.parse_string(prg1)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        # UNCOMMENT to run the test
        self.assertEqual(set (['z']), uv.get_undefs ())

        pass

    def test_variable_used_before_definition(self):
        prg = "x := y + 2"
        ast2 = ast.parse_string(prg)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast2)
        self.assertEqual(set(['y']), uv.get_undefs())

        pass

    def test_undefined_variable_in_expression(self):
        prg = "x := 2; y := 5 * x + z"
        ast3 = ast.parse_string(prg)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast3)
        self.assertEqual(set(['z']), uv.get_undefs())
        pass

    def test_variable_definition_and_usage_in_havoc(self):
        prg = "havoc x; y := x"
        ast4 = ast.parse_string(prg)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast4)
        self.assertEqual(set(), uv.get_undefs())
        pass


    def test_nested_conditional_and_loop(self):
        prg = "x := 1; while x < 8 do if x > 3 then y := z else y := w"
        ast6 = ast.parse_string(prg)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast6)
        self.assertEqual(set(['z', 'w']), uv.get_undefs())