import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse


from polls.models import Question

def create_question(question_text, days):
    """
    Create a question with a given 'question_text' at 'days' offset from the
    current time. eg. Negative days for the past positive for the future
    """
    time = timezone.now() + timezone.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date=time)



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


    def test_was_created_recently_with_past_question(self):
        """
        was_published_recently() should return False for questions whose
         pub_date is older than one day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(pub_date=time)
        self.assertEqual(past_question.was_published_recently(), False)


    def test_was_created_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within one day of the current date
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date = time)
        self.assertEqual(recent_question.was_published_recently(), True)

# Create your tests here.
#question view tests
class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        res =  response.context['latest_question_list']

        self.assertQuerysetEqual(response.context['latest_question_list'],[] )


    def test_index_view_with_a_past_question(self):
        """
        QUestions with a pub_date in the past should be displayed on
        the index page
        """
        create_question("Past Question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        ['<Question: Past Question.>']
        )


    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed
        on the index page
        """

        create_question("Future Question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        []
        )

    def test_index_view_with_a_future_question_and_a_past_question(self):
        """
        Even if both future and past questions exist only past questions
        should be displayed
        """

        create_question("Future Question.", days=30)
        create_question("Past Question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        ['<Question: Past Question.>']
        )


    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions
        """
        create_question("Past Question 1.", days=-30)
        create_question("Past Question 2.", days=-29)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
        response.context['latest_question_list'],
        ['<Question: Past Question 2.>', '<Question: Past Question 1.>']
        )


class QuestionIndexDetailTest(TestCase):

    def test_question_index_view_with_a_future_question(self):
        """
        The detail view for a future question index should return a
        404 not found
        """
        future_question = create_question("Future Question.", days=5)

        response = self.client.get(reverse('polls:detail',
                                    args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)


    def test_question_index_view_with_a_past_question(self):
        """
        The detail view for a past question index should display
        the questions text
        """

        past_question = create_question("Past Question.", days=-5)

        response = self.client.get(reverse('polls:detail',
                                    args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
                                    status_code = 200)
