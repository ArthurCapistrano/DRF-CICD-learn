from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        
        response = self.client.post(
            reverse('token'), 
            {'username': 'testuser', 'password': 'testpass123'}
        )
        
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_task(self):
        response = self.client.post(
            '/api/tasks/', {'title': 'Test Task'}
        )
        
        # Se falhar, isso vai te mostrar se é erro no título, no usuário, etc.
        if response.status_code != 201:
            print(response.data) 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_task(self):
        task = Task.objects.create(user=self.user, title='Task to delete')
        response = self.client.delete(f'/api/tasks/{task.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
