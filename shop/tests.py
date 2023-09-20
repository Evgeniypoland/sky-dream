from django.test import TestCase
from .models import Helmets

# Create your tests here.
class TestShop(TestCase):
    def test_index(self):
        response = self.client.get('')

    def test_parachutes(self):
        response = self.client.get('/parachutes/')
        self.assertEqual(response.status_code, 200)

    def test_hayduke(self):
        response = self.client.get('/parachutes/hayduke-2')
        self.assertEqual(response.status_code, 301)

class HelmetsModelTestCase(TestCase):
    def setUp(self):
        self.helmet = Helmets.objects.create(name='Test helmet1', description='Good', price=1000)
        Helmets.objects.create(name='Test helmet2', description='Normal', price=700)
        Helmets.objects.create(name='Test helmet3', description='Bad', price=500)

    @staticmethod
    def print_info(message):
        count = Helmets.objects.count()
        print(f'{message}: all_helmets = {count}')

    def test_helmet_creation(self):
        self.print_info('Start test_helmet_creation')
        self.assertEqual(self.helmet.name, 'Test helmet1')
        self.assertEqual(self.helmet.description, 'Good')
        self.assertEqual(self.helmet.price, 1000)
        self.assertEqual(self.helmet.slug, 'test-helmet1')
        self.print_info('Finish test_helmet_creation')

    def test_helmet_get_record(self):
        self.print_info('Start test_helmet_get_record')
        first = Helmets.objects.get(name='Test helmet1')
        self.assertEqual(first.price, 1000)
        self.print_info('Finish test_helmet_get_record')