from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Task
class SecurityTest(TestCase):

	def setUp(self):
		username = "user1"
		password = "123456"
		email= "user1@nd.edu"
		User.objects.create_user(username, email, password)
		self.client = Client()

	def test1(self):
		# response = self.client.get("/tasktracker/")
		#print(response)
		# redirect is good
		# self.assertEqual(response.status_code, 302)
		# self.assertEqual(response.url, '/accounts/login/')
		# 
		# my_input = {"username":"1' or '1' = '1",
		# "password":"1' or '1' = '1"}
		# response = self.client.post(
		# 	response.url,
		# 	my_input)

		self.client.login(username='user1', password='123456')
		response = self.client.get('/tasktracker/')
		# print(dir(response))
		# print(response.content)
		
		# print('-----------------------')
		# print(response, dir(response), 'xd')
		# print(response.content, response.status_code)
		my_add = {"title":'need to write paper <script>document.write("This is not good");</script>', 'due_date':'1111-1-1', 'status': 'C'}
		request = self.client.post('/tasktracker/add/', my_add)
		#print(request.status_code)
		response = self.client.get('/tasktracker/')
		self.assertFalse(b'This is not good' in response.content)
		#print(response.content)
		# print(response)
		# print(dir(response))
		# print(response.content)
		# print(b"This is not good" in response.content)
		#print(response)
		#self.assertEqual(response.url, '/tasktracker/')

		# my_add = {"title":'<script>alert(“hello”);</script>', 'due_date':'1111-1-1', 'status': '0'}
		# response = self.client.post('/tasktracker/add/', my_add)
		
		# error_message = b"Your username and password didn't match"
		# self.assertTrue(error_message in response.content)


	# def test2(self):
	# 	self.client.login(username="user1",password="123456")
	# 	my_input = {
	# 		"title": "'); DROP TABLE tasktracker_task; --",
	# 		"due_date":"2022-05-01",
	# 		"status":"I"
	# 	}
	# 	response = self.client.post("/tasktracker/add", my_input)
	# 	all_tasks = Task.objects.all()
	# 	self.assertEqual(len(all_tasks), 1)
			
			

