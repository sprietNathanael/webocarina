import unittest

from models import *


class TestModels(unittest.TestCase):
    
    def test_init(self):
        self.assertRaises(AttributeError, TypeOcarina, None, None)
        self.assertRaises(AttributeError, TypeOcarina, None, 1)
        self.assertRaises(AttributeError, TypeOcarina, "", 1)
        self.assertRaises(AttributeError, TypeOcarina, "test", None)
        self.assertRaises(AttributeError, TypeOcarina, "test", 0)
        self.assertRaises(AttributeError, TypeOcarina, "test", -1)

        self.assertRaises(AttributeError, Performer, None)
        self.assertRaises(AttributeError, Performer, "")

        self.assertRaises(AttributeError, TypeMedia, None)
        self.assertRaises(AttributeError, TypeMedia, "")

        self.assertRaises(AttributeError, Media, None, None, None)
        self.assertRaises(AttributeError, Media, None, None, 1)
        self.assertRaises(AttributeError, Media, None, 75, None)
        self.assertRaises(AttributeError, Media, None, 75, 1)
        self.assertRaises(AttributeError, Media, "test", None, None)
        self.assertRaises(AttributeError, Media, "test", None, 1)
        self.assertRaises(AttributeError, Media, "test", 75, None)
        self.assertRaises(AttributeError, Media, "", 75, 1)
        self.assertRaises(AttributeError, Media, "test", -1, 1)
        self.assertRaises(AttributeError, Media, "test", 0, 1)
        self.assertRaises(AttributeError, Media, "test", 75, 0.5)

        self.assertRaises(AttributeError, Occurrence, None, None, None, None, None)
        self.assertRaises(AttributeError, Occurrence, None, None, None, None, 1)
        self.assertRaises(AttributeError, Occurrence, None, None, None, "", None)
        self.assertRaises(AttributeError, Occurrence, None, None, None, "", 1)
        self.assertRaises(AttributeError, Occurrence, None, None, 1, None, None)
        self.assertRaises(AttributeError, Occurrence, None, None, 1, None, 1)
        self.assertRaises(AttributeError, Occurrence, None, None, 1, "", None)
        self.assertRaises(AttributeError, Occurrence, None, None, 1, "", 1)
        self.assertRaises(AttributeError, Occurrence, None, 1, None, None, None)
        self.assertRaises(AttributeError, Occurrence, None, 1, None, None, 1)
        self.assertRaises(AttributeError, Occurrence, None, 1, None, "", None)
        self.assertRaises(AttributeError, Occurrence, None, 1, None, "", 1)
        self.assertRaises(AttributeError, Occurrence, None, 1, 1, None, None)
        self.assertRaises(AttributeError, Occurrence, None, 1, 1, None, 1)
        self.assertRaises(AttributeError, Occurrence, None, 1, 1, "", None)
        self.assertRaises(AttributeError, Occurrence, None, 1, 1, "", 1)
        self.assertRaises(AttributeError, Occurrence, 1, None, None, None, None)
        self.assertRaises(AttributeError, Occurrence, 1, None, None, None, 1)
        self.assertRaises(AttributeError, Occurrence, 1, None, None, "", None)
        self.assertRaises(AttributeError, Occurrence, 1, None, None, "", 1)
        self.assertRaises(AttributeError, Occurrence, 1, None, 1, None, None)
        self.assertRaises(AttributeError, Occurrence, 1, None, 1, None, 1)
        self.assertRaises(AttributeError, Occurrence, 1, None, 1, "", None)
        self.assertRaises(AttributeError, Occurrence, 1, None, 1, "", 1)
        self.assertRaises(AttributeError, Occurrence, 1, 1, None, None, None)
        self.assertRaises(AttributeError, Occurrence, 1, 1, None, None, 1)
        self.assertRaises(AttributeError, Occurrence, 1, 1, None, "", None)
        self.assertRaises(AttributeError, Occurrence, 1, 1, None, "", 1)
        self.assertRaises(AttributeError, Occurrence, 1, 1, 1, None, None)
        self.assertRaises(AttributeError, Occurrence, 1, 1, 1, None, 1)
        self.assertRaises(AttributeError, Occurrence, 1, 1, 1, "", None)


if __name__ == '__main__':
    unittest.main()