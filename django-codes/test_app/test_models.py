from django.test import TestCase
from core.models import Contact


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = {
            'name' : 'John',
            'email': 'john@google.com',
            'subject': 'Test',
            'message': 'MEssage'
        }
        cls.contact = Contact.objects.create(**cls.data)

    def test_create_method(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)

    @classmethod
    def tearDownClass(cls) -> None:
        pass