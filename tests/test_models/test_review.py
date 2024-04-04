#!/usr/bin/python3
"""test_Review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """test_Review """

    def __init__(self, *args, **kwargs):
        """test_Review """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_Review_place_id(self):
        """ test_Review """
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_Review_user_id(self):
        """test_Review """
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_Review_text(self):
        """test_Review """
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))