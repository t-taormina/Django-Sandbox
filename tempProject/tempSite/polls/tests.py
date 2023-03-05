from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

# Create your tests here.


def create_question(text, days):
    """
    Creates a question with text as the question_text and with an offset from
    timezone.now(). Positive days will result in future dates. Negative
    days will result in past dates.
    """
    time = timezone.now() + datetime.timedelta(days=offset)
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
        return 

    def test_future_question(self):
        return

    def test_future_and_past_questions(self):
        return

    def test_past_questions(self):
        return





