from django.test import TestCase, Client
from rest_framework.test import APIClient
from stories.models import Category, Tag
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
import os


class RecipeAPIViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        cls.url = reverse_lazy('recipes-list')
        cls.response = client.get(cls.url)
        category = Category.objects.create(title = 'Category 1')
        tag = Tag.objects.create(title = 'Tag 1')
        file_path = os.path.join(settings.MEDIA_ROOT, 'recipe_images/recipe_1_3YzO93k.jpeg')
        cls.data = {
            'title' : 'Recipe 34',
            'category' : category.id,
            'tags' : tag.id,
            'small_description' : 'small_description',
            'description' : 'Description',
            'image' : (open(file_path, 'rb'),),
            'cover_image': (open(file_path, 'rb'),)
        }
        cls.post_valid = client.post(cls.url, data=cls.data)
    
    def test_url(self):
        self.assertEqual(self.url, '/api/recipes/')

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_status_code(self):
        self.assertEqual(self.post_valid.status_code, 201)

    
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass