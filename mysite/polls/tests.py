import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

#test that was_created_recently doean't pass questions made in the future
class QuestionMethodTests(TestCase):

    def test_was_created_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

# Create your tests here.
