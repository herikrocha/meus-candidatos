from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class UserSkillsTestCase(TestCase):
    
    def setUp(self):
        self.userSkills = UserSkills.objects.create(fullName='Alberto Silva',email='alfred@gmail.com',html=5,css=5,javascript=5,python=5,django=5,iosDevelopment=5,androidDevelopment=5)

    def tearDown(self):
        self.userSkills.delete()

    def test_user_skills_success(self):
        data = {'fullName': 'Alberto Silva','email': 'alfred@gmail.com','html': 5,'css': 5,'javascript': 5,'python': 5,'django': 5,'iosDevelopment': 5,'androidDevelopment': 5}
        client = Client()
        response = client.get('/')



class IndexTest(TestCase):
    
    def test_home_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
