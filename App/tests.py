from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.utils import timezone

from App.views import details_post, posts_for_date, home
from .models import Post

class Post_Teste_models(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title = 'teste post',
            summary='Resumo do teste',
            content='Conteúdo do teste',
            date_creat=timezone.now(),
            category='Tecnologia'
        )

    def test_title_field_model(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')


    def teste_summary_field_model(self):
        post = Post.objects.get(id=1)
        fiel_label = post._meta.get_field('summary').verbose_name
        self.assertEqual(fiel_label, 'summary')


    def teste_content_field_model(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    
    def teste_date_creat_field_model(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('date_creat').verbose_name
        self.assertEqual(field_label, 'date creat')

    
    def teste_category_field_model(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('category').verbose_name
        self.assertEqual(field_label,'category')


    def teste_string_return_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), post.title)


class ViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.post = Post.objects.create(
            title='Teste Post',
            summary='Resumo do teste',
            content='Conteúdo do teste',
            date_creat='2023-08-19',
            category='Tecnologia'
        )

    def test_home_view(self):
        request = self.factory.get(reverse('home'))
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste Post')  # Verifica se o título do post está no conteúdo da resposta


    def test_posts_for_date_view(self):
        date = '2023-08-19'
        url = reverse('posts_for_date', args=[date])
        request = self.factory.get(url)
        response = posts_for_date(request, date=date)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste Post')


    def test_details_post_view(self):
        request = self.factory.get(reverse('details_post', args=[self.post.id]))
        response = details_post(request, id_post=self.post.id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste Post')  # Verifica se o título