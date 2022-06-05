from django.http import response
from django.test import TestCase

# Create your tests here.
class TestFile(TestCase):
    def testHome(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def testSignup(self):
        response=self.client.get('/signup')
        self.assertEqual(response.status_code,200)
    # def testLogin(self):
    #     response=self.client.get('/login')
    #     self.assertEqual(response.status_code,200)
    # def testAdditem(self):
    #     response=self.client.get('/additem')
    #     self.assertEqual(response.status_code,200)
    # def testfilter(self):
    #     response=self.client.get('/filter')
    #     self.assertEqual(response.status_code,200)