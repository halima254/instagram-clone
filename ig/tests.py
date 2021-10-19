from django.test import TestCase
from .models import Profile,Post,Comment,Like

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.halima=Profile(pic="img.png",bio="beautiful",userId=1)
    def test_instance(self):
        self.assertTrue(isinstance(self.halima,Profile))

    def test_initialization(self):
        self.assertEqual(self.halima.pic,"img.png")
        self.assertEqual(self.collo.bio,"beautiful")
        self.assertEqual(self.collo.userId,1)

    def test_save(self):
        self.halima.save_profile()
        prof=Profile.objects.all()
        self.assertTrue(len(prof)>0)

    def test_delete(self):
        self.halima.delete_profile()
        prof=Profile.objects.all()
        self.assertEqual(len(prof),0)

class TestImage(TestCase):
    def setUp(self):
        self.comment=Comments(images=1,comment='this is dope')
        self.follow=Followers(user="halima",insta='like',user_id=1)
        self.new_image=Image(image="image",name="nature",caption="amazing",likes=0,userId=10)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

  

 




