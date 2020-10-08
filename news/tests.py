from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.priscilla= Editor(first_name = 'Priscilla', last_name ='Ungai', email ='priscillaungai99@gmail.com')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.priscilla,Editor))

        # Testing Save Method
    def test_save_method(self):
        self.priscilla.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)