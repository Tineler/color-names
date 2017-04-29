import dist.colornames as color_names
import unittest


class TestColorNames(unittest.TestCase):

    def test_name(self):
        self.assertEqual(color_names.by_name['Zorba'], '#a29589')


class TestColorValue(unittest.TestCase):

    def test_value(self):
        self.assertEqual(color_names.by_value['#014b43'], 'Aqua Deep')
