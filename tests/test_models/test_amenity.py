#!/usr/bin/python3
'''Unittest for base_model.py([..])'''
from datetime import datetime
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''Define unit test for the Amenity Class'''
    def test_init_a(self):
        '''Tests the __init__ function'''
        a = Amenity()
        self.assertEqual(type(a), Amenity)
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_init_b(self):
        '''Tests the __init__ function'''
        b = Amenity()
        self.assertEqual(type(b), Amenity)
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)

    def test_add_attribute_a(self):
        a = Amenity()
        a.name = 'KSI'
        a.number = 999
        self.assertEqual(a.name, 'KSI')
        self.assertEqual(a.number, 999)
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.number), int)

    def test_add_attribute_b(self):
        b = Amenity()
        b.name = 'Swarmz'
        b.number = 0
        self.assertEqual(b.name, 'Swarmz')
        self.assertEqual(b.number, 0)
        self.assertEqual(type(b.name), str)
        self.assertEqual(type(b.number), int)

    def test_str_a(self):
        '''Tests the __str__ function'''
        a = Amenity()
        nm = a.__class__.__name__
        dc = a.__dict__
        self.assertEqual(a.__str__(), f"[{nm}] ({a.id}) {dc}")

    def test_str_b(self):
        '''Tests the __str__ function'''
        b = Amenity()
        nm = b.__class__.__name__
        dc = b.__dict__
        self.assertEqual(b.__str__(), f"[{nm}] ({b.id}) {dc}")

    def test_save_a(self):
        '''Tests the save function'''
        a = Amenity()
        cd = a.created_at.isoformat()
        ud = a.updated_at.isoformat()
        self.assertEqual(cd, ud)
        a.save()
        self.assertNotEqual(ud, a.updated_at.isoformat())

    def test_save_b(self):
        '''Tests the save function'''
        b = Amenity()
        cd = b.created_at.isoformat()
        ud = b.updated_at.isoformat()
        self.assertEqual(cd, ud)
        b.save()
        self.assertNotEqual(ud, b.updated_at.isoformat())

    def test_to_dict_a(self):
        '''Tests the to_dict function'''
        a = Amenity()
        dc = a.to_dict()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)
        self.assertEqual(dc['__class__'], 'Amenity')
        self.assertEqual(type(dc['updated_at']), str)
        self.assertEqual(type(dc['created_at']), str)

    def test_to_dict_b(self):
        '''Tests the to_dict function'''
        b = Amenity()
        dc = b.to_dict()
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)
        self.assertEqual(dc['__class__'], 'Amenity')
        self.assertEqual(type(dc['updated_at']), str)
        self.assertEqual(type(dc['created_at']), str)


if __name__ == '__main__':
    unittest.main()
