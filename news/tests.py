from django.test import TestCase
from .models import Editor,Article,tags

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