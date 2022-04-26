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

		self.client.login(username='user1', password='123456')
		response = self.client.get('/tasktracker/')

		my_add = {"title":'need to write paper <script>document.write("This is not good");</script>', 'due_date':'1111-1-1', 'status': 'C'}
		request = self.client.post('/tasktracker/add/', my_add)
		#print(request.status_code)
		response = self.client.get('/tasktracker/')
		self.assertFalse(b'This is not good' in response.content)
			
class DeleteTest(TestCase):
    def setUp(self):
        username = "test_user"
        password = "password"
        email = "test_user@nd.edu"
        User.objects.create_user(username, email, password)

        setup_client = Client()
        setup_client.login(username=username, password=password)
        response = setup_client.post("/tasktracker/add/", {"title": "test_user task", "due_date": "2022-05-01", "status": "I"})

    # without logging in, we attempt to delete a task
    def test1(self):
        tasks = Task.objects.all()
        initial_length = len(tasks)
        print(initial_length)
        id_remove = tasks[0].id

        client = Client()
        url = f"/tasktracker/delete/{id_remove}/"
        response = client.get(url)
        tasks = Task.objects.all()
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertEqual(len(tasks), initial_length)

