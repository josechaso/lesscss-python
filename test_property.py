import unittest
from property import parse_property


class TestAccessor(unittest.TestCase):
    def test_mixin(self):
        self.assertRaises(ValueError, parse_property, '#bundle > .button;')
                         
    def test_property(self):
        self.assertRaises(ValueError, parse_property, ".article['color'];")
                         
    def test_variable(self):
        self.assertRaises(ValueError, parse_property, "#defaults[@width];")


class TestFont(unittest.TestCase):
    def setUp(self):
        self.property = parse_property('''src: local('Vollkorn'),
url('http://themes.googleusercontent.com/font?kit=_3YMy3W41J9lZ9YHm0HVxA')
format('truetype');''')

    def test_name(self):
        self.assertEqual(self.property.name, 'src')
    
    def test_value(self):
        self.assertEqual(self.property.value, '''local('Vollkorn'),
url('http://themes.googleusercontent.com/font?kit=_3YMy3W41J9lZ9YHm0HVxA')
format('truetype')''')


class TestContent(unittest.TestCase):
    def setUp(self):
        self.property = parse_property("content: '\0000A9';")
        
    def test_name(self):
        self.assertEqual(self.property.name, 'content');
        
    def test_value(self):
        self.assertEqual(self.property.value, "'\0000A9'");


class TestContentURL(unittest.TestCase):
    def setUp(self):
        self.property = parse_property("content: url(/uri);")
        
    def test_name(self):
        self.assertEqual(self.property.name, 'content');
        
    def test_value(self):
        self.assertEqual(self.property.value, "url(/uri)");


class TestLength(unittest.TestCase):
    def test_single_line(self):
        self.assertEqual(parse_property('display:block;display:none').value,
                         'block')

    def test_multi_line(self):
        self.assertEqual(parse_property('display:block;\ndisplay:none').value,
                         'block')

    def test_multi_line_value(self):
        self.assertEqual(parse_property('''src: local('Vollkorn'),
url('http://themes.googleusercontent.com/font?kit=_3YMy3W41J9lZ9YHm0HVxA')
format('truetype');
display: block;''').value,'''local('Vollkorn'),
url('http://themes.googleusercontent.com/font?kit=_3YMy3W41J9lZ9YHm0HVxA')
format('truetype')''')


if __name__ == '__main__':
    unittest.main()