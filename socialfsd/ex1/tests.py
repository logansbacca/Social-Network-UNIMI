import unittest
from django.test import Client
from ex1.models import User, Post
import random


class TestEx1(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.u = User(username='usertest', password='passwordtest')
        self.p = Post(author=self.u, text='Post text for testing purpose!')

    def setUp(self):
        self.c = Client()
        
    def user_create_test(self):
        self.u.save()
        
    def user_delete_test(self):
        self.u.delete()
        
    def post_create_test(self):
        self.p.save()
        
    def post_delete_test(self):
        self.p.delete()
        
    def test_username_exist(self):
        self.user_create_test()
        
        response = self.c.get(f'/ex1/user/{self.u.username}/')
        self.assertEqual(response.status_code, 200, 'expecting http error code 200')
        self.assertIn(self.u.username, str(response.content), f'expecting "{self.u.username}" as text inside webpage')
        
        self.user_delete_test()
        
    def test_username_not_exist(self):
        username = '2uhf0ehiyg78er58ff13'
        response = self.c.get(f'/ex1/user/{username}/')
        self.assertEqual(response.status_code, 404, 'expecting http error code 404 when username was not found')
        
    def test_post_not_exist(self):
        post_id = random.randint(10000, 99999)
        response = self.c.get(f'/ex1/post/{post_id}/')
        self.assertEqual(response.status_code, 404, 'expecting http error code 404')
        
    def test_post_exist(self):
        self.user_create_test()
        self.post_create_test()
        
        response = self.c.get(f'/ex1/post/{self.p.id}/')
        self.assertEqual(response.status_code, 200, 'expecting http error code 200')
        self.assertIn(self.p.text, str(response.content), f'expecting "{self.p.text}" as text inside webpage')
        
        self.post_delete_test()
        self.user_delete_test()

    def test_login_fail(self):
        username = "oqiuEHF92734RY9"
        password = "owquidbfifgioq"
        
        response = self.c.post("/ex1/login/", {'username': username, 'password': password})
        self.assertIn("User not found", str(response.content), 'Expecting "User not found"')
        self.assertIn("Wrong password", str(response.content), 'Expecting "Wrong password"')
        
    def test_login_ok(self):
        self.user_create_test()
        
        response = self.c.post("/ex1/login/", {'username': self.u.username, 'password': self.u.password})
        self.assertNotIn("User not found", str(response.content), 'Not expecting "User not found" inside page')
        self.assertNotIn("Wrong password", str(response.content), 'Not expecting "Wrong password" inside page')
        
        self.user_delete_test()
        

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
