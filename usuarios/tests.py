from django.test import TestCase
from unittest.case import TestCase
from django.test import Client
from django.contrib.auth.models import User

class UserViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('\nUserViewTests')

    