import unittest
from code.mydict import Dict


class TestDict(unittest.TestCase):
    def test_init(self):
        # 初始化a=1,b='test
        d = Dict(a=1, b='test')
        # 判断a是否为1
        self.assertEqual(d.a, 1)
        # 判断b是否为'test'
        self.assertEqual(d.b, 'test')
        # 判断d是否是dict的实例
        self.assertTrue(isinstance(d, dict))
        # 判断d是否是Dict的实例
        self.assertIsInstance(d, Dict)

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertIn('key', d)
        self.assertTrue('key' in d)

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
