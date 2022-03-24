from django.test import TestCase
from.models import Editor,Article, tags

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.tracy= Editor(first_name = 'Tracy', last_name ='Wangari', email ='tracyjacobs775@gmail.com')

    #Testing instance
def test_instance(self):
        self.assertTrue(isinstance(self.tracy,Editor))
  
    # Testing Save Method
def test_save_method(self):
        self.tracy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)