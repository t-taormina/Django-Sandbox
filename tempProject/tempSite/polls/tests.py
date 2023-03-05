from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question
import datetime

# Create your tests here.


def create_question(text, day_offset):
    """
    Creates a question with text as the question_text and with an offset from
    timezone.now(). Positive days will result in future dates. Negative
    days will result in past dates.
    """
    time = timezone.now() + datetime.timedelta(days=day_offset)
    return Question.objects.create(question_text=text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_future_date_is_not_recent(self):
        """
        was_published_recently() returns False for future dates.
        """
        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Future Question", pub_date=future_date)
        self.assertIs(future_question.was_published_recently(), False)

    def test_old_question_is_not_recent(self):
        """
        was_published_recently() returns False for questions
        with a pub_date older than 1 day ago.
        """
        old_date = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=old_date)
        self.assertIs(old_question.was_published_recently(), False)

class QuestionIndexViewTests(TestCase):
    
    def test_no_questions(self):
        # get a response
        response = self.client.get(reverse('polls:index'))
        # verify response status code
        self.assertEqual(response.status_code, 200)
        # response contains appropriate text.
        self.assertContains(response, "No polls are available.")
        # verify an empty query set with context latest question list
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question(self):
        create_question(text="Future Question", day_offset=5)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_questions(self):
        return

    def test_past_questions(self):
        return





