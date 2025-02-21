from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class HomePageTest(TestCase):

    def  test_status_code(self):
        #TODO some sort of test 

        response=self.client.get(reverse("landing_page"))
        # print(response.content)
        self.assertEqual(response.status_code,200)


    def test_template_name(self):
        # TODO 
        response=self.client.get(reverse("landing_page"))

        self.assertTemplateUsed(response,"leads/landing_page.html")
        

